from pytube import YouTube
from pytube import Channel
from pytube import Search

#get the link from the user
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