#This file contains the code to modify the aspect ratio of an image and save it destination folder

import cv2

import os
import numpy as np
import fnmatch
import shutil
import math

def aspectRatioTransform(path,dpath):
	if os.path.exists(dpath):
		shutil.rmtree(dpath)
	os.makedirs(dpath)

	print dpath
	size = 200
	for filename in os.listdir(path):
		if fnmatch.fnmatch(filename, '*.jpg') or fnmatch.fnmatch(filename, '*.png'):
			image = cv2.imread(path + filename,0)
			[height,width] = image.shape
			narray = (np.arange(140,370,5)).tolist()
			#fix width 
			i = 0
			for nwidth in narray:
				aspect_ratio = nwidth/width
				newHeight = int((aspect_ratio+0.5)*height)
				dim = (nwidth, newHeight)
				# perform the actual resizing of the image and show it
				resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
				left = 0
				top = 0
				if nwidth < size :
					left = size-nwidth
					if newHeight <= size:
						top = size - newHeight
					finalImage=cv2.copyMakeBorder(resized, top=top, bottom=0, left= left, right=0, borderType= cv2.BORDER_CONSTANT, value=[255,255,255] )
					if newHeight > size:
						hdiff = int((newHeight-size)/2)
						finalImage = finalImage[hdiff:finalImage.shape[0]-hdiff, 0:finalImage.shape[1]]
				elif nwidth > size:
					wdiff =  nwidth - size
					hdiff = 0
					if newHeight  > size:
						hdiff = newHeight - size
					[cwidth,cheight]= [int(wdiff/2),int(hdiff/2)]
					finalImage = resized[cheight:resized.shape[0]-cheight, cwidth:resized.shape[1]-cwidth]
					#print " Cropped finalImage width and height",finalImage.shape[0],finalImage.shape[1]
				cv2.imwrite(dpath+"aspectRatio"+str(i)+filename, finalImage)
				i = i+1
			i = 0
			for nheight in narray:
				aspect_ratio = nheight/height
				newWidth = int((aspect_ratio+1.5)*width)
				dim = (newWidth, nheight)
				# perform the actual resizing of the image and show it
				resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
				left = 0
				top = 0
				if nheight < size :
					top = size-nheight
					if newWidth < size:
						left = size - newWidth
					finalImage=cv2.copyMakeBorder(resized, top=top, bottom=0, left= left, right=0, borderType= cv2.BORDER_CONSTANT, value=[0,0,0] )
					if newWidth > size:
						wdiff = int((newWidth-size)/2)
						finalImage = finalImage[0:finalImage.shape[0], wdiff:finalImage.shape[1]-wdiff]
						#print " Height Padded/cropped finalImage width and height",finalImage.shape[0],finalImage.shape[1]
				elif nheight > size:
					hdiff =  nheight - size
					wdiff = 0
					if newWidth  > size:
						wdiff = newWidth - size
					[cwidth,cheight]= [int(wdiff/2),int(hdiff/2)]
					finalImage = resized[cheight:resized.shape[0]-cheight, cwidth:resized.shape[1]-cwidth]
				cv2.imwrite(dpath+"aspectRatio"+ str(i)+filename, finalImage)
				i = i+1
					
	



			
			