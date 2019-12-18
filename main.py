# import subprocess
# def importPackage(package):
#     try:
#         __import__(package)
#     except ImportError:
#         subprocess.check_call(["pip", "install", package])

# importPackage("requests")
# importPackage("bs4")
# importPackage("pyperclip")

import tkinter as tk
from components import Header

root = tk.Tk()
root.geometry("500x500")
root.resizable(0, 0)
# set Title
root.title("Genius Lyrics Fetcher")

"""" Main Class """
class App:
    def __init__(self, master):
        self.master = master
        Header(master)
        
"""
song = input("Song name: ")
song = urllib.parse.quote(song)
print(song)
print(GeniusAPI.fetchLyrics(song))
"""

App(root)
root.mainloop()
