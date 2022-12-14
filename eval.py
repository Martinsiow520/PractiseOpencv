import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['Ben Afflek', 'Elton John', 
		  'Jerry Seinfield', 'Madonna','Mindy Kiling']
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')
img = cv.imread(r'D:\Dp\OpenCV\Resources\Faces\val\elton_john\1.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

face_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y,w,h) in face_rect:
	faces_roi = gray[y:y+h, x:x+w]
	label, confidence = face_recognizer.predict(faces_roi)
	print(f'label={people[label]} and confidence = {confidence}')
	cv.putText(img, str(people[label]),(20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
	cv.rectangle(img, (x, y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('detected face', img)
cv.waitKey(0)