from pytube import YouTube
from pytube import Channel
from pytube import Search
from pytube import Playlist

#Easing the download process using Pytube from anywhere

"""
1. Ask what is the type of link you are having 
- Video Link
- Channel Link
- Playlist Link

What you want to do with the Link?

if Video Link:
    -download Video
    -download Audio

if Channel Link:
    -List the 
2. List the choices for 
"""
linkType = input("Enter the type of link you have[Video\Channel\Playlist])
if lower(linkType) == "video":
    link = input('Provide the link of the youtube video:')
    kind = input('Select V for Video else A for Audio')
def dload_vid(link):
    vid = YouTube(link)
    stream = vid.streams
    get_vid = stream.get_highest_resolution()
    get_vid.download()

def dload_aud(link):
    vid = YouTube(link)
    stream = vid.streams
    get_aud = stream.get_by_itag(140)
    get_aud.download()
print('starting download....')
if kind == 'V':
    dload_vid(link)
else:
    dload_aud(link)
print('Completing download....')
