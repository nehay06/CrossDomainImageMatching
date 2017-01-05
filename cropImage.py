#This methods crops the image and pads the difference to have image size of 200*200
# It also rescales the image up and then crops the image
#All the cropped+padded/Rescaled+Croped images are saved in the destination folder

import sys

sys.path.append('/Users/nehayadav/.virtualenvs/cv/lib/python2.7/site-packages')

import cv2

import os
import numpy as np
import fnmatch
import shutil
import math
from resizeImage import resizeIm


def cropImage(path,dpath):

# load the image and show it
	if os.path.exists(dpath):
		shutil.rmtree(dpath)
	os.makedirs(dpath)

	print dpath
	size = 200

	for filename in os.listdir(path):
		if fnmatch.fnmatch(filename, '*.jpg') or fnmatch.fnmatch(filename, '*.png'):
			image = cv2.imread(path + filename,0)
			print filename
			[height,width] = image.shape

			narray = (np.arange(10,60,5)).tolist()
			print narray
			i = 0

			for param in narray:
				temp = " "
				croppedImage = image[param:width-param, param:height-param]	
				paddedImage=cv2.copyMakeBorder(croppedImage, top=param, bottom=param, left=param, right=param, borderType= cv2.BORDER_CONSTANT, value=[255,255,255] )
				temp = "scaledncropped"+str(i)+filename
				cv2.imwrite(dpath+temp, paddedImage)
				i = i+1
			i = 0
			narray = (np.arange(200,310,10)).tolist()
			for param in narray:
				temp = " "
				resizedImage= resizeIm(image,param,'true')
				[rheight,rwidth] = resizedImage.shape
				diff = int((param-size)/2)
				croppedImage = resizedImage[diff:rwidth-diff, diff:rheight-diff]	
				temp  = "scaledncropped"+str(i)+filename
				cv2.imwrite(dpath+temp, croppedImage)
				i = i+1

