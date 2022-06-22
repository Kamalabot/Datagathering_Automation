#program that takes in youtube link and downloads video to your local drive

from pytube import YouTube
from pytube import Channel
from pytube import Search
from pytube.innertube import InnerTube

from sys import argv

link = argv[1]


def dload_vid(link):
    
    """Function takes the link, and send out the video"""
    
    vid = YouTube(link)
    stream = vid.streams
    get_vid = stream.get_highest_resolution()
    get_vid.download()

def main():
    
    dload_vid(link)

if __name__ == "__main__": main()