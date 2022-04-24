import cv2 as cv
import time
import imutils

# cap = cv.VideoCapture('http://192.168.43.1:8080/video')
cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 80)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 100)

i = 1
while True:
    sucess, img = cap.read()
    # img = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
    img = imutils.resize(img, width=640, height=480)
    # if you want to click one photo every 10 milli second so simply add time.sleep(10) here
    time.sleep(0.1)
    
    cv.imwrite(f"images/hariom/{i}.png", img)
    i = i+1
    cv.imshow("Video", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
