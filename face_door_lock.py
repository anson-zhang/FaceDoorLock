import os
import cv2
import numpy as np
from PIL import Image
import time

#Define face cascade
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

#Defind face recognizer: LBPH
recognizer = cv2.createLBPHFaceRecognizer()

def train_data(path):
	data_paths = [os.path.join(path, f) for f in os.listdir(path)]
	datas = []
	labels = []
	for data_path in data_paths:
		data = np.array(Image.open(data_path).convert('L'))
		label = int(os.path.split(data_path)[1].split(".")[0])
		face = faceCascade.detectMultiScale(data)
		for (x, y, w, h) in face:
			datas.append(data[y: y + h, x: x + w])
			labels.append(label)
	recognizer.train(datas, np.array(labels))

train_data('./FaceKeys');

#Set video
video_capture = cv2.VideoCapture(0)
#video_capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,1080)
#video_capture.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT,720)

t_start = time.time()
fps = 0
while True:
	ret, frame = video_capture.read()
	image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(image, 1.3)
	for (x, y, w, h) in faces:
		label_predict, conf = recognizer.predict(image[y: y + h, x: x + w])
		if conf < 5000.0:
			cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
			cv2.putText(frame, str(label_predict), (x, y), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255 ,0))
			cv2.putText(frame, str(conf), (x + w, y + h), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255 ,0))
	fps = fps + 1
	sfps = fps / (time.time() - t_start)
	cv2.putText( frame, "FPS : " + str( int( sfps ) ), ( 100, 100 ), cv2.FONT_HERSHEY_COMPLEX, 2, ( 0, 255, 0 ), 2 )

	cv2.imshow('Video', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

video_capture.release()
cv2.destroyAllWindows()


