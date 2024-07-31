import cv2
import os
from moviepy.editor import VideoFileClip

def get_bitrate(video_path):
    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        return None

    fps = video.get(cv2.CAP_PROP_FPS)
    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
    duration = frame_count / fps  # Thời gian video

    file_size = os.path.getsize(video_path) * 8  # Đổi byte sang bit

    bitrate = file_size / duration
    return bitrate

def video2sound(path):
    video = VideoFileClip(path)
    fps = video.fps
    if fps is None:
        fps = 24.0
    
    save_path  = os.path.splitext(path)[0]
    audio = video.audio
    audio.write_audiofile(f"{save_path}_audio.mp3")
    bitrate = get_bitrate(path)/1000
    video_no_audio = video.without_audio()
    video_no_audio.write_videofile(f"{save_path}_video_no_audio.mp4", codec = 'libx264', fps = fps, bitrate = f"{bitrate}k")
    audio.close()
    video.close()
    video_no_audio.close()
video2sound("SƠN TÙNG M-TP - ĐỪNG LÀM TRÁI TIM ANH ĐAU - OFFICIAL MUSIC VIDEO.mp4")