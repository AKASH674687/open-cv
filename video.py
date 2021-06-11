import cv2 as cv
cap = cv.VideoCapture("images/myvideo.mp4")

while cap.isOpened():
    ret,frame = cap.read()
    cv.imshow("webcam",frame)
    if not ret:
        print("video format is not supported")
        break
    #cv.waitKey(1)
    if cv.waitKey(1) == ord("z"):
        break