import cv2

img = cv2.UMat(cv2.imread("tt.jpg", cv2.IMREAD_COLOR))
# imgUMat = cv2.UMat(img)
umat = cv2.UMat.get(img)
# gray = cv2.cvtColor(imgUMat)
# gray = cv2.GaussianBlur(gray, (7, 7), 1.5)
# gray = cv2.Canny(gray, 0, 50)
print(umat)
cv2.imshow("edges", umat)
cv2.waitKey();