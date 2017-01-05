#This file contains code to extract those images from the predicted file whose true label was one or which were indeed the true matched 
#images

import os
import shutil
from shutil import copyfile

destDir = "DataSet/training/postivePredictions/"
if os.path.exists(destDir):
	shutil.rmtree(destDir)
os.makedirs(destDir)

source = "DataSet/training/predictedFiles/"

filePath = "DataSet/training/predictedFiles/predictedLabels.txt"
for line in open(filePath,'r').readlines():
	[filename,label] = line.split()
	impath = source+filename+".jpg"
	print "NEHA PATH",impath
	if os.path.isfile(impath):
		print "label",label
		if str(label) == "1":
			shutil.move(impath,destDir+filename+".jpg")