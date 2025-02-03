from pytubefix import YouTube
from mod.config import Config
import const


config = Config()
config.clear()
config.pytubefix.innertube.replace_token_verifier()
config.clear()

yt = YouTube(const.URL,use_po_token=True)
print(yt.streams)