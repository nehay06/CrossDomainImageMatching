import cv2

def resizeIm(image,size,setwidth):
	r = float(size) / image.shape[1]
	if setwidth == 'true':
		dim = (size, int(image.shape[0] * r))
	else:
		dim = (int(image.shape[1] * r),size)
	# perform the actual resizing of the image and show it
	resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
	if dim[1] < size:
		bordersize = size-dim[1]
		paddedImage=cv2.copyMakeBorder(resized, top=bordersize, bottom=0, left=0, right=0, borderType= cv2.BORDER_CONSTANT, value=[0,0,0] )
	else:
		paddedImage = resized[0:size,0:size]
	
	return paddedImage