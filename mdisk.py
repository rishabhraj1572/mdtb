import requests
import json
import os
import subprocess

#setting
currentFile = __file__
realPath = os.path.realpath(currentFile)
dirPath = os.path.dirname(realPath)
dirName = os.path.basename(dirPath)
ytdlp = dirPath + "/binaries/yt-dlp"
aria2c = dirPath + "/binaries/aria2c"
mkvmerge = dirPath + "/binaries/mkvmerge"
ffmpeg = dirPath + "/ffmpeg/ffmpeg"

os.system(f"chmod 777 {ytdlp} {aria2c} {mkvmerge} {ffmpeg} ffmpeg/ffprobe ffmpeg/qt-faststart")

def req(link):
    inp = link #input('Enter the Link: ')
    fxl = inp.split("/")
    cid = fxl[-1]

    URL = f'https://diskuploader.entertainvideo.com/v1/file/cdnurl?param={cid}'

    header = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://mdisk.me/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    }

    print("Requesting to Server")


    #requesting
    resp = requests.get(url=URL, headers=header).json()['source']
