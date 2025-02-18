from pytubefix import Playlist
from colorama import Fore, Style
from mod.config import Config
import time
import const


config = Config()


def init_config():
    print(Style.BRIGHT)
    config.pytubefix.innertube.replace_token_verifier()
    config.create_output(const.PATH)


def download_playlist(playlist_url, output_path):
    playlist = Playlist(playlist_url,use_po_token=True)
    print(Fore.CYAN + f'Descargando playlist: {playlist.title}' + Style.RESET_ALL)

    for video in playlist.videos:
        print(Fore.YELLOW + f'Descargando: {video.title}...' + Style.RESET_ALL)
        audio_stream = video.streams.filter(only_audio=True).first()
        audio_stream.download(output_path)
        print(Fore.GREEN + f'{video.title} descargado con éxito.\n' + Style.RESET_ALL)
    
    print(Fore.MAGENTA + 'Playlist descargada completamente.' + Style.RESET_ALL)

if __name__ == '__main__':
    init_config()
    download_playlist(const.URL, const.PATH)

Style.RESET_ALL
config.clear()

