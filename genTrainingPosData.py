import cv2
import os
import numpy as np
import fnmatch
from resizeImage import resizeIm
from random import randint
import os.path
import glob
import shutil
from test_transform import performTransformation
from shutil import copyfile
from extractImage import extractImage

#define the source  query directory 
sourceDir = "DataSet/training/ufdd/classe21/"

postiveTrainSet = "DataSet/training/postiveTrainSet/"
QueryImage = "DataSet/training/QueryImage/"

if os.path.exists(postiveTrainSet):
	shutil.rmtree(postiveTrainSet)
os.makedirs(postiveTrainSet)

#move Back the randomly tested files back to the source dir This is done to make sure after multiple iterations content of source dir are preserved
if os.path.exists(QueryImage):
	for filename in os.listdir(QueryImage):
		if fnmatch.fnmatch(filename, '*.jpg') or fnmatch.fnmatch(filename, '*.png'):
			filepath = QueryImage+filename
			print filename
			if os.path.isfile(filepath): 
				shutil.move(filepath,sourceDir+filename)
	shutil.rmtree(QueryImage)

os.makedirs(QueryImage)

#Create a test folder inside sourceDir and move one single postive image randomly inside this folder
FilesCount = len([name for name in os.listdir(sourceDir) if os.path.isfile(os.path.join(sourceDir, name))])
FileNum=randint(0,FilesCount)

print "Random File Number",FileNum
counter = 1
for filename in os.listdir(sourceDir):
	if fnmatch.fnmatch(filename, '*.jpg') or fnmatch.fnmatch(filename, '*.png'):
		if FileNum == counter:
			filepath = sourceDir+filename
			print filename
			if os.path.isfile(filepath): 
				copyfile(filepath, QueryImage+filename)
				shutil.move(filepath,postiveTrainSet+filename)
		counter = counter+1

#Define the directory path for Positive Sample. These folders will be generated after transformation
croppedImage = sourceDir+"croppedImage/"
aspectRatio = sourceDir+"aspectRatio/"
transformations= sourceDir+"transformations/"

#Create Positive Sample from a single positive Query Image
performTransformation("translate",postiveTrainSet,croppedImage)
performTransformation("cropImage",postiveTrainSet,aspectRatio)
performTransformation("aspectRatio",postiveTrainSet,transformations)

#move all files inside the positiveTestSet
extractImage(None,croppedImage,postiveTrainSet,"fixed","move")
extractImage(None,aspectRatio,postiveTrainSet,"fixed","move")
extractImage(None,transformations,postiveTrainSet,"fixed","move")

#set this flag to false if you don't want to delete the folders.
deleteTransformationFolder = True

if deleteTransformationFolder is True:
	if os.path.exists(croppedImage):
		shutil.rmtree(croppedImage)
	if os.path.exists(aspectRatio):
		shutil.rmtree(aspectRatio)
	if os.path.exists(transformations):
		shutil.rmtree(transformations)

