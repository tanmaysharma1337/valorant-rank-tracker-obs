import tkinter as tk
from tkinter import Label
from tkinter import Entry
from overlay import Window
from tkinter import Button
import requests
from PIL import Image,ImageTk

root = tk.Tk()
root.title("Valorant Tracker")
root.geometry("400x140+1000+500")
root.iconbitmap("valorant.ico")
root.resizable(False,False)
usernamelabel = Label(root,text="Riot ID")
usernamelabel.pack()
usernameentry = Entry(root)
usernameentry.pack()
taglabel = Label(root,text = "Riot Tag")
taglabel.pack()
tagnameentry = Entry(root)
tagnameentry.pack()

def getentries():
    global username
    global tag
    username = usernameentry.get()
    tag = tagnameentry.get()
def getuserdata():
    global word
    username.replace(" " , "%20")
    r = requests.get(f"https://api.kyroskoh.xyz/valorant/v1/mmr/ap/{username}/{tag}?show=rankonly&display=0")
    word = r.text.split()
    print(word)
    return(word)


def getrankimage():
    global word
    global image1
    
    if(word[1] == "Radiant"):
        image1 = ImageTk.PhotoImage(Image.open(f"rank_png/{word[0]}.png"))
    else:
        image1 = ImageTk.PhotoImage(Image.open(f"rank_png/{word[0]}{word[1]}.png"))
    return(image1)

refreshcount = 0

def mainwindow():
    global word
    global image1
    win = Window()
    win.size = (400,400)
    imagelabel = tk.Label(win.root,image=image1)
    imagelabel.pack()
    label = tk.Label(win.root, text=word[0]+" "+word[1] , font= "comic 20 bold")
    label.pack()
    label2 = tk.Label(win.root, text=word[3][0:len(word[3])-1] , font= "comic 20 bold")
    label2.pack()
    label3 = tk.Label(win.root,text = str(refreshcount))
    label3.pack()
    
    def _quit():
        root.quit()
        root.destroy()
    def refresher():
        global word
        global image1
        global refreshcount
        word = getuserdata()
        image1 = getrankimage()
        imagelabel.config(image=image1)
        label.config(text=word[0]+" "+word[1])
        label2.config(text=word[3][0:len(word[3])-1])
        label3.config(text = str(refreshcount))
        refreshcount = refreshcount+1
        win.after(120000,refresher)
    refresher()
    root.protocol("WM_DELETE_WINDOW", _quit)
    Window.launch()

def Submitbuttonfunc():
    getentries()
    getuserdata()
    getrankimage()
    mainwindow()

SubmitButton = Button(root,text="Submit",command=Submitbuttonfunc)
SubmitButton.pack()

root.mainloop()





