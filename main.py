from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import filedialog
from tkinter import colorchooser
from tkinter import ttk
import webbrowser
import os
from pytube import YouTube
import requests
import moviepy.editor as mpez
itag_audio="251"
itag144="160"
itag240="133"
itag360="18"
itag480="135"
itag720="22"
itag1080="137"
itag1440="271"
itag2160="313"
def takefrompc():
    PostionPc.delete(0,END)
    PostionPc.insert(END,filedialog.askdirectory())
def typesandqualities():
    Link = link.get();Pc = pc.get()
    valid = Link[0:23]
    if len(Link) == 0:
        messagebox.showerror('error', 'input the link please')
        com.config(value=(""))
        com.set('')
        com.config(state=DISABLED)
    elif valid != 'https://www.youtube.com':
        messagebox.showerror('error',"input a youtube link in form http://")
        com.config(value=(""))
        com.set('')
        com.config(state=DISABLED)
    elif len(Link) < len(valid) :
        messagebox.showerror('error',"the link isn't work")
        com.config(value=(""))
        com.set('')
        com.config(state=DISABLED)
    elif requests.get(Link).ok:
        video=YouTube(Link)
        com.config(state=NORMAL)
        if video.streams.get_by_itag(itag480)!=None:
            if video.streams.get_by_itag(itag720)!=None:
                if video.streams.get_by_itag(itag1080)!=None:
                    if video.streams.get_by_itag(itag1440)!=None:
                        if video.streams.get_by_itag(itag2160)!=None:
                             com.config(value=("144p " + video.streams.get_by_itag(itag144).filesize,"240p " + video.streams.get_by_itag(itag240).filesize,"360p" + video.streams.get_by_itag(itag360).filesize,"480p " + video.streams.get_by_itag(itag480).filesize,"720p " + video.streams.get_by_itag(itag720).filesize,"1080p","1440p","2160p"))
                        else:com.config(value=("144p " + video.streams.get_by_itag(itag144).filesize,"240p " + video.streams.get_by_itag(itag240).filesize,"360p" + video.streams.get_by_itag(itag360).filesize,"480p " + video.streams.get_by_itag(itag480).filesize,"720p " + video.streams.get_by_itag(itag720).filesize,"1080p " +video.streams.get_by_itag(itag1080).filesize,"1440p "+video.streams.get_by_itag(itag1440).filesize))
                    else:com.config(value=("144p " + video.streams.get_by_itag(itag144).filesize,"240p " + video.streams.get_by_itag(itag240).filesize,"360p" + video.streams.get_by_itag(itag360).filesize,"480p " + video.streams.get_by_itag(itag480).filesize,"720p " + video.streams.get_by_itag(itag720).filesize,"1080p " +video.streams.get_by_itag(itag1080).filesize))
                else:com.config(value=("144p " + video.streams.get_by_itag(itag144).filesize,"240p " + video.streams.get_by_itag(itag240).filesize,"360p" + video.streams.get_by_itag(itag360).filesize,"480p " + video.streams.get_by_itag(itag480).filesize,"720p " + video.streams.get_by_itag(itag720).filesize))
            else:com.config(value=("144p " + video.streams.get_by_itag(itag144).filesize,"240p " + video.streams.get_by_itag(itag240).filesize,"360p" + video.streams.get_by_itag(itag360).filesize,"480p " + video.streams.get_by_itag(itag480).filesize))
        else:com.config(value=("144p " + video.streams.get_by_itag(itag144).filesize,"240p " + video.streams.get_by_itag(itag240).filesize,"360p" + video.streams.get_by_itag(itag360).filesize))
        com.set('360')


def download():
    Link=link.get();Quality=quality.get();Type=TypeV.get();Pc=pc.get()
    valid= Link[0:23]
    if  len(Pc)==0 :
        messagebox.showerror('error','input the link please')
    if len(Quality) ==0 :
        messagebox.showerror('error', 'unchoosen quality of video')
    else:
        video=YouTube(Link)
        if Quality=="720p":
            video.streams.get_by_itag(itag720).download(Pc)
        elif Quality=="360p":
            video.streams.get_by_itag(itag360).download(Pc)
        else:
            videotitle=video.title
            video.streams.get_by_itag(itag_audio).download(Pc,filename='audio')
            if Quality=="240p":
                video.streams.get_by_itag(itag240).download(Pc,filename="V")
            elif Quality=="144p":
                video.streams.get_by_itag(itag144).download(Pc,filename="V")
            elif Quality=="480p":
                video.streams.get_by_itag(itag480).download(Pc,filename="V")
            elif Quality=="1080p":
                video.streams.get_by_itag(itag1080).download(Pc,filename="V")
            elif Quality=="2160p":
                video.streams.get_by_itag(itag2160).download(Pc,filename="V")
            elif Quality=="1440p":
                video.streams.get_by_itag(itag1440).download(Pc,filename="V")
            clip =mpe.VideoFileClip(fr'{Pc}\V.mp4')
            audio=mpe.AudioFileClip(fr"{Pc}\audio.webm")
            finalclip=clip.set_audio(audio)
            finalclip.write_videofile(fr"{Pc}\final.mp4")
            clip=os.path.join(Pc,"V.mp4")
            audio=os.path.join(Pc,"audio.webm")
            os.remove(clip)
            os.remove(audio)
            videotitle="download"
            clip=Pc+"\\"+videotitle+".mp4"
            # print(clip)
            os.rename(fr"{Pc}\final.mp4",clip)






t=Tk()
t.title("Youtube Downloader")
t.geometry('500x400+200+200')
icon=t.iconbitmap('2.ico')
link=StringVar()
quality=StringVar()
TypeV=StringVar()
pc=StringVar()

where=" "
PostionPc=Entry(textvariable=pc,width=40)
PostionPc.grid(row=1,column=0,padx=(50,0),pady=(35,5))
PostionPc.insert(END,"C:/Users/DreamOnline/Downloads")
inpc=Button(cursor="hand2",bitmap="gray25",command=takefrompc)
inpc.place(x=303,y=33)

text=Entry(textvariable=link,width=40)
text.grid(row=2,column=0,padx=(50,0))
#label1=Label(text='input your link',fg='black')
#label1.grid(row=2,column=1,padx=(10,0),pady=(20))

sure=Button(text="input the link and click",cursor="hand2",command=typesandqualities)
sure.grid(row=2,column=1,padx=(10,0),pady=(20))

com=ttk.Combobox(t)
com.config(textvariable=quality,state=DISABLED)        #value=('1280','720','480','360','240','144')
                                    #com.set('480');
com.grid(row=3,column=0)
labeltrash=Label(text='')
labeltrash.grid(row=3,column=1)
label2=Label(text='Quality of video',fg='black')
label2.place(x=230,y=123)
# spin=ttk.Spinbox(t)
# spin.config(value=('mp4','voice','video without audio'),textvariable=TypeV);spin.set('mp4')
# spin.grid(row=4,column=0,pady=(20,0))
# label3=Label(text='Type of video',fg='black')
# label3.place(x=230,y=160)
#print(colorchooser.askcolor())

b=Button(text='Download',bg='#00d500',activebackground="#00b700",bd=5,command=lambda :download())
b.place(x=200,y=210)

progress=ttk.Progressbar(t)
progress.config(length=250)
progress.place(x=110,y=260)
t.mainloop()
# video=YouTube('https://www.youtube.com/watch?v=WlRB1VyMB_A')
# video=YouTube('https://www.youtube.com/watch?v=uGf6Y2jrSMY')
#video=YouTube('https://www.youtube.com/watch?v=H6O9KlknPe8')
#video=YouTube('https://www.youtube.com/watch?v=m0jyjCyFw_c')
# print(video.streams.get_by_itag(itag1080))
# print(video.streams.get_lowest_resolution())
# for s in video.streams:
#     print(s)
# print(video.streams.get_by_itag(itag1080))
# import moviepy.editor as mpe
# go=r'F:\New folder'
# clip =mpe.VideoFileClip(fr'{go}\a.mp4')
# audio=mpe.AudioFileClip(fr"{go}\audio.webm")
# finalclip=clip.set_audio(audio)
# finalclip.write_videofile(fr"{go}\final.mp4")