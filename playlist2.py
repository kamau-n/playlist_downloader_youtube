#!/usr/bin/env python3
import os

from pytube import Playlist
link=input("Enter the link \n")


# Get the current user's home directory
home_directory = os.path.expanduser("~")

playlistLocation  =home_directory +"/Downloads/YoutubeDownloader/"
print("Playlist is available at : " +  playlistLocation)


  
try:  
   playlist=Playlist(link)

   for video in playlist.videos:
       print("Downloading ..." + video.title)
       print()
    
       audio=video.streams.get_audio_only()
       try:
          audio.download(playlistLocation)
       except Exception as err:
          print("Error Occured :" , err)
except Exception as err2:
    print("Another Error Occurred " ,err2)
        
    
for i in os.listdir(path):
    if i.endswith('.mp4'):
       oldname=i
       _name=oldname[:-3]
       newname=_name+'mp3'
       newname=path+newname
       oldname=path+oldname
       os.rename(oldname,newname)
   
    
