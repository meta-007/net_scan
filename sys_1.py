import os
import urllib.request 
import ctypes
import ssl
from moviepy.editor import VideoFileClip
import pygame
#import sys
from pytube import YouTube
import webbrowser  


context = ssl._create_unverified_context()
sysRoot = os.path.expanduser('~')
print(sysRoot)
path = f'{sysRoot}/Desktop/background.webp'
imageUrl = 'https://cdn.bhdw.net/im/spider-man-sitting-on-building-in-the-rain-wallpaper-91214_w635.webp'
response = urllib.request.urlopen(imageUrl,context=context)
image = response.read()
with open(path, "wb") as file:
    file.write(image)
    

# Go to specif url and download+save image using absolute path
#path = f'{sysRoot}/Desktop/background.jpg'
#print(path)
#client.send(f"Image file path:{path}".encode())
#urllib.request.urlretrieve(imageUrl, path,verify=False)
SPI_SETDESKWALLPAPER = 20
# Access windows dlls for funcionality eg, changing dekstop wallpaper
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)


# url of the video

#sysRoot = os.path.expanduser('~')
#path = f'{sysRoot}/Desktop/video'
url = "https://www.youtube.com/watch?v=ruKlY2yLIj4  "
yt = YouTube(url)
stream = yt.streams.get_by_itag(22)
video = yt.streams.get_highest_resolution()
path =video.download()

def video_player(file_path):
    
    pygame.init()
    screen = pygame.display.set_mode((800, 600), pygame.NOFRAME)
    pygame.display.set_caption("Video Player")
      # Prevent default close behavior
        
    try:
        clip = VideoFileClip(file_path)
        clip.preview()
    except Exception as e:
        print("Error: Could not load or play the video file.", e)
    finally:
        while True: 
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pass
         pygame.display.flip()
                
         

    #    pygame.quit()
    #    sys.exit()

if __name__ == "__main__":
      # Replace with the actual path to your video file
    video_player(path)