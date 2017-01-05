import os,errno
import shutil
from shutil import copyfile
import fnmatch

negativeTrainSet = "DataSet/training/negativeTrainSet/"
predictedLabelsFile = "DataSet/training/predictedFiles/predictedLabels.txt"

def silentremove(filename):
    try:
        os.remove(filename)
    except OSError as e: # this would be "except OSError, e:" before Python 2.6
        if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
            raise # re-raise exception if a different error occured

def removeEasyExamples(negativeTrainSet,predictedLabelsFile):
	for line in open(predictedLabelsFile,'r').readlines():
		[filename,classifier] = line.split()
		if (str(classifier) == '1'):
			print line
			filepath = negativeTrainSet+filename+".jpg"
			silentremove(filepath)
