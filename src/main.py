import const

from pytubefix import Playlist, YouTube
from colorama import Fore, Style
from time import sleep

from mod.config import Config
from mod.menu import Menu
from mod.mp3_convert import convert_mp4_to_mp3




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


def disk_first_options():
    options={
        "Playlist": download_playlist,
        "Video": download_video,
    }
    menu = Menu(options)
    menu.showOptions()

    choicedOption= int(input("Select a option:"))
    menu.executeSelect(choicedOption,const.URL,const.PATH)
    
def disk_second_options():
    options={
        "Mp4": "",
        "Mp3": convert_mp4_to_mp3,
    }
    menu = Menu(options)
    menu.showOptions()

    choicedOption= int(input("Select a option: "))
    menu.executeSelect(choicedOption, const.PATH)
    


if __name__ == '__main__':
    init_config()
    disk_first_options()
    disk_second_options()
    
Style.RESET_ALL
config.clear()

