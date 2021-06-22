# In this program we will know 
# how to download any youtube video in mp3 format
# It is based on our last video

import os
from pytube import YouTube

def downloader(link):
    url = YouTube(link)
    os.chdir(os.path.join(os.path.expanduser('~'),'desktop'))

    audio = url.streams.filter(only_audio=True).first()

    audio.download()

    print("Downloaded Succesfully")

downloader("https://www.youtube.com/watch?v=3sCqPzrOhJU")