from pytubefix import YouTube
import const

yt = YouTube(const.URL,use_po_token=True)
for stream in yt.streams.filter(type='audio'):
    print(stream)