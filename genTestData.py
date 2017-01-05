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
from generateLable import generateLabel


className = "21"
dataSet = "ufdd"
sourceDir = "DataSet/training/"
testDir = "DataSet/test/testdata/"
addRandomNegatives = True
testLabelDir = "DataSet/test/testLabels/"
testLabelFile = "DataSet/test/testLabels/genLabel.txt"

if os.path.exists(testDir):
	shutil.rmtree(testDir)
os.makedirs(testDir)

if os.path.exists(testLabelDir):
	shutil.rmtree(testLabelDir)
os.makedirs(testLabelDir)

if dataSet == "ufdd":
	sourceDir = "DataSet/training/"
	sourceImagePath =sourceDir+"ufdd/classe"+className+"/"
	extractImage(None,sourceImagePath,testDir,"fixed","copy")

if dataSet =="ufdd":
	sourceDir = "DataSet/test/UFDD/"
	extractImage(None,sourceDir+"painting/",testDir,"fixed","copy")
	extractImage(None,sourceDir+"photo/",testDir,"fixed","copy")
	extractImage(None,sourceDir+"sketch/",testDir,"fixed","copy")
	generateLabel(testDir,className,testLabelFile,dataSet)

if dataSet == "sketchy":
	sourceDir = "DataSet/test/"
	negatives = ["bicycle","cow","airplane","motorcycle","helicopter","wine_bottle"]
	sourceImagePath = sourceDir+"sketchy/"+className+"/"
	extractImage(None,sourceImagePath,testDir,"fixed","copy")
	generateLabel(testDir,className,testLabelFile,dataSet)
	for className in negatives:
		negImagePath = sourceDir+"sketchy/"+className+"/"
		extractImage(None,sourceImagePath,testDir,"fixed","copy")
		generateLabel(testDir,className,testLabelFile,"negative")

if addRandomNegatives == True:
	sourceDir = "DataSet/test/"
	#copy images from Pascal VOC
	sourceImagePath = sourceDir+"VOCdevkit/JPEGImages/"
	extractImage(None,sourceImagePath,testDir,"random","copy")
	generateLabel(testDir,None,testLabelFile,"negative")
	#copy images form flickr
	sourceDir = "DataSet/test/negativeImages"
	extractImage(None,sourceDir,testDir,"random","copy")
	generateLabel(testDir,None,testLabelFile,"negative")
	#copy Images from INRIAHolidays
	sourceDir = "DataSet/training/INRIA"
	extractImage(None,sourceDir,testDir,"random","copy")
	generateLabel(testDir,None,testLabelFile,"negative")

