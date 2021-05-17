from pytube import YouTube
from moviepy.editor import *
import time
import os

def convertYtVid(string):
    yt = YouTube(string)
    name = str(int(time.time()))
    yt.streams.filter(
        progressive = True,
        file_extension = "mp4"
    ).first().download(output_path = "pytube/",filename = name)
    video = VideoFileClip(os.path.join("pytube/", name + ".mp4"))
    video.audio.write_audiofile(os.path.join("audio/", name + ".wav"))