from moviepy.editor import *

def convert_mp4_to_mp3(input_path, output_path):
    video = VideoFileClip(input_path)
    audio = video.audio
    audio.write_audiofile(output_path)
    audio.close()
    video.close()

# Example usage:
input_path = "./mp4/dover4.mp4"
output_path = "./mp3/dover4.mp3"
convert_mp4_to_mp3(input_path, output_path)