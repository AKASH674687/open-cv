import cv2 as cv

img = cv.imread("images/bmw.jpg")

cv.imshow("image", img)

cv.waitKey(0)