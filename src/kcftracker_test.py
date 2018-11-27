import cv2
# import rect
import my_rect
import mat
import numpy as np
import kcftracker

print("Creating some objects:")

image = cv2.imread("tt.jpg")
# cv2.imshow('image', image)
# cv2.waitKey();
image = np.array(image)

umat = cv2.UMat(image)


fname = '1.jpg'
img = cv2.imread(fname)
image = mat.Mat.from_array(img)
# cv2.imshow('image', image)
# cv2.waitKey();
print("////////cv::Point moved//////////////")
a = my_rect.CVrect(31.1,67,662,137)
# aa = rect.receive_Rect2f(a)

print("//////////////////////rect:")
print(a)
# print("//////////////////////mat:")
# # print(image)
# print("//////////////////////umat:")


c = kcftracker.KCFTracker()
c.init(a, image)
c.update(image)

print("Creating some objects:")

if __name__=="__main__":
	print("hello")