import socket
from tkinter import *
from threading import Thread
from tkinter import ttk
from tkinter import filedialog

PORT = 8050
IP_ADDRESS = "127.0.0.1"
SERVER = None
BUFFER_SIZE = 4096

listBox = None


def connectToServer():
    global SERVER
    global name
    global sendingFile

    cname = name.get()
    SERVER.send(cname.encode())


def musicWindow():
    print("\n\t\t\t\t\t\tIP MESSENGER\n")
    window = Tk()
    window.title("Music Window")
    window.geometry("300x300")
    window.configure(bg="LightSkyBlue")
    global listBox

    selectLabel = Label(window, text="Select Song", bg="LightSkyBlue", font=("Calibri", 8))
    selectLabel.place(x=2, y=1)

    listBox = Listbox(window, height=10, width=39, activestyle="dotbox", bg="LightSkyBlue", borderwidth=2, font=("Calibri", 10))
    listBox.place(x=10, y=10)

    scrollbar1 = Scrollbar(listBox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listBox.yview)

    playButton = Button(window, text="Play", width=10, bd=1, bg="SkyBlue", font=("Calibri", 10))
    playButton.place(x=30, y=200)

    stopButton = Button(window, text="Stop", width=10, bd=1, bg="SkyBlue", font=("Calibri", 10))
    stopButton.place(x=200, y=200)

    uploadButton = Button(window, text="Upload", width=10, bd=1, bg="SkyBlue", font=("Calibri", 10))
    uploadButton.place(x=30, y=250)

    downloadButton = Button(window, text="Download", width=10, bd=1, bg="SkyBlue", font=("Calibri", 10))
    downloadButton.place(x=200, y=250)

    infoLabel = Label(window, text= "",fg= "blue", font = ("Calibri", 8))
    infoLabel.place(x=4, y=280)

    window.mainloop()


def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))
    musicWindow()


setup()

