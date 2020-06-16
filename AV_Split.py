import moviepy.editor
def split_av(file_path, file_name):
	video_file=file_path +file_name+".mp4"
	audio_file=file_path +file_name+".wav"
	video=moviepy.editor.VideoFileClip(video_file)

	audio = video.audio
	audio.write_audiofile(audio_file)