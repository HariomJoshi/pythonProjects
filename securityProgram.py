import cv2 as cv
import face_recognition as fr
import mediapipe as mp
import numpy as np

cap = cv.VideoCapture(0)

def faceRecognition(user_image, img2):
    myImg = fr.load_image_file(user_image)  # user image
    myImg = cv.cvtColor(myImg, cv.COLOR_BGR2RGB)
    myImg2 = fr.load_image_file(img2)  # image to be checked
    myImg2 = cv.cvtColor(myImg2, cv.COLOR_BGR2RGB)

    # faceLoc = fr.face_locations(myImg)[0]  # getting the first element, since we only have one image
    encodings = fr.face_encodings(myImg)[0]  # similarly getting the first element here as well

    # face2Loc = fr.face_locations(myImg2)[0]
    f2encodings = fr.face_encodings(myImg2)[0]

    results = fr.compare_faces([encodings], f2encodings)
    faceDist = fr.face_distance([encodings], f2encodings)
    print(faceDist)  # the lower the value of faceDist, similar the faces
    print(results)



while True:
    sucess, img = cap.read()
    img2 = cv.imencode('.jpg', img)
    faceRecognition('face.jpg', img2)
    cv.imshow("video", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
