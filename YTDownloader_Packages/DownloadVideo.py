import logging
from pytube import YouTube

def DownloadVideo(URL, location):
    try:
        url = YouTube(str(URL.get()))
        video = url.streams.get_highest_resolution()
        video.download(location)
        logging.info("Downloaded from '" + str(url) + "'")
        logging.info("Saved file to '" + str(location) + "'")
        return True
    except Exception as e:
        logging.exception("exception occured "+ str(e))
        return False