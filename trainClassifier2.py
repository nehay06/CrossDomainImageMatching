import cv2
import os
import numpy as np
import fnmatch
from sklearn.svm import LinearSVC
from sklearn.externals import joblib
import os.path
import glob
import shutil
from shutil import copyfile
from extractImage import extractImage
from extractFeatures import extractFeature


#Define the directory path for Positive Sample. These folders will be generated after transformation
postiveTrainSet = "DataSet/training/postiveTrainSet/"
featureDir =  "DataSet/training/postiveFeatures/"


#Negative DataSet Training Variable
fullNegativeTrainSet = "DataSet/training/negativeImages/"
negativeTrainSet = "DataSet/training/negativeTrainSet/"

# Directory where classfier will be save
classifierDir =  "DataSet/training/Model/"


# Extract features from the Positive Sample 
extractFeature(postiveTrainSet,"Positive",featureDir,False)


# Load the positive features and create Training Data and Training Label
print "Calculating Positive training Labels and Data"
index = 1
for feat_path in glob.glob(os.path.join(featureDir,"*.feat")):
	print "Feature File Name",feat_path
	posHOG = joblib.load(feat_path)
	mposHOG = posHOG.reshape(1,posHOG.shape[0])
	if index == 1 :
		dataTrain = np.array([]).reshape(0,posHOG.shape[0])
		dataLabel = np.empty([0,1],dtype=int)
		index = 0
	dataTrain = np.append(dataTrain,mposHOG,0)
	dataLabel = np.append(dataLabel,1)

print "Calulated Trainning Data Size and Label "
print dataTrain.shape
print dataLabel.shape



extractImage(None,fullNegativeTrainSet,negativeTrainSet,"random","move")
print "Calculating Negative training Labels and Data"
#Negative data set extract features 
for filename in os.listdir(negativeTrainSet):
	if fnmatch.fnmatch(filename, '*.jpg') or fnmatch.fnmatch(filename, '*.png'):
		filepath  = negativeTrainSet+filename
		print "filepath",filepath
		if os.path.isfile(filepath): 
			negHog = extractFeature(filepath,"Negative",None,True)
			mnegHog = negHog.reshape(1,negHog.shape[0])
			dataTrain = np.append(dataTrain,mnegHog,0)
			dataLabel = np.append(dataLabel,-1)


#train SVM Model
classifier = LinearSVC(loss="hinge")
classifier.fit(dataTrain, dataLabel)

# save Classifier 
if os.path.exists(classifierDir):
	shutil.rmtree(classifierDir)
os.makedirs(classifierDir)
print os.path.join(classifierDir, "Classifier.pkl")
joblib.dump(classifier, os.path.join(classifierDir, "Classifier.pkl"))
print "Classifier saved to {}".format(classifierDir)


