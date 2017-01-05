import cv2
from extractFeatures import extractFeature
from aspectRatio import aspectRatioTransform
from cropImage import cropImage
from extractImage import extractImage
from transformations import imagetransform

def performTransformation(method,source,destination):

	print "Performin"
	if method == "translate":
		print "Performing Translations"
		imagetransform(source,destination)
	elif method == "cropImage":
		#test Crop image 
		print "Perform Crop Transformations"
		cropImage(source,destination)
	elif method =="aspectRatio":
		#testaspectRation
		print "Perform Aspect Ratio"
		aspectRatioTransform(source,destination)
