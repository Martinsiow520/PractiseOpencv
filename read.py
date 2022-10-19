import cv2 as cv

#img = cv.imread('Resources/Photos/cat.jpg')

#cv.imshow('Dog',img)
#cv.waitKey(0)

capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
	isTrue, frame = capture.read()
	cv.imshow('Video', frame)

	if cv.waitKey(10) & 0xFF == ord('q'):
		break

capture.release()
cv.destroyAllWindows()
