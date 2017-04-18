import os
import cv2
import numpy as np
from PIL import Image

#Define face cascade
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#Defind face recognizer: LBPH
recognizer = cv2.createLBPHFaceRecognizer()

def train_data(path):
	file = open("./Faces/face_label.txt", "w")
	dic = dict();
	data_paths = [os.path.join(path, f) for f in os.listdir(path)]
	datas = []
	labels = []
	for data_path in data_paths:
		img = Image.open(data_path).resize((640, 480), Image.ANTIALIAS)
		img.save(data_path);
		data = np.array(img.convert('L'))
		name = str(os.path.split(data_path)[1].split(".")[0].split("-")[0])
		label = int(os.path.split(data_path)[1].split(".")[0].split("-")[1].split("_")[0])
		dic[label] = name
		face = faceCascade.detectMultiScale(data, 1.2)
		for (x, y, w, h) in face:
			datas.append(data[y: y + h, x: x + w])
			labels.append(label)
			img.crop((x, y, x + w, y + h)).save("./Faces/" + os.path.split(data_path)[1])
	recognizer.train(datas, np.array(labels))
	recognizer.save("fdl.xml")
	for obj in dic.keys():
		file.write(str(obj) + " " + dic[obj] + "\n")
	file.close()

train_data("./FaceKeys");