import cv2
from extractFeatures import extractFeature
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
from sklearn.metrics import accuracy_score
from generateLable import generateLabel



dataSet = "ufdd"
classifierDir =  "DataSet/training/Classifier/"

#Directory where model is saved
model_path ="DataSet/training/Model/Classifier.pkl"
 
testLabelFile = "DataSet/test/testLabels/genLabel.txt"
# Load the classifier
classifier = joblib.load(model_path)

#testImagePath =  "DataSet/training/negativeImages/"

testImagePath = "DataSet/test/testdata/"


testFilePaths = []

#Generate Labels for negative Data Set
if dataSet == "negative":
	testImageLabels = "DataSet/test/testLabels/"
	if os.path.exists(testImageLabels):
		shutil.rmtree(testImageLabels)
	os.makedirs(testImageLabels)
	testLabelFile  = testImageLabels+"/genLabel.txt"
	generateLabel(testImagePath,None,testLabelFile,dataSet)
 

# Reading the file names from a textfile and they picking them up from the respective folder. this was required to generate lables.
print "Calculating testing set Labels and Data"
index = 1
for line in open(testLabelFile,'r').readlines():
	[filename,label] = line.split( )
	filepath = testImagePath+filename+".jpg"

	if os.path.isfile(filepath):
		if str(label) == '1':
			print "File Path  %s and label %s" %(filepath,str(label))
			testHog = extractFeature(filepath,"Test data",None,True)
			if index == 1 :
				dataTest = np.array([]).reshape(0,testHog.shape[0])
				testLabel = np.empty([0,1],dtype=int)
				index = 0
			mtestHog = testHog.reshape(1,testHog.shape[0])
			dataTest = np.append(dataTest,mtestHog,0)
			testLabel = np.append(testLabel,1)
			testFilePaths.append(os.path.join(testImagePath, filename))
		elif str(label) == '-1':
			if os.path.isfile(filepath):
				print "File Path",filepath
				testHog = extractFeature(filepath,"Test data",None,True)
				if index == 1 :
					dataTest = np.array([]).reshape(0,testHog.shape[0])
					testLabel = np.empty([0,1],dtype=int)
					index = 0
				mtestHog = testHog.reshape(1,testHog.shape[0])
				dataTest = np.append(dataTest,mtestHog,0)
				testLabel = np.append(testLabel,-1)
				testFilePaths.append(os.path.join(testImagePath, filename))

print "Test Data Feature descriptor and labels size"
print dataTest.shape
print testLabel.shape
# Predict the labekss of the trainning data
predictions = classifier.predict(dataTest)
#Calculate their accuracy 

scores = accuracy_score(testLabel, predictions)
print "Reported Scores ",scores
#Create Directory to save the predicted Files 
predictPath = "DataSet/test/predictedFiles/"

if os.path.exists(predictPath):
	shutil.rmtree(predictPath)
os.makedirs(predictPath)

count = 0
matchedIndex = []
pfileName = predictPath+"predictedLabels.txt"
if not os.path.isfile(pfileName):
	file = open(pfileName, "w") 
else:
	file = open(pfileName, "a")

print "Generating labels for predictions and saving them in a file"
for r in range(len(predictions)):
	if predictions[r] == 1 or  predictions[r] == '1' :
		count = count+1
		matchedIndex.append(r)
		file_name = os.path.basename(testFilePaths[r])
		stringData = file_name + " " + str(testLabel[r]) + "\n" 
		file.write( stringData  )
file.close()

print "Total Matched Count",count

print "Mathced Images Paths"
for index in range(len(matchedIndex)):
	FileName = os.path.split(testFilePaths[matchedIndex[index]])[1].split(".")[0]
	filepath = testFilePaths[matchedIndex[index]]+".jpg"
	if os.path.isfile(filepath):
		shutil.move(filepath, predictPath+FileName+".jpg")
