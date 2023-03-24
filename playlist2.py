#!/usr/bin/env python3
import os

from pytube import Playlist
link=input("Enter the link \n")

print("Enter the folder :\n")
print(''' 1. pop.
2. Afropop.
3.Hiphop.
4.Oldies.
5.Electric''')
folder=input()
if folder=="1":
    path='/harry/Music/pop/'
elif folder=="2":
    path='/harry/Music/afropop/'
elif folder=="3":
    path='/harry/Music/hiphop/'
elif folder=="4":
    path='/harry/Music/Oldies/'
elif folder=="5":
    path='/harry/Music/Electric/'

else:
    path='/harry/Videos/' + folder + '/'
  
try:  
   playlist=Playlist(link)

   for video in playlist.videos:
       print("Downloading ..." + video.title)
       print()
    
       audio=video.streams.get_audio_only()
       try:
          audio.download(path)
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
   
    
