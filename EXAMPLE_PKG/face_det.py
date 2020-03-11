import cv2

def face_detect(imgPath, cascPath=None):
	
	if cascPath==None:
		print('No cascadades.. No cool')
		return

	faceCascade = cv2.CascadeClassifier(cascPath)

	image = cv2.imread(imgPath,0)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	faces = faceCascade.detectMultiScale(
	    gray,
	    scaleFactor=1.1,
	    minNeighbors=5,
	    minSize=(30, 30)
	)


	return image, faces

def draw_squares(image, faces):
	for (x, y, w, h) in faces:
	    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
	return image
