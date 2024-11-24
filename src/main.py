import yt_dlp
from modules.dir_create import dir_create
from modules.clear import clear
import const
clear()
dir_create(const.PATH_DOWNLOADS)
playlist_url = const.URL 
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': f'{const.PATH_DOWNLOADS}/%(title)s.%(ext)s',
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])
