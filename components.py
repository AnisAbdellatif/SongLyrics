import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from GeniusAPI import GeniusAPI
import io
from PIL import Image, ImageTk
import requests
import pyperclip

""" The Header section: Label + (Entry+Button) """
class Header:
    def __init__(self, master):
        self.master = master
        Header = tk.Frame(self.master)
        tk.Label(Header, text="Genius Lyrics Fetcher", font=("Arial Bold", 24)).pack()
        
        Input = tk.Frame(Header)
        self.inputSongName = tk.StringVar()

        self.songEntry = tk.Entry(Input, textvariable=self.inputSongName, width=35)
        self.songEntry.grid(row=0, column=0, padx=20, ipady=5)
        tk.Button(Input, text="Search", command=self.inputSearch, bg="blue", activebackground="#55f").grid(row=0, column=1)
        tk.Button(Input, text="Clear", command=self.inputClear, bg="red", activebackground="#f55").grid(row=0, column=2, padx=10)
        Input.pack()
        Header.pack(fill = tk.Y)
        self.songName = ""
        self.resultElements = None
        self.resultsFrame = None

    def inputSearch(self):
        if (self.inputSongName.get() == "") or (self.inputSongName.get() == self.songName) : return
        self.songName = self.inputSongName.get()
        print(self.songName)
        self.__pressHandler(self.songName)
    
    def inputClear(self, all=True):
        if all: self.inputSongName.set('')
        if (self.resultElements is not None):
            for element in self.resultElements:
                element.destroy()
        if (self.resultsFrame is not None): self.resultsFrame.destroy()

    def __pressHandler(self, songName):
        results = GeniusAPI.search(songName)
        results = map(lambda result: result["result"], results)
        self.inputClear(all=False)
        self.resultsFrame = tk.Frame(self.master)
        self.resultsFrame.pack()
        self.resultElements = []
        for song in results:
            self.resultElements.append( Result(self.resultsFrame, song) )


class Result:
    def __init__(self, master, song):
        self.__create(master, song)

    def __create(self, master, song):
        self.master = master
        resultElementFrame = tk.Frame(self.master)
        resultElementFrame.pack()
        songName = song["full_title"]
        songPath = song["path"]
        self.label = tk.Label(resultElementFrame, text=songName)
        self.label.pack(side=tk.LEFT)
        self.label.bind("<Button-1>", lambda e: self.__clickCallback(songName, songPath))
    
    def __clickCallback(self, songName, songPath):
        lyrics = tk.StringVar(value=GeniusAPI.fetchLyrics(songPath))
        lyricsPage = tk.Toplevel(self.master)
        lyricsPage.title(f"Lyrics for: {songName}")

        text = ScrolledText(lyricsPage)
        text.pack()
        text.insert(tk.END, lyrics.get())
        text.config(state=tk.DISABLED)

        tk.Button(lyricsPage, text="Copy", command=lambda : pyperclip.copy(lyrics.get())).pack()
        tk.Button(lyricsPage, text="Dismiss", command=lyricsPage.destroy).pack()

    def destroy(self):
        self.label.destroy()

class LogoImage:

    @staticmethod
    def Create(master, URL):
        img = ImageTk.PhotoImage(file = LogoImage.__getImage(URL))

        imgLabel = tk.Label(master, image=img, width=50, height=50)
        imgLabel.image = img
        imgLabel.pack()

    @staticmethod
    def __getImage(URL):
        imgweb = requests.get(URL).content
        return io.BytesIO(imgweb)
