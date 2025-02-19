from pytubefix import Playlist, YouTube
from colorama import Fore, Style
from mod.config import Config
import const
from time import sleep


config = Config()


def init_config():
    print(Style.BRIGHT)
    config.pytubefix.innertube.replace_token_verifier()
    config.create_output(const.PATH)

def download_playlist(playlist_url, output_path):
    playlist = Playlist(playlist_url,use_po_token=True)
    print(Fore.CYAN + f'Descargando playlist: {playlist.title}')

    for video in playlist.videos:
        print(Fore.YELLOW + f'Descargando: {video.title}...')
        stream = video.streams.first()
        stream.download(output_path)
        print(Fore.GREEN + f'{video.title} descargado con éxito.\n')
    
    print(Fore.MAGENTA + 'Playlist descargada completamente.')

def download_video(video_url, output_path):
    youtube = YouTube(video_url,use_po_token=True)
    print(Fore.CYAN + f'Descargando: {youtube.title}')
    stream = youtube.streams.first()
    stream.download(output_path)
    print(Fore.GREEN + f'{youtube.title} descargado con éxito.\n')
    sleep(2)

if __name__ == '__main__':
    init_config()
    # download_playlist(const.URL, const.PATH)
    download_video('https://www.youtube.com/watch?v=KpD53CQ5hSs',const.PATH)

Style.RESET_ALL
config.clear()

