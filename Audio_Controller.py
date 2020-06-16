import noise_spect
import numpy as np
def audio_control(path,file_name):
	print("2129")
	ims1=noise_spect.setname(("2129-iau.wav"))
	print(np.shape(ims1))
	print("2149")
	ims2=noise_spect.setname("2149-iau.wav")
	print(np.shape(ims2))
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
	print((ctr/(mcols*np.shape(ims1)[1])))
