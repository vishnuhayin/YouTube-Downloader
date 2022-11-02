import os, logging
import tkfontchooser
from YTDownloader_functions import *
import tkinter as tk

def main():
    root = tk.Tk()
    root.geometry('550x300')
    root.resizable(0,0)
    root.config(bg="#808080")
    root.title("Enjoy Downloading Videos !!!")

    link = tk.StringVar()
    defaultLocation = tk.StringVar()
    defaultLocation.set(os.getcwd())

    def saveToLocation():
        defaultLocation.set(selectFile())
        save_to = tk.Entry(root, width=40, textvariable = defaultLocation)
        save_to.place(x=140, y=120)

    def DownloadFile():
        location = save_to.get()
        if Downloader(link, location):
            DownloadLabel = tk.Label(root, bg="#808080", text = '!! DOWNLOADED !!', font = 'arial 15')
            DownloadLabel.place(x= 175 , y = 220)
        else:
            DownloadLabel = tk.Label(root, bg="#808080", text= 'Download Failed.', font='arial 15')
            DownloadLabel.place(x=175, y=220)

    Heading = tk.Label(root, text='Youtube Video Downloader', bg="#808080",
                       font = tkfontchooser.Font(family="Comic Sans MS", size=20, weight="bold") )
    Heading.pack(pady= 5)

    urlLabel = tk.Label(root, bg="#808080", text = 'Paste Video URL:',
                        font = tkfontchooser.Font(family='Comic Sans MS', size=10, weight="normal"))
    urlLabel.place(x= 30 , y = 60)
    link_enter = tk.Entry(root, width = 51,textvariable = link)
    link_enter.place(x = 150, y = 60)

    saveToLabel = tk.Label(root, bg="#808080", text = 'Save video to:',
                           font = tkfontchooser.Font(family='Comic Sans MS', size=10, weight="normal"))
    saveToLabel.place(x= 30 , y = 120)
    save_to = tk.Entry(root, width = 43, textvariable = defaultLocation)
    save_to.place(x = 140, y = 120)

    browseButton = tk.Button(root,text = 'Browse',
                             font = tkfontchooser.Font(family='Comic Sans MS', size=10, weight="normal"),
                             bg = '#8B8000', padx = 2, command = saveToLocation)
    browseButton.place(x=460 ,y = 115)

    downloadButton = tk.Button(root,text = ' Download File ',
                                font = tkfontchooser.Font(family='Comic Sans MS', size=10, weight="bold"),
                                bg = '#04F404', padx = 2, command = DownloadFile)
    downloadButton.place(x=200, y=170)
    root.mainloop()
    return

# if __name__ == '__main__':
#     main()