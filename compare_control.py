import integrate
import numpy as np
import noise_spect
print("running for first file")
#ims1,mfcc1=integrate.controller()
ims1=noise_spect.setname("2149-iau(1)")
print(np.shape(ims1))
print("running for second file")
#ims2,mfcc2=integrate.controller()
ims2=noise_spect.setname("68-iau")
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
