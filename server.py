import socket
import ffmpeg
import subprocess
import yt_dlp
import subprocess
import dump
import play

stream = True
static_url = "https://www.youtube.com/live/dqbPOGv3MrY?si=ALDRdRQj2FHJvj6Q"
temp_stream = "temp_stream.mp4"

# def server_start():
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#     # set up socket connection
#     server_address = ('localhost', 10000)
#     sock.bind(server_address)

#     # listen for incoming connections
#     sock.listen(1)

def grab_livestream(static_url, temp_stream):
    try:
        ydl_json = {
            'outtmpl': temp_stream,
            'max_filesize': 1000000,
            'abort-on-error': True
        }
        with yt_dlp.YoutubeDL(ydl_json) as ydl:
            ydl.download([static_url])

        play.store = temp_stream
        play.VideoPlayer(play.store)
        stream = False
        return stream

    except Exception as e:
        print("Error: ", e)
        stream = False
        return stream
    
    ## vlc play or tkinter play video in window






# empty
if __name__ ==  "__main__":

    while stream is True:
        grab_livestream(static_url, temp_stream)