import os
from tkinter import *
from tkinter import filedialog
from pygame import mixer

root = Tk()
root.title('Music Player')
root.geometry('920x600+290+85')
root.configure(background='#0f1a2b')
root.resizable(False, False)

mixer.init()


def addMusic():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
            if song.endswith('.mp3'):
                playList.insert(END, song)


def playMusic():
    music_name = playList.get(ACTIVE)
    print(music_name[0:-4])
    mixer.music.load(playList.get(ACTIVE))
    mixer.music.play()


image_icon = PhotoImage(file='images/logo.png')
root.iconphoto(False, image_icon)

top = PhotoImage(file='images/top.png')
Label(root, image=top, bg='#0f1a2b').pack()

logo = PhotoImage(file='images/logo.png')
Label(root, image=logo, bg='#0f1a2b', bd=0).place(x=70, y=115)

buttonPlay = PhotoImage(file='images/play.png')
Button(root, image=buttonPlay, bg='#0f1a2b', bd=0,
       command=playMusic).place(x=100, y=400)

buttonStop = PhotoImage(file='images/stop.png')
Button(root, image=buttonStop, bg='#0f1a2b', bd=0,
       command=mixer.music.stop).place(x=30, y=500)

buttonResume = PhotoImage(file='images/resume.png')
Button(root, image=buttonResume, bg='#0f1a2b', bd=0,
       command=mixer.music.unpause).place(x=115, y=500)

buttonPause = PhotoImage(file='images/pause.png')
Button(root, image=buttonPause, bg='#0f1a2b', bd=0,
       command=mixer.music.pause).place(x=200, y=500)

menu = PhotoImage(file='images/menu.png')
Label(root, image=menu, bg='#0f1a2b').pack(padx=10, pady=50, side=RIGHT)

frame_music = Frame(root, bd=2, relief=RIDGE)
frame_music.place(x=330, y=350, width=560, height=200)

Button(root, text='Open Folder', width=15, height=2,
       font=('arial', 10, 'bold'), fg='black', bg='#21b3de', command=addMusic).place(x=330, y=300)

scroll = Scrollbar(frame_music)
playList = Listbox(frame_music, width=100, font=('arial', 10), bg='#000000', fg='white',
                   selectbackground='lightblue', cursor='hand2', bd=0, yscrollcommand=scroll.set)
scroll.config(command=playList.yview)
scroll.pack(side=RIGHT, fill=Y)
playList.pack(side=LEFT, fill=BOTH)

root.mainloop()
