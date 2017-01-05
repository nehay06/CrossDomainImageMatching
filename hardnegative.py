import cv2
import os
import numpy as np
import fnmatch
from sklearn.svm import LinearSVC
from random import randint
from sklearn.externals import joblib
import os.path
import glob
import shutil
from shutil import copyfile
from generateLable import generateLabel
from extractFeatures import extractFeature
from extractImage import extractImage
from removeEasyExample import silentremove,removeEasyExamples

sourceDir = "DataSet/training/ufdd/classe21/"
#generate Label for False Positive Data
genFilePath = "DataSet/training/testLabels/genLabel.txt"
predictFilePath = "DataSet/test/predictedFiles/predictedLabels.txt"
predictedImPath = "DataSet/test/predictedFiles/"
classNum = "22"
dataset  = "negative"
#Positive Feature Directory
featureDir =  "DataSet/training/postiveFeatures/"

if dataset == "ufdd":
	generateLabel(predictedImPath,classNum,genFilePath,dataset)

#Negative DataSet Training Variable
fullNegativeTrainSet = "DataSet/training/negativeImages/"
negativeTrainSet = "DataSet/training/negativeTrainSet/"

# Directory where classfier will be save
classifierDir =  "DataSet/training/Model/"

if dataset == "ufdd":
	filePath = genFilePath
else:
	filePath = predictFilePath

#remove some files from negative training set
counter = 1
for filename in os.listdir(negativeTrainSet):
	if fnmatch.fnmatch(filename, '*.jpg') or fnmatch.fnmatch(filename, '*.png'):
		if counter == 50:
			break
		else:
			silentremove(negativeTrainSet+filename)
			counter = counter+1

#remove False Positive from Training Data Set
removeEasyExamples(negativeTrainSet,filePath)

#Move Flase postives from predicted data to negative training set
for line in open(filePath,'r').readlines():
	[filename,label] = line.split()
	impath = predictedImPath+filename+".jpg"
	print "NEHA PATH",impath
	if os.path.isfile(impath):
		print "label",label
		if str(label) == "-1":
			shutil.move(impath,negativeTrainSet+filename+".jpg")

#Extract more random image from  negative data set and add them to negativeTrainSet
extractImage(None,fullNegativeTrainSet,negativeTrainSet,"random","move")

#Calculate negative trainning data and labels
counter = 1
for filename in os.listdir(negativeTrainSet):
	if fnmatch.fnmatch(filename, '*.jpg') or fnmatch.fnmatch(filename, '*.png'):
		print filename
		negHog = extractFeature(negativeTrainSet+filename,"Negative",None,True)
		if counter == 1 :
			dataTrain = np.array([]).reshape(0,negHog.shape[0])
			dataLabel = np.empty([0,1],dtype=int)
			counter = 0
		mnegHog = negHog.reshape(1,negHog.shape[0])
		dataTrain = np.append(dataTrain,mnegHog,0)
		dataLabel = np.append(dataLabel,-1)

#lOAD positive features and create training vectors and labels
for feat_path in glob.glob(os.path.join(featureDir,"*.feat")):
	print "Positive feature File",feat_path
	posHOG = joblib.load(feat_path)
	mposHOG = posHOG.reshape(1,posHOG.shape[0])
	dataTrain = np.append(dataTrain,mposHOG,0)
	dataLabel = np.append(dataLabel,1)


print dataTrain.shape
print dataLabel

 # Load the classifier
classifier = joblib.load("DataSet/training/Model/Classifier.pkl")
classifier.fit(dataTrain, dataLabel)

# save Classifier 
if os.path.exists(classifierDir):
	shutil.rmtree(classifierDir)
os.makedirs(classifierDir)
print os.path.join(classifierDir, "Classifier.pkl")
joblib.dump(classifier, os.path.join(classifierDir, "Classifier.pkl"))
print "Classifier saved to {}".format(classifierDir)