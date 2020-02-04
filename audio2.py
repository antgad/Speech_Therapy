
import os
import librosa   #for audio processing
#import IPython.display as ipd
import matplotlib.pyplot as plt

import numpy as np
from scipy.io import wavfile #for audio processing
#print('A')
# 1. Get the file path to the included audio example

# 2. Load the audio as a waveform `y`
#    Store the sampling rate as `sr`
f1=input("FILE 1:")
samples, sample_rate = librosa.load(f1, sr = 16000)
#print(samples)
#print(sample_rate)
samples = librosa.resample(samples, sample_rate, 8000)
#print(samples)
print(len(samples))
for i in range(10):
    print (samples[i])

fig = plt.figure(figsize=(14, 8))
ax1 = fig.add_subplot(211)
#a=np.linspace(0, sample_rate/len(samples), 8000)
#print(a)
#ax1.plot(np.linspace(0, sample_rate/len(samples), sample_rate), samples)
ax1.plot(np.linspace(0, sample_rate,num=len(samples)), samples)
print(np.linspace(0, sample_rate, num=len(samples)).shape)
print(samples.shape)
plt.title('Anant "a"')
plt.show()
#plt.title('Kanak a')
#plt.subplot(221)
#print("zfdv")
