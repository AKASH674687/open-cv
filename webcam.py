import cv2 as cv
cap = cv.VideoCapture(0)
while True:
    ret,frame = cap.read(0)
    cv.imshow("webcam is",frame)
    if not ret:
        print("camera is not responding")
        break
    #cv.waitKey(1)
    if cv.waitKey(1) == ord("c"):
        break