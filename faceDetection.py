
import cv2 as cv
import mediapipe as mp
import numpy as np
import face_recognition as fr


myImg = fr.load_image_file('face.jpg')
myImg = cv.cvtColor(myImg, cv.COLOR_BGR2RGB)
myImg2 = fr.load_image_file('face2.jpg')
myImg2 = cv.cvtColor(myImg2, cv.COLOR_BGR2RGB)

# step 2 - finding the faces, and finding their encodings as well

faceLoc = fr.face_locations(myImg)[0]  # getting the first element, since we only have one image
encodings = fr.face_encodings(myImg)[0]  # similarly getting the first element here as well

# we draw a rectangle just to see that where do we have detected the face
cv.rectangle(myImg, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]),(255, 0, 255), 3 )


face2Loc = fr.face_locations(myImg2)[0]
f2encodings = fr.face_encodings(myImg2)[0]

cv.rectangle(myImg2, (face2Loc[3], face2Loc[0]), (face2Loc[1], face2Loc[2]),(255, 0, 255), 3 )

# Step 3 - comparing the faces and finding the spaces between them

results = fr.compare_faces([encodings], f2encodings)
faceDist = fr.face_distance([encodings], f2encodings)
print(faceDist)  # the lower the value of faceDist, similar the faces
print(results)
# if the results is true so it means both the faces are similar. i.e. the encodings are of same face
cv.putText(myImg2, f'{results} {round(faceDist[0], 2)}', (50, 50), cv.FONT_ITALIC, 1, (0, 0, 255), 2)

cv.imshow("My face", myImg)
cv.imshow("My face 2", myImg2)
cv.waitKey(0)

