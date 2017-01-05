#This methods generates the feature descriptor of the given images

import cv2
from resizeImage import resizeIm
from skimage.feature import hog
from skimage.io import imread
from sklearn.externals import joblib
from cropImage import cropImage
import numpy as np
import glob
import os
import shutil

def extractFeature(im_path,featureType,featureDir,is_file):
	
	# If feature directories don't exist, create them

	if featureDir is not None:
		if not os.path.isdir(featureDir):
			print "neha Rocks"
			os.makedirs(featureDir)

	orientations = 9
	cells_per_block =[3, 3]
	visualize =True
	normalize = True

	# Calculate Descriptor for all images in a directory.
	if is_file is False:
		print "Calculating the descriptors for the"+featureType+ "samples and saving them"
		for im_path in glob.glob(os.path.join(im_path, "*")):
			im = imread(im_path, as_grey=True)
			print "Current Image Size",im.shape
			image = resizeIm(im,200,'true')
			px = 20
			py = 20
			[fd,hog_image] = hog(image, orientations, [px,py], cells_per_block, visualize, normalize)
			if featureDir is not None:
				fd_name = os.path.split(im_path)[1].split(".")[0] + ".feat"
				joblib.dump(fd,os.path.join(featureDir, fd_name))
				print featureType +"Features saved in {}".format(featureDir)
	
	#Calculate feature descriptor for a single file.
	elif is_file is True:
		im = imread(im_path, as_grey=True)
		negImage = resizeIm(im,200,'true')
		px = 20
		py = 20
		[fd,hog_image] = hog(negImage, orientations, [px,py], cells_per_block, visualize, normalize)
		if featureDir is not None:
			fd_name = os.path.split(im_path)[1].split(".")[0] + ".feat"
			joblib.dump(fd,os.path.join(featureDir, fd_name))
			print featureType +"Features saved in {}".format(featureDir)
		return fd

