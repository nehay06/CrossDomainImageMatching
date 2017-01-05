#this method contains code to move or copy files form one folder to another
#from_file- reads the file name for a file and copies/moves form source to destination folder
#random - it movies or copies files in a random order from source to destination. Filenums contains the random numbers genrated and to be moves
#fixed- it simply moves from source to destination

import cv2
import os
import shutil
import fnmatch
import shutil
from random import randint
from shutil import copyfile

def extractImage(file_path,source,destDir,method,extractType):

	if not os.path.exists(destDir):
		os.makedirs(destDir)

	if not os.path.exists(destDir):
		os.makedirs(destDir)
		
	# to read the filename from a file and move or copy images
	if method =="from_file":
		for line in open(file_path,'r').readlines():
			[filename,classifier] = line.split()
			if (str(classifier) == '1'):
				print line
				category = (os.path.split(file_path)[1][:-4])
				ind = category.find('_')
				#filePath = source+'/'+filename+".jpg"
				dPath = destDir+'/'+category[0:ind]
				#dfilePath = cPath+'/'+filename+".jpg"
				if not os.path.exists(dPath):
					os.makedirs(dPath)
				if extractType == "copy":
					copyfile(source+'/'+filename+".jpg", dPath+'/'+filename+".jpg")
				if extractType == "move":
					shutil.move(source+'/'+filename+".jpg", dPath+'/'+filename+".jpg")

	#move some random files from source to destination this method assumes files are named properly. Pascal voc and random flicker images			
	if method == "random":
		FilesCount = len([name for name in os.listdir(source) if os.path.isfile(os.path.join(source, name))])
		randomFilesNum = 100
		FilesNum=[randint(0,FilesCount) for p in range(0,randomFilesNum)]
		filenameLen = 6
		for filenum in FilesNum:
			length = len(str(filenum))
			string_val = "".join('0' for i in range(filenameLen-length))
			filepath  = source+'/'+str(string_val)+str(filenum)+".jpg"
			filename = str(string_val)+str(filenum)+".jpg"
			if os.path.isfile(filepath): 
				if extractType == "move":
					shutil.move(filepath,destDir+filename)
				if extractType == "copy":
					copyfile(filepath,destDir+filename)

	#move or copy all files from one folder to another
	if method == "fixed":
		for filename in os.listdir(source):
			if fnmatch.fnmatch(filename, '*.jpg') or fnmatch.fnmatch(filename, '*.png'):
				filepath = source+filename
				print filename
				if os.path.isfile(filepath): 
					if extractType == "move":
						shutil.move(filepath,destDir+filename)
					if extractType == "copy":
						copyfile(filepath,destDir+filename)


