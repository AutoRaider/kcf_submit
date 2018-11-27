import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import cv2

image_path = '/home/iotg-demo/GPU_KCF/test_data/traffic/*.jpg'
coll = io.ImageCollection(image_path)
# print(len(coll))
# bgr = coll[0][...,::-1]
groundtruth_path = '/home/iotg-demo/GPU_KCF/test_data/traffic/groundtruth.txt'

# cv2.imshow('image', bgr)
# cv2.waitKey();
# io.imshow(coll[0])
# plt.show()

# groundtruth = np.loadtxt('/home/iotg-demo/GPU_KCF/test_data/traffic/groundtruth.txt')
file = open(groundtruth_path,"r")
list_arr = file.readlines()
l = len(list_arr)
for i in range(l): 
	list_arr[i] = list_arr[i].strip()
	list_arr[i] = list_arr[i].split(",")
groundtruth = np.array(list_arr)
groundtruth = groundtruth.astype(float)
file.close()
print(groundtruth[0,2])
print(min(10,30))

if __name__=="__main__":
	print("hello")
