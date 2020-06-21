
from imutils.video import VideoStream
from imutils import face_utils
import datetime
import argparse
import imutils
import time
import dlib
import cv2
import math
import csv
import numpy
import pandas as pd
import matplotlib.pyplot as plt

# ap = argparse.ArgumentParser()
# ap.add_argument("-p", "--shape-predictor", required=True,
# 	help="path to facial landmark predictor")
# ap.add_argument("-r", "--picamera", type=int, default=-1,
# 	help="whether or not the Raspberry Pi camera should be used")
# args = vars(ap.parse_args())
def video_analysis(path,file):

	detector = dlib.get_frontal_face_detector()
	predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


	#print("[INFO] camera sensor warming up...")
	#vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
	print("Loading File")
	time.sleep(2.0)
	path="D://mpstme//SEM 7//PROJECT//"
	#file="asdfghj"
	file=file.split('.')[0]
	vs=cv2.VideoCapture((path+file+".avi"),cv2.CAP_FFMPEG)
	fc=int(vs.get(cv2.CAP_PROP_FRAME_COUNT))
	jr=[]
	jl=[]
	n1=[]
	n2=[]
	nd=[]
	njr=[]
	njl=[]
	eyel=[]
	eyer=[]
	ctr=0
	fc=fc-1
	print("Detecting Features")
	while ctr<fc:
		#print(ctr)
		ctr=ctr+1
		ret,frame = vs.read()
		if type(frame)==numpy.ndarray:
			frame =imutils.resize(frame, width=400)
			'''if(size.height>0):
				cv2.imshow("Frame", frame)'''
			#print(type(frame))
			
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


			
			rects = detector(gray, 0)
			#print(rects)

			
			for rect in rects:
				
				shape = predictor(gray, rect)
				#print(shape)
				#print("\n")
				shape = face_utils.shape_to_np(shape)
				#print(len(shape))
		#
				i=0
				eyel.append(((shape[40][1]+shape[41][1])/2)-((shape[37][1]+shape[38][1])/2))
				eyer.append(((shape[46][1]+shape[47][1])/2)-((shape[43][1]+shape[44][1])/2))
				for (x, y) in shape:
		                        i=i+1
		                        if (i in range(1,18) or i in range(28,32) or i==34):
		                                cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)
		                        
		                        if(i == 28):
		                                jr.append([x,y])
		                                cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)

		                        if(i == 31):
		                                jl.append([x,y])
		                                cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)

		                        if(i == 7):
		                                n1.append([x,y])
		                                cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)

		                        if(i == 11):
		                                n2.append([x,y])
		                                cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)

		                                
			  
			
			#cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF
	 
		
		if key == ord("q"):
			break


	cv2.destroyAllWindows()
	#vs.stop()
	#print(eyel)
	print("Calculating values")
	for i in range(len(jr)):
	        nd.append([abs(n2[i][0]-n1[i][0]),abs(n2[i][1]-n1[i][1])])
	        njl.append(math.sqrt((nd[i][0]-jl[i][0])^2+(nd[i][1]-jl[i][1])^2))
	        njr.append(math.sqrt((nd[i][0]-jr[i][0])^2+(nd[i][1]-jr[i][1])^2))
	        #print(njr[i])

	data=[njl,njr]
	print(data)
	
	#plt.set_title('Left and Right Jaw Movement')
	plt.boxplot(data)

	
	plt.savefig(file+'_bplt.png')#r"\\static\\images\\"+
	#plt.show()
	print("writing csv")
	with open((file+".csv"), 'w', newline='') as csvfile:
	    outputwriter = csv.writer(csvfile, delimiter=',')
	    outputwriter.writerow(["NO","Nx","Ny","JRx","JRy","JLx","JLy","NJR","NJL","EyeL","EyeR"])
	    for i in range(len(jr)):
	        outputwriter.writerow([i,nd[i][0],nd[i][1],jr[i][0],jr[i][1],jl[i][0],jl[i][1],njr[i],njl[i],eyel[i],eyer[i]])
	        #print("sdaf")



#video_analysis()