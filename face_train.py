import os
from tkinter import Label
import cv2 as cv
from PIL import Image
from numpy import uint8
import numpy as np
import pickle

# os.path.abspath(__file__) gives us the adress of face_train file
# we could have directly pasted the adress here, but the path file is not the same for all the system
# but from this method we will always get the absolute path of the file, regardless of the system
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images")

face_cascade = cv.CascadeClassifier('data/haarcascade_frontalface_alt.xml')
recognizer = cv.face.LBPHFaceRecognizer_create()

currentID = 0
label_ids = {}
y_labels = []
x_train = []

for root, dir, files in os.walk(image_dir):
    for file in files:
        if file.endswith('.jpg') or file.endswith('.png'):
            path = os.path.join(root, file)
            label = os.path.basename(os.path.dirname(path)).replace(" ", "-").lower()
            # print(label, path)
            pil_image = Image.open(path).convert("L")  # converts image to grayscale
            image_array = np.array(pil_image, uint8)  # converting grayscaled image to numpy array
            # print(image_array)  # we just converted image to numbers, with the help of numpy

            if not label in label_ids:
                label_ids[label] = currentID
                currentID +=1

            id_ = label_ids[label]
            print(label_ids)
            
            
            faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)

            for (x,y,w,h) in faces:
                roi = image_array[y:y+h, x:x+w]  # from y to y+h,  x to x+w
                x_train.append(roi)
                y_labels.append(id_)

# print(y_labels)  # y_labels is a list of ids 
# print(x_train)  # x_train is a label of region of interest

# using pickle to save lable ids
with open("labels.pkl", 'wb') as file:
    pickle.dump(label_ids, file)

# now we have to train the openCV recognizer 
recognizer.train(x_train, np.array(y_labels))
recognizer.save("trainer.yml")

# now all we have to do is implement this recognizer

