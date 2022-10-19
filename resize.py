import cv2 as cv



def rescaleFrame(frame, scale=0.7):
	width = int(frame.shape[1]*scale)
	height = int(frame.shape[0]*scale)

	dimensions = (width, height)

	return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

def changeRes(width, height):
	capture.set(3,width)
	capture.set(4,height)
	
capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
	isTrue, frame = capture.read()

	imageresize=rescaleFrame(frame)

	cv.imshow('Video', frame)
	cv.imshow('Vedio_size', imageresize)

	if cv.waitKey(10) & 0xFF == ord('q'):
		break

capture.release()
cv.destroyAllWindows()