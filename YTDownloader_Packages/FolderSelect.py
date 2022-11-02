import os,logging
from tkinter import filedialog

def FolderSelect():
    try:
        filePath = filedialog.askdirectory()
        return filePath
    except Exception as e:
        logging.exception("exception occured " + str(e))
        filePath = os.getcwd()
        return filePath