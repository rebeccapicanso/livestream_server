import os
import yt_dlp
import ffmpeg
import threading
import cv2
import numpy
import time
import io
import threading


stream = True
static_url = "https://www.youtube.com/live/dqbPOGv3MrY?si=ALDRdRQj2FHJvj6Q"
temp_stream = "temp_stream_yay.mp4"


class VideoStream:
    thread = None  # background thread that reads frames from camera
    frame = None  # current frame is stored here by background thread
    last_access = 0  # time of last client access to the camera
    path = None

    def __init__(self, path: str):
        self.path = path

    def initialize(self):
        if self.thread is None:
            # start background frame thread
            self.thread = threading.Thread(target=self._thread)
            self.thread.start()

            # wait until frames start to be available
            while self.frame is None:
                time.sleep(0)

    def get_frame(self):
        self.last_access = time.time()
        self.initialize()
        return self.frame

    @classmethod
    def _thread(cls):
        while True:
            cls.grab_livestream(static_url, temp_stream)
            time.sleep(10)
        # temp_stream = "temp_stream_yay.mp4"
        # cap = cv2.VideoCapture(temp_stream)
        
        # # Check if video opened successfully
        # if not cap.isOpened():
        #     print(f"Error: Could not open video file: {cls.path}")
        #     return

        # # Get video properties
        # frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        # frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # fps = int(cap.get(cv2.CAP_PROP_FPS))
        # total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        # print(f"Video Properties:")
        # print(f"Dimensions: {frame_width}x{frame_height}")
        # print(f"FPS: {fps}")
        # print(f"Total Frames: {total_frames}")
        
        # frame_count = 0
        
        # stream = io.BytesIO()

        # # Read until video is completed
        # while cap.isOpened():
        #     # Capture frame-by-frame
        #     ret, frame = cap.read()
            
        #     if ret:
        #         frame_count += 1
                
        #         # Here you can process the frame
        #         # 'frame' is a numpy array in BGR format
                
        #         # Example: Display the frame
        #         #cv2.imshow('Frame', frame)

        #         # store frame
        #         stream.seek(0)
        #         cls.frame = stream.read()
                
        #         # Press Q on keyboard to exit
        #         if cv2.waitKey(25) & 0xFF == ord('q'):
        #             break
        #     else:
        #         break
        
        # # Release everything when done
        # cap.release()
        # cv2.destroyAllWindows()
        # cls.thread = None

    @staticmethod
    def grab_livestream(static_url, temp_stream):
        try:
            ydl_json = {
                'outtmpl': temp_stream
            }
            with yt_dlp.YoutubeDL(ydl_json) as ydl:
                ydl.download([static_url])
            print("LINE 16 DONE! 🐣 🐣 🐣 🐣 🐣 🐣 🐣 ")

            store = temp_stream
            return store

        except Exception as e:
            print("Error: ", e)
            return False

if __name__ == "__main__":
    print("THIS PLAYED :-)")
    while stream is True:
        # video = Video.grab_livestream(static_url, temp_stream)
        # print(video)
        # print("Playing video, LINE 29 🐑 🐑 🐑 🐑 🐑 🐑 🐑 ")
        # os.system(f"ffplay -i {video}")

        break