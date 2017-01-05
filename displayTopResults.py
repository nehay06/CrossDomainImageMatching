# USAGE
# Given the generated scores for the images. This file contains code to sort the images files in descending order of their scores
#and generate a new file that contains the imagename and scores.
#This will be useful in predicting the top scores

# import the necessary packages
import matplotlib.pyplot as plt
import numpy as np
import cv2
from skimage.io import imread
from resizeImage import resizeIm
import glob
import os
import fnmatch

#source directory which contains the image predicted by classifier
sourceDir = "DataSet/test/predictedFiles/"

#File name which contains the  generated scores for each image file
genScoreFile = "DataSet/test/predictedFiles/genScores.txt"

#File to contain the Sorted scores of each file
sortedScoresFile = "DataSet/test/predictedFiles/genScoreSorted.txt"

scoreArray = []
for line in open(genScoreFile,'r').readlines():
	temp = (line.split()[0],line.split()[1])
	scoreArray.append(temp)
	sorted_lines = sorted(scoreArray, key = lambda x : x[1],reverse=True )
	
for line in sorted_lines:
	genData = ''.join([line[0]," ", line[1],"\n"])
	if not os.path.isfile(sortedScoresFile):
		file = open(sortedScoresFile, "w") 
		print "FileText",genData
	else:
		file = open(sortedScoresFile, "a")
		print "FileText",genData
	file.write( genData  )
	file.close()
