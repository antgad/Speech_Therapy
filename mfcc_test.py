import scipy.io.wavfile as wav
import wave
import librosa
import matplotlib.pyplot as plt
import librosa.display
from fastdtw import fastdtw
print("imoprted")
samples, samplerate = librosa.load("2129-iau(1).wav")
samples2, samplerate2 = librosa.load("68-iau.wav")
print("imoprted")
print(type(samples))
print(type(samplerate))
mfcc1 = librosa.feature.mfcc(y=samples, sr=samplerate, n_mfcc=40)

#plt.figure(figsize=(10, 4))
#librosa.display.specshow(mfccs, x_axis='time')
#plt.colorbar()
#lt.title('MFCC')
#plt.tight_layout()
#plt.show()
plt.subplot(1, 2, 1) 
#mfcc1 = librosa.feature.mfcc(y1,sr1)   #Computing MFCC values
librosa.display.specshow(mfcc1)

plt.subplot(1, 2, 2)
mfcc2 = librosa.feature.mfcc(y=samples2, sr=samplerate2, n_mfcc=40)
librosa.display.specshow(mfcc2)
print((mfcc1.shape))
print((mfcc2.shape))
print((mfcc1))
print(mfcc2)

dist, cost = fastdtw(mfcc1.T, mfcc2.T)#, dist='euclidean')
print("The normalized distance between the two : ",dist)   # 0 for similar audios 

#plt.imshow(cost.T, origin='lower', cmap=plt.get_cmap('gray'), interpolation='nearest')
#plt.plot(path[0], path[1], 'w')   #creating plot for DTW

plt.show()  #To display the plots graphically