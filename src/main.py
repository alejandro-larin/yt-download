from pytubefix import Playlist
from colorama import Fore, Style
from mod.config import Config
# import ffmpeg

import time
import os
import const


config = Config()


def init_config():
    print(Style.BRIGHT)
    config.pytubefix.innertube.replace_token_verifier()
    config.create_output(const.PATH)



# def chage_extension(file): 
#     try:
#         ffmpeg.input(mp4_path).output(mp3_path, format="mp3", audio_bitrate="192k").run(overwrite_output=True)
#         os.remove(mp4_path)  # Elimina el archivo MP4 después de la conversión
#         print(Fore.GREEN + f'Convertido a MP3: {mp3_path}' + Style.RESET_ALL)
#     except Exception as e:
#         print(Fore.RED + f'Error en la conversión: {e}' + Style.RESET_ALL)

def download_playlist(playlist_url, output_path):
    playlist = Playlist(playlist_url,use_po_token=True)
    print(Fore.CYAN + f'Descargando playlist: {playlist.title}')

    for video in playlist.videos:
        print(Fore.YELLOW + f'Descargando: {video.title}...')
        stream = video.streams.first()
        stream.download(output_path)
        print(Fore.GREEN + f'{video.title} descargado con éxito.\n')
    
    print(Fore.MAGENTA + 'Playlist descargada completamente.')

if __name__ == '__main__':
    init_config()
    download_playlist(const.URL, const.PATH)

Style.RESET_ALL
# config.clear()

