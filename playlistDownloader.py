#/usr/bin/env python
from pytube import YouTube
from pytube import Playlist

linkPlay = input('Provide the Youtube Playlist Link: ')

start = int(input('If Interupted earlier, then provide the index: '))

kind = input('Select V for Video else A for Audio: ')

def midInteruptedList(link2Playlist, start = 0,kind='A'):
    trazCar = Playlist(link2Playlist)
    trazCarList= list(trazCar.video_urls)
    vidList = trazCarList[start:] #We can set the number of videos to download in one go
    for index, ind in enumerate(vidList):
        vidObj = YouTube(ind)        
        if vidObj.length != 0 and vidObj.length < 10000:
            print(f'{start + index} vid : {vidObj.title}')
            yt = YouTube(ind).streams
            if kind == 'V':
                get_vid = yt.get_highest_resolution()
                get_vid.download()
            if kind == 'A':
                stream = yt.get_by_itag(140)
                stream.download()

midInteruptedList(linkPlay,start,kind)


