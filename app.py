import ffmpeg
import yt_dlp
import subprocess
from flask import Flask, send_file, render_template, Response
from video import VideoStream, temp_stream
import os

video_stream = VideoStream(temp_stream)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# def gen(livestream):
#     while True:
#         frame = livestream.get_frame()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# @app.route('/get_feed')
# def video_feed():
#     temp_stream = "temp_stream_yay.mp4"
#     return Response(gen(VideoStream(path=temp_stream)),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video')
def video():
    if os.path.exists(temp_stream):
        return send_file(temp_stream, mimetype='video/mp4')
    else:
        return "Stream not found", 404

livestream = ''
if __name__ ==  "__main__":
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
    