from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import youtube_dl
import ffmpeg
import sys

root=Tk()
root.resizable(0,0)

def save():
    #messagebox.showinfo('Wybór', 'Wybierz folder docelowy')
    messagebox.showinfo('Folder Selection', 'Select download folder')
    directory=filedialog.askdirectory()
    #directory = 'downloaded_music'
    ydl_opts = {

    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([e1.get()])
    #messagebox.showinfo('Zakonczone','Pobieranie zakonczone')
    messagebox.showinfo('Success','Download completed')

def exit():
    sys.exit()

if __name__ == '__main__':
    root.title('Youtube downloader')
    #l1=Label(root,text='Wpisz adres url filmu Youtube',font=20)
    l1=Label(root,text='Download MP3 from Youtube video',font=20)
    l1.pack()
    e1=Entry(root,width=50)
    e1.pack()
    #b1=Button(root,text='Pobierz',width=7,height=2,command=save)
    b1=Button(root,text='Download',width=7,height=2,command=save)
    b1.pack(side=LEFT)
    #b2=Button(root,text='Wyjdź',command=exit,width=7,height=2)
    b2=Button(root,text='Exit',command=exit,width=7,height=2)
    b2.pack(side=RIGHT)
    root.mainloop()