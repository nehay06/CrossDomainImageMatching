# USAGE
#This file contains code to comapre the Query Image with the Images classified as positive by the Classifier. 
# Method also generates a text file that contains the file name and reported score

# import the necessary packages
from skimage.measure import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
from skimage.io import imread
from resizeImage import resizeIm
import glob
import os
import fnmatch

QueryImageDir = "DataSet/training/QueryImage/"
#Specify the query Image. This needs to changed as per requirement. 
for filename in os.listdir(QueryImageDir):
	filepath = QueryImageDir+filename
	if os.path.isfile(filepath):
		queryImage = filepath

#Flag to display the result on a plot. Set this Flag to true if visualiztion is required.
is_display = False


#Directory where generatedScores will be saved in a text file
sourceDir = "DataSet/test/predictedFiles/"
#Generated Score File
genScoreFile = "DataSet/test/predictedFiles/genScores.txt"

def compare_images(queryImage, predictedImage, title,predictedImageFileName):
	# compute the mean squared error and structural similarity
	# index for the images
	s = ssim(queryImage, predictedImage)
	genData = ''.join([str(predictedImageFileName), ' ', str(float("{0:.2f}".format(s))), "\n"])
	if not os.path.isfile(genScoreFile):
		file = open(genScoreFile, "w") 
	else:
		file = open(genScoreFile, "a")
	print "Scores",genData
	file.write( genData  )
	file.close()

	# setup the figure
	if is_display == True:
		fig = plt.figure(title)
		plt.suptitle("SSIM: %.2f" % (s))

		# show first image
		ax = fig.add_subplot(1, 2, 1)
		plt.imshow(queryImage, cmap = plt.cm.gray)
		plt.axis("off")

		# show the second image
		ax = fig.add_subplot(1, 2, 2)
		plt.imshow(predictedImage, cmap = plt.cm.gray)
		plt.axis("off")

		# show the images
		plt.show()

# load the images

original = imread(queryImage,as_grey=True)
queryImage = resizeIm(original,200,'true')

# compare the images
for filename in os.listdir(sourceDir):
	if fnmatch.fnmatch(filename, '*.jpg') or fnmatch.fnmatch(filename, '*.png'):
		filepath = sourceDir+filename
		predicted = imread(filepath,as_grey=True)
		predictedImage = resizeIm(predicted,200,'true')
		compare_images(queryImage, predictedImage, "queryImage vs. predictedImage",filename.split(".")[0])


