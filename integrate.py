print("importing Video_File")
import Video_File
print("importing AV_Split")
import AV_Split
print("importing AV2")
import AV2
print("importing os")
import os
print("importing noise_spect")
import noise_spect
print("importing mfccc_runer")
#import mfcc_runner
import numpy as np


def controller(f_name,r_len):
	print("entered integrate")
	ch=1#int(input("Select one of the following:\n1. Camera\n2. Preloaded file\n"))
	file_name=""
	path=os.getcwd()+"\\"
	if ch == 1:
		file_name=f_name#input("Enter File Name to be saved: ")
		length=r_len#int(input("Enter Recording Length: "))
		print("\n\ncaptureing video\n\n")
		fc=AV2.ctrl(file_name,length)
	#elif ch==2:
	#	file_name=input("Enter File Name: ")
	#	ch=int(input("Select one of the following:\n1. File in working directory\n2. File in different location\n"))
	#	if ch==2:
	#		path=input("Enter Path: ")
	#	AV_Split.split_av(path,file_name)
	print("\n\nvideo anallysis\n\n")
	Video_File.video_analysis(path,file_name)
	print("\n\naudio analysis\n\n")
	ims1=noise_spect.setname(file_name)
	#mfcc=mfcc_runner.mfcc_run(file_name)
	print("\n\ncalculating 92iau\n\n")
	ims2=noise_spect.setname("92-iau")
	ctr=0
	if(np.shape(ims1)[0]>np.shape(ims2)[0]):
		ims3=np.full_like(ims1,0)
		mcols=np.shape(ims2)[0]
	else:
		ims3=np.full_like(ims2,0)
		mcols=np.shape(ims1)[0]
	print(np.shape(ims3))
	for i in range(mcols):
		for j in range(np.shape(ims1)[1]):
			"""print(i,j)
			print(ims1[i,j])
			print(ims2[i,j])"""
			if abs(ims1[i,j]-ims2[i,j])<=15:
				ims3[i,j]=1
				ctr+=1
	print(ctr)
	sim=(ctr/(mcols*np.shape(ims1)[1]))
	print(sim)



	return sim



	#AV2.start_AVrecording(file_name)
	#time.sleep(length)
	#AV2.stop_AVrecording(file_name)
#AV_Split.split_av("D:\mpstme\SEM 7\PROJECT","F02-B1-DV-1")

