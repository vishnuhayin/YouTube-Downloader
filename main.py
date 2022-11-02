import logging
import YTDownloader_window

logging.basicConfig(filename = "YouTubeDownloader.log" , level = logging.INFO , format = '%(asctime)s %(levelname)s %(message)s')

def main():
    logging.info("YouTube Downloader Opened")
    YTDownloader_window.main()
    logging.info("YouTube Downloader Closed")

if __name__ == '__main__':
    main()
    