import os
import yt_dlp
import threading
import time
from flask import Flask, send_file, render_template

app = Flask(__name__)

stream = True
static_url = "https://www.youtube.com/live/dqbPOGv3MrY?si=ALDRdRQj2FHJvj6Q"
chunk_prefix = "chunk_"
chunk_duration = 10  # Duration of each chunk in seconds
chunks_to_keep = 3  # Number of chunks to keep before deleting

class VideoStreamer:
    thread = None
    last_access = 0
    chunk_index = 0
    url = None
    chunk_prefix = None
    chunk_duration = None
    chunks = []

    def __init__(self, url, chunk_prefix, chunk_duration):
        VideoStreamer.url = url
        VideoStreamer.chunk_prefix = chunk_prefix
        VideoStreamer.chunk_duration = chunk_duration
        self.current_chunk = None

    def initialize(self):
        if VideoStreamer.thread is None:
            VideoStreamer.thread = threading.Thread(target=self._thread)
            VideoStreamer.thread.start()

            while self.current_chunk is None:
                time.sleep(0.1)

    def get_chunk(self):
        VideoStreamer.last_access = time.time()
        self.initialize()
        return self.current_chunk

    def grab_livestream(self):
        try:
            ydl_opts = {
                'outtmpl': f'{VideoStreamer.chunk_prefix}{VideoStreamer.chunk_index}.mp4',
                'format': 'best',
                'max_filesize': 1000000,
                'abort-on-error': True,
                'external_downloader_args': ['-ss', '0', '-t', str(VideoStreamer.chunk_duration)]
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([VideoStreamer.url])
            chunk_name = f'{VideoStreamer.chunk_prefix}{VideoStreamer.chunk_index}.mp4'
            self.current_chunk = chunk_name
            VideoStreamer.chunks.append(chunk_name)
            VideoStreamer.chunk_index += 1
            print(f"Downloaded chunk: {self.current_chunk}")
        except Exception as e:
            print("Error: ", e)
            self.current_chunk = None

    @classmethod
    def _thread(cls):
        while stream:
            instance = cls(cls.url, cls.chunk_prefix, cls.chunk_duration)
            instance.grab_livestream()
            if len(cls.chunks) > chunks_to_keep:
                old_chunk = cls.chunks.pop(0)
                os.remove(old_chunk)
                print(f"Deleted chunk: {old_chunk}")
            if time.time() - cls.last_access > 10:
                break
        cls.thread = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video/<int:chunk_id>')
def video(chunk_id):
    chunk_name = f'{chunk_prefix}{chunk_id}.mp4'
    if os.path.exists(chunk_name):
        return send_file(chunk_name, mimetype='video/mp4')
    else:
        return "Chunk not found", 404

if __name__ == "__main__":
    video_streamer = VideoStreamer(static_url, chunk_prefix, chunk_duration)
    app.run(debug=True)