from moviepy.editor import VideoFileClip
import ffmpeg

def convert_mp4_to_mp3(input_path, output_path):
    # Use ffmpeg to convert and downmix audio to mono
    (
        ffmpeg
        .input(input_path)
        .output(output_path, ac=1)  # 'ac=1' sets the audio to mono
        .run()
    )


# Example usage:
input_path = "./mp4/dover3.mp4"
output_path = "./mp3/dover3.mp3"
convert_mp4_to_mp3(input_path, output_path)