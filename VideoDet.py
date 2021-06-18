import cv2, time

from tkinter import *

window=Tk()	

def videoFaceDet():

	video = cv2.VideoCapture(0)
	
	faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        while True:
		
		check, frame = video.read()
		
		grayImg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		
		faces=faceCascade.detectMultiScale(grayImg, scaleFactor=1.05, minNeighbors=5)
		
		for x, y, w, h in faces:
			frame=cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
		
		cv2.imshow("Capturing", frame)

		key=cv2.waitKey(1)
		if key==ord('q'):
			break
	
	
	cv2.destroyAllWindows()
	
	video.release()


b1=Button(window, text="Start", command=videoFaceDet)
b1.grid(row=0, column=0)

l1=Label(window, text="Press Q to Stop Capturing")
l1.grid(row=0, column=1)


window.mainloop()
