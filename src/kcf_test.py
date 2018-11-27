import my_rect
import mat
import numpy as np
import kcftracker
import matplotlib.pyplot as plt
import skimage.io as io
import os

origin = os.path.abspath(os.path.dirname(os.getcwd()))
image_path = origin + '/test_data/traffic/*.jpg'
groundtruth_path = origin + '/test_data/traffic/groundtruth.txt'

def GetInput():
	image_rgb = io.ImageCollection(image_path)
	image_cv = []
	for i in range( len(image_rgb) ):
		image_cv.append(image_rgb[i][...,::-1])
	return image_cv

def GetRoi(num):
	file = open(groundtruth_path,"r")
	list_arr = file.readlines()
	for i in range( len(list_arr) ):
		list_arr[i] = list_arr[i].strip()
		list_arr[i] = list_arr[i].split(",")
	groundtruth = np.array(list_arr)
	groundtruth = groundtruth.astype(float)
	file.close()
	# num = 0
	xMin = min(groundtruth[num,0], min(groundtruth[num,2], 
			min(groundtruth[num,4], groundtruth[num,6])))
	yMin = min(groundtruth[num,1], min(groundtruth[num,3], 
			min(groundtruth[num,5], groundtruth[num,7])))
	width = max(groundtruth[num,0], max(groundtruth[num,2], 
			max(groundtruth[num,4], groundtruth[num,6]))) - xMin
	height = max(groundtruth[num,1], max(groundtruth[num,3], 
			max(groundtruth[num,5], groundtruth[num,7]))) - yMin
	rect_result = my_rect.CVrect(xMin,yMin,width,height)
	return rect_result

if __name__=="__main__":

	img = GetInput()
	tracking = kcftracker.KCFTracker()
	if len(img) != 0:
		orig_image = mat.Mat.from_array(img[0])
		roi = GetRoi(0)
		tracking.init(roi, orig_image)
		for i in range( 1, len(img) ):
			orig_image = mat.Mat.from_array(img[i])
			tracking.update(orig_image)




