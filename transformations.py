import cv2
import os
import fnmatch
import shutil
import random
import numpy as np


def imagetransform(path,cpath):

	# load the image and show it
	if os.path.exists(cpath):
		shutil.rmtree(cpath)
	os.makedirs(cpath)

	print cpath

	for filename in os.listdir(path):
		if fnmatch.fnmatch(filename, '*.jpg') or fnmatch.fnmatch(filename, '*.png'):
			image = cv2.imread(path + filename,0)
			k = 1
			j = -1
			for i in range(20):
				num1 = k * random.uniform(0,50)
				num2 = j *random.uniform(0,100)
				M = np.float32([[1, 0, num1], [0, 1, num2]])
				translated = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
				dpath = cpath+'translate_'+str(i)+'.jpg'
				cv2.imwrite(dpath, translated )
				k = k*-1
				j = j*-1

