import moviepy.editor
video_file="KANAK.mp4"
audio_file="KANAK.wav"
video=moviepy.editor.VideoFileClip(video_file)

audio = video.audio
audio.write_audiofile(audio_file)