#this method generates the lables for images

import cv2
import os
import fnmatch
import shutil
import random
import numpy as np


def generateLabel(source,className,filePath,dataset):

#filePath denotes the label file that would be generated
	if not os.path.isfile(filePath):
		file = open(filePath, "w") 
	else:
		file = open(filePath, "a")

	if dataset is not None and dataset == "ufdd":
		for filename in os.listdir(source):
			if fnmatch.fnmatch(filename, '*.jpg') or fnmatch.fnmatch(filename, '*.png'):
				nameContents = filename.split("_")[1][2:4]
				print "neha",nameContents
				if className == str(nameContents):
					stringData = filename.split(".")[0] + " " + "1" +"\n"
				else:
					stringData = filename.split(".")[0] + " " + "-1" +"\n"
				file.write( stringData  )
		file.close()
	#generate label for negative dataSet  Give 1 to all files sketcy data set. As this folder only contains the positive image.
	elif dataset == "sketchy":
		for filename in os.listdir(source):
			if fnmatch.fnmatch(filename, '*.jpg') or fnmatch.fnmatch(filename, '*.png'):
				print "neha",filename
				stringData = filename.split(".")[0] + " " + "1" +"\n"
				file.write( stringData  )

		file.close()
	elif dataset == "negative":
		for filename in os.listdir(source):
			if fnmatch.fnmatch(filename, '*.jpg') or fnmatch.fnmatch(filename, '*.png'):
				print "neha",filename
				stringData = filename.split(".")[0] + " " + "-1" +"\n"
				file.write( stringData  )

		file.close()

