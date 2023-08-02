# Mini project 13
# Install the essential packages:
# !pip install moviepy

from moviepy.editor import VideoFileClip
import os
def convert_video_to_audio_moviepy(video_file, output_ext="mp3"):
    """Converts video to audio using MoviePy library
    that uses `ffmpeg` under the hood"""
    filename, ext = os.path.splitext(video_file)
    clip = VideoFileClip(video_file)
    clip.audio.write_audiofile(f"{filename}.{output_ext}")

convert_video_to_audio_moviepy('D:\Coding\Python programmming\summer_school\proj_13.mp4')