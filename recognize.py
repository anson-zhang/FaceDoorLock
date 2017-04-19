import os
import cv2
import numpy as np
from PIL import Image
import time

#Define face cascade
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#Set video
video_capture = cv2.VideoCapture(0)
video_capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,640)
video_capture.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT,480)
dic = dict()
for l in open("./Faces/face_label.txt"):
	dic[l.split(" ")[0]] = l.split(" ")[1].strip("\n")

t_start = time.time()
fps = 0

while True:
	ret, frame = video_capture.read()
	#fps = fps + 1
	#sfps = fps / (time.time() - t_start)
	#cv2.putText(frame, "FPS : " + str(sfps), (0, 480), cv2.FONT_HERSHEY_SIMPLEX, 1, ( 0, 255, 0 ))
	cv2.imshow("Face Door Lock", frame)
	if cv2.waitKey(5) & 0xFF == ord('t'):
		#Defind face recognizer: LBPH
		recognizer = cv2.createLBPHFaceRecognizer()
		recognizer.load("fdl.xml")
		image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		col_img = frame
		faces = faceCascade.detectMultiScale(image, 1.2)
		for (x, y, w, h) in faces:
			label_predict, conf = recognizer.predict(image[y: y + h, x: x + w])
			if conf < 70.0:
				cv2.rectangle(col_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
				cv2.rectangle(col_img, (0,420), (640,460), (255, 255, 255), -1)
				cv2.putText(col_img, "Welcome " + str(dic[str(label_predict)]) + "!", (0, 450), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0 ,0))
				#cv2.putText(col_img, "Open for " + str(dic[str(label_predict)]) + " " + str(conf), (x, y + h), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255 ,0))
				cv2.imwrite("./visitors/" + dic[str(label_predict)] + str(time.strftime("-%Y-%m-%d-%H_%M_%S", time.localtime())) + ".jpg", col_img)
				cv2.imshow("Face Door Lock", col_img)
				cv2.waitKey(5000)
			else:
				if conf < 200.0:
					cv2.rectangle(col_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
					cv2.rectangle(col_img, (0,420), (640,460), (255, 255, 255), -1)
					cv2.putText(col_img, "Sorry! You are not allowed to come in.", (0, 450), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0))
					#cv2.putText(col_img, "unknown " + str(dic[str(label_predict)]) + str(conf), (x, y + h), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255 ,0))
					cv2.imwrite("./visitors/" + "unknown" + str(time.strftime("-%Y-%m-%d-%H_%M_%S", time.localtime())) + ".jpg", col_img)
					cv2.imshow("Face Door Lock", col_img)
					cv2.waitKey(5000)
	if cv2.waitKey(5) & 0xFF == ord('q'):
		break

video_capture.release()
cv2.destroyAllWindows()
