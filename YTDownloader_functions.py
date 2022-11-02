from YTDownloader_Packages.DownloadVideo import DownloadVideo
from YTDownloader_Packages.FolderSelect import FolderSelect

def selectFile():
    return FolderSelect()

def Downloader(URL, location):
    return DownloadVideo(URL, location)
