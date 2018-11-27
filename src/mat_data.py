import cv2
from PIL import Image, ExifTags

cvimage = cv2.imread('1.jpg')
image = Image.fromarray(cvimage)