import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
import math
import contextlib
import scipy.io.wavfile as wav
from numpy.lib import stride_tricks
from scipy import signal
import os
import librosa
import xlsxwriter    
from scipy.io import wavfile #for audio processing

fname = ''
fname2 = ''
outname = ''
def setname(file_name):
	global fname, outname,fname2
	fname2=file_name
	fname=file_name+".wav"
	outname=file_name+"_spect"
	print(fname)
	something()
	return plotstft(fname)

cutOffFrequency = 400.0

# from http://stackoverflow.com/questions/13728392/moving-average-or-running-mean
def running_mean(x, windowSize):
  cumsum = np.cumsum(np.insert(x, 0, 0)) 
  return (cumsum[windowSize:] - cumsum[:-windowSize]) / windowSize

# from http://stackoverflow.com/questions/2226853/interpreting-wav-data/2227174#2227174
def interpret_wav(raw_bytes, n_frames, n_channels, sample_width, interleaved = True):

    if sample_width == 1:
        dtype = np.uint8 # unsigned char
    elif sample_width == 2:
        dtype = np.int16 # signed 2-byte short
    else:
        raise ValueError("Only supports 8 and 16 bit audio formats.")

    channels = np.frombuffer(raw_bytes, dtype=dtype)

    if interleaved:
        # channels are interleaved, i.e. sample N of channel M follows sample N of channel M-1 in raw data
        channels.shape = (n_frames, n_channels)
        channels = channels.T
    else:
        # channels are not interleaved. All samples from channel M occur before all samples from channel M-1
        channels.shape = (n_channels, n_frames)

    return channels
def something():
	with contextlib.closing(wave.open(fname,'rb')) as spf:
	    sampleRate = spf.getframerate()
	    ampWidth = spf.getsampwidth()
	    nChannels = spf.getnchannels()
	    nFrames = spf.getnframes()

	    # Extract Raw Audio from multi-channel Wav File
	    signal = spf.readframes(nFrames*nChannels)
	    spf.close()
	    channels = interpret_wav(signal, nFrames, nChannels, ampWidth, True)

	    # get window size
	    # from http://dsp.stackexchange.com/questions/9966/what-is-the-cut-off-frequency-of-a-moving-average-filter
	    freqRatio = (cutOffFrequency/sampleRate)
	    N = int(math.sqrt(0.196196 + freqRatio**2)/freqRatio)

	    # Use moviung average (only on first channel)
	    filtered = running_mean(channels[0], N).astype(channels.dtype)

	    wav_file = wave.open(outname, "w")
	    wav_file.setparams((1, ampWidth, sampleRate, nFrames, spf.getcomptype(), spf.getcompname()))
	    wav_file.writeframes(filtered.tobytes('C'))
	    wav_file.close()



	###spectrum############

	###
	
###
""" short time fourier transform of audio signal """
def stft(sig, frameSize, overlapFac=0.5, window=np.hanning):
    win = window(frameSize)
    hopSize = int(frameSize - np.floor(overlapFac * frameSize))
    
    # zeros at beginning (thus center of 1st window should be for sample nr. 0)
    #samples = np.append(np.zeros(np.floor(frameSize/2.0)), sig).astype(int)#error here
    samples = np.append(np.zeros(int (frameSize/2.0)), sig)
    # cols for windowing
    cols = np.ceil( (len(samples) - frameSize) / float(hopSize)) + 1
    # zeros at end (thus samples can be fully covered by frames)
    samples = np.append(samples, np.zeros(int(frameSize)))
    cols=int(cols)
    frames = stride_tricks.as_strided(samples, shape=(cols, frameSize), strides=(samples.strides[0]*hopSize, samples.strides[0])).copy()
    frames *= win
    
    return np.fft.rfft(frames)    
    
""" scale frequency axis logarithmically """    
def logscale_spec(spec, sr=44100, factor=20.):
    timebins, freqbins = np.shape(spec)

    scale = np.linspace(0, 1, freqbins) ** factor
    scale *= (freqbins-1)/max(scale)
    scale = np.unique(np.round(scale))
    
    # create spectrogram with new freq bins
    newspec = np.complex128(np.zeros([timebins, len(scale)]))
    for i in range(0, len(scale)):
        if i == len(scale)-1:
            newspec[:,i] = np.sum(spec[:,int(scale[i]):], axis=1)
        else:        
            newspec[:,int(i)] = np.sum(spec[:,int(scale[int(i)]):int(scale[int(i+1)])], axis=1)
    
    # list center freq of bins
    allfreqs = np.abs(np.fft.fftfreq(freqbins*2, 1./sr)[:freqbins+1])
    freqs = []
    for i in range(0, len(scale)):
        if i == len(scale)-1:
            freqs += [np.mean(allfreqs[int(scale[i]):])]
        else:
            freqs += [np.mean(allfreqs[int(scale[i]):int(scale[i+1])])]
    
    return newspec, freqs

""" plot spectrogram"""
def plotstft(audiopath, binsize=2**10, plotpath=True, colormap="jet"):
	workbook = xlsxwriter.Workbook((fname[:(fname.find('.wav'))]+".xlsx"))
	worksheet = workbook.add_worksheet()
	samplerate, samples = wav.read(audiopath)
	s = stft(samples, binsize)
	sshow, freq = logscale_spec(s, factor=1.0, sr=samplerate)
	ims = 20.*np.log10(np.abs(sshow)/10e-6) # amplitude to decibel
	row = 0
	print (np.shape(ims))
	for col, data in enumerate(ims):
		worksheet.write_column(row, col, data)
	workbook.close()
	timebins, freqbins = np.shape(ims)
	plt.figure(figsize=(15, 7.5))
	plt.imshow(np.transpose(ims), origin="lower", aspect="auto", cmap=colormap, interpolation="none")          #
	plt.colorbar()
	plt.xlabel("time (s)")
	plt.ylabel("frequency (hz)")
	plt.xlim([0, timebins-1])
	plt.ylim([0, freqbins])
	xlocs = np.float32(np.linspace(0, timebins-1, 5))
	plt.xticks(xlocs, ["%.02f" % l for l in ((xlocs*len(samples)/timebins)+(0.5*binsize))/samplerate])
	ylocs = np.int16(np.round(np.linspace(0, freqbins-1, 10)))
	plt.yticks(ylocs, ["%.02f" % freq[i] for i in ylocs])
	x1,x2,y1,y2 = plt.axis()
	plt.axis((x1,x2,y1,200))
	if plotpath:
		plt.savefig((fname2+"_spect"), bbox_inches="tight")#"\\static\\images\\"+
		print("image saved")
	else:
		plt.show()
	plt.clf()
	return ims
    
    




