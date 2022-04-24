from logging import exception
from traceback import print_tb
import cv2 as cv
import numpy as np
import time

# print(cv.__file__)  # just to see the location of data folder
face_cascade = cv.CascadeClassifier('data/haarcascade_frontalface_alt.xml')
recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

cap = cv.VideoCapture(0)


while True:
    sucess, img = cap.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    # below x, y, w, h are the values of the rectangle surrounding the face
    try:
        for (x, y, w, h) in face:
            # print(x, y, w, h)

            cv.rectangle(img, (x,y), (x+w, y+h), (244, 232, 23), 2)

            roi_gray = gray[y:y+h , x:x+w]  # cropping a certain part of image
            roi_color = img[y:y+h , x:x+w]

            id_, conf = recognizer.predict(roi_gray)
            if conf>= 45 and conf <= 85:
                print(id_)

            img_written = "face3.png"
            img_written2 = "face4.png"
            cv.imwrite(img_written2, roi_color)
            cv.imwrite(img_written, roi_gray)

    except:
        continue

    # now we have to use a pre trained model to recognize the face


    cv.imshow("Video", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break



cap.release()
cv.destroyAllWindows()