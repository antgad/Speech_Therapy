
print("Import Sequence Initiated...")
import os
import librosa   #for audio processing
#import IPython.display as ipd
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile #for audio processing
#print('A')
#print ('Hi')
#print ('Audio 1: Harshitha "a"')
#print ('Audio 2: Anant "a"')
f1=input("FILE 1:")
f2=input("FILE 2:")

#from os import listdir
#from os.path import isfile, join
#mypath='C://Users//Anant//Downloads//F//F01//Session1'
#onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#print(onlyfiles)


print("Import Sequence Completed...")
path = 'D://mpstme//SEM 7//PROJECT//Datasets//Control//Male//MC01'

files1 = [f1]
files2 = [f2]
# r=root, d=directories, f = files
# for r, d, f in os.walk(path):
#     for file in f:
#         if '.wav' in file:
#             files1.append(os.path.join(r, file))
# print("DIR 1 Imported")
# path = 'D://mpstme//SEM 7//PROJECT//Datasets//Control//Male//MC02'
# for r, d, f in os.walk(path):
#     for file in f:
#         if '.wav' in file:
#             files2.append(os.path.join(r, file))
# print("DIR 2 Imported")
m=-1
for f1 in files1:
    for i in range (1):
        m=m+1
        f2=files2[m]
        
        samples, sample_rate = librosa.load(f1, sr = 16000)
        #print(samples)
        #print(sample_rate)
        samples = librosa.resample(samples, sample_rate, 8000)
        #print(samples)
        #print("No of samples (audio 1):",len(samples))
        l1=len(samples)
        #for i in range(10):
        #    print (samples[i])
        #fig = plt.figure(figsize=(14, 8))
        #ax1 = fig.add_subplot(211)
        #a=np.linspace(0, sample_rate/len(samples), 8000)
        #print(a)
        #ax1.plot(np.linspace(0, sample_rate/len(samples), sample_rate), samples)
        #ax1.plot(np.linspace(0, sample_rate,num=len(samples)), samples)
        #print(np.linspace(0, sample_rate, num=len(samples)).shape)
        #print(samples.shape)
        #plt.show()
        #print("zfdv")

        samples2, sample_rate2 = librosa.load(f2, sr = 16000)
        samples2 = librosa.resample(samples2, sample_rate2, 8000)
        #print("No of samples (audio 2):",len(samples2))
        l2=len(samples2)
        #print(type(samples2))
        m1=samples.max()
        m2=samples2.max()
        s3=[]
        s4=[]
        s5=[]
        #l1=100
        #l2=100
        for i in range(l1):
            s3.append(samples[i]/m1)
        for j in range(l2):

            s4.append(samples2[j]/m2)
        #print(s3)
        #print(s4)
        g=0
        h=0
        while(s4[g]<0):
            s4.pop(g)
        while(s3[h]<0):
            s3.pop(h)
        #print(s3)
        #print(s4)

        if(len(s3)<len(s4)):
            a=len(s3)
        else:
            a=len(s4)
               
        for k in range(a):
            if(abs(s3[k]-s4[k])<0.1):
                s5.append(1)
            else:
                s5.append(0)

        sums=sum(s5)
        c=100*(sums/l1)
        print("File 1"+str(f1))
        print("File 2"+str(f2))
        print("Percentage similarity:",c)


