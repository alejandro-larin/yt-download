from pytubefix import Playlist
from colorama import Fore, Style
from mod.config import Config
import const


config = Config()

def init_config():
    print(Style.BRIGHT)
    config.pytubefix.innertube.replace_token_verifier()
    config.create_output(const.PATH)


def download_playlist(url,path):
    print('descargando playlist')

if __name__ == '__main__':
    init_config()
    download_playlist(const.URL, const.PATH)

Style.RESET_ALL
config.clear()

