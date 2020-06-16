
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
 

#ap = argparse.ArgumentParser()
#ap.add_argument("-p", "--shape-predictor",
#	help="path to facial landmark predictor")
#ap.add_argument("-r", "--picamera", type=int, default=-1,
#	help="whether or not the Raspberry Pi camera should be used")
#args = vars(ap.parse_args())

#detector = dlib.get_frontal_face_detector()
#predictor = dlib.shape_predictor(args["shape_predictor"])
#predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


print("[INFO] camera sensor warming up...")
vs = VideoStream().start()
time.sleep(2.0)

jr=[]
jl=[]
n1=[]
n2=[]
nd=[]
njr=[]
njl=[]
runner=input("Start?: ")

while runner=='Y' or runner=='y':

	while True:
		
		frame = vs.read()
		frame = imutils.resize(frame, width=400)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


		
		rects = detector(gray, 0)

		
		for rect in rects:
			
			shape = predictor(gray, rect)
			#print(shape)
			#print("\n")
			shape = face_utils.shape_to_np(shape)
			#print(len(shape))

			i=0
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
	                                
		  
		
		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF
	 
		
		if key == ord("q"):
			break


	cv2.destroyAllWindows()
	vs.stop()

	for i in range(len(jr)):
	        nd.append([abs(n2[i][0]-n1[i][0]),abs(n2[i][1]-n1[i][1])])
	        njl.append(math.sqrt((nd[i][0]-jl[i][0])^2+(nd[i][1]-jl[i][1])^2))
	       # print("math.sqrt(("+str(nd[i][0])+"-"+str(jl[i][0])+"^2+("+str(nd[i][1])+"-"+str(jl[i][1])+")^2)")
	        #print(math.sqrt((nd[i][0]-jl[i][0])^2+(nd[i][1]-jl[i][1])^2))
	        #njr.append(math.sqrt((nd[i][0]-jr[i][0])^2+(nd[i][1]-jr[i][1])^2))

	        njr.append(math.sqrt((nd[i][0]-jr[i][0])^2+(nd[i][1]-jr[i][1])^2))
	        #print(njr[i])



	with open('output2.csv', 'w', newline='') as csvfile:
	    outputwriter = csv.writer(csvfile, delimiter=',')
	    outputwriter.writerow(["NO","Nx","Ny","JRx","JRy","JLx","JLy","NJR","NJL"])
	    for i in range(len(jr)):
	        outputwriter.writerow([i,nd[i][0],nd[i][1],jr[i][0],jr[i][1],jl[i][0],jl[i][1],njr[i],njl[i]])

	runner=input("Run Again?: ")
 