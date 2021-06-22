import os
from pytube import YouTube

def downloader(link):
    url = YouTube(link)

    os.chdir(os.path.join(os.path.expanduser('~'),'desktop'))

    video = url.streams.first()

    video.download()

    print(video.title,"- DOWNLOADED succesfully")

downloader("https://www.youtube.com/watch?v=PT2_F-1esPk") #<--YOUR YOUTUBE VIDEO LINK HERE
