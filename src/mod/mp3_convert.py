import os
from moviepy import VideoFileClip

def convert_mp4_to_mp3(path):
    files = os.listdir(path)

    for file in files:
        if file.endswith(".mp4"):
            input_path = os.path.join(path, file)
            output_path = os.path.join(path, file.replace(".mp4", ".mp3"))

            try:
                video = VideoFileClip(input_path)
                video.audio.write_audiofile(output_path)

                os.remove(input_path)
                print(f"Convertido y reemplazado: {file} -> {output_path}")

            except Exception as e:
                print(f"Error al convertir {file}: {e}")

