import cv2
import os
import numpy as np
import fnmatch
from random import randint
import os.path
import glob
import shutil
from shutil import copyfile
from extractImage import extractImage
from generateLable import generateLabel


testImagePath = "DataSet/test/UFDD/testdata/"
testLabelFile = "DataSet/test/UFDD/testdata/genLabel.txt"

generateLabel(testImagePath,None,testLabelFile,"negative")

