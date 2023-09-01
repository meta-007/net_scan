import cv2
import os
from pytube import YouTube
from moviepy.editor import *
import moviepy
import tkinter as tk
from tkVideoPlayer import TkinterVideo
from pydub import AudioSegment
from pydub.playback import play
import pygame

# url of the video
root = tk.Tk()
#sysRoot = os.path.expanduser('~')
#path = f'{sysRoot}/Desktop/video'
url = "https://www.youtube.com/watch?v=Qnagf4K4Ju8"
yt = YouTube(url)
stream = yt.streams.get_by_itag(22)
video = yt.streams.get_highest_resolution()
path =video.download()

#videoplayer = TkinterVideo(master=root, scaled=True)
#videoplayer.load(path)
#videoplayer.pack(expand=True)

#videoplayer.play() # play the video

#root.mainloop()


#videos = moviepy.editor.VideoFileClip(path)
#aud = videos.audio
#aud.write_audiofile("audio.mp3")


#def audio_player(file_path):
#    pygame.init()
#    pygame.mixer.init()
    
#    try:
#        pygame.mixer.music.load(file_path)
#        pygame.mixer.music.play()
        
#        while pygame.mixer.music.get_busy():
#            continue
#    except pygame.error:
#        print("Error: Could not load or play the audio file.")

#    pygame.quit()

#if __name__ == "__main__":
#    audio_file_path = "C:/Users/Sarvesh Kumar/Desktop/python/audio.mp3"  # Replace with the actual path to your audio file
#    audio_player(audio_file_path)





