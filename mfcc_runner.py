print("importing librosa")
import librosa
def mfcc_run(audio_file):
	samples, samplerate = librosa.load(audio_file+."wav")
	mfcc1 = librosa.feature.mfcc(y=samples, sr=samplerate, n_mfcc=40)
	return mfcc1