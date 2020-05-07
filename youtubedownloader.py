#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/5 上午 11:37
# @Author : condal36
# @Site : 
# @File : youtubedownloader.py
# @Software: PyCharm
import tkinter as tk
from tkinter import messagebox
import ytube_module as m
from pytube import YouTube
import threading

#button event
def click_func():
    url=yt_url.get()
    try:
        YouTube(url)
    except:
        messagebox.showerror("錯誤","pytube不支援此影片或網址錯誤")
        return
    #成功,開始下載
    urls=m.get_urls(url)
    if urls and messagebox.askyesno("確認方塊","下載清單中所有影片?"):
        print("開始下載")
        for u in urls:
            threading.Thread(target=m.start_dload,args=(u,listbox)).start()
    else:
        yt=YouTube(url)
        if messagebox.askyesno("確認方塊",f"是否下載{yt.title}影片?"):
            threading.Thread(target=m.start_dload,args=(url,listbox)).start()
        else:
            print("取消下載")
#主視窗
window = tk.Tk()
window.geometry("640x480")
window.title("Youtube fast Downloader")
# frame
input_fm = tk.Frame(window, bg="red",
                    width=640, height=120)
# frame pack
input_fm.pack()
#frame label
#label
lb=tk.Label(input_fm,
            bg="red", fg="white", text="請輸入youtube網址",font=("細明體",30),padx=50,pady=80)
lb.place(rely=0.25,relx=0.5,anchor="center")
#Entry
yt_url=tk.StringVar()
entry=tk.Entry(input_fm, textvariable=yt_url, width=50)
entry.place(rely=0.5,relx=0.5,anchor="center")
#button
tkstr=tk.StringVar()
tkstr.set("下載影片")
btn=tk.Button(input_fm, textvariable=tkstr, font=("細明體",10),command=click_func)
btn.place(rely=0.5,relx=0.85,anchor="center")

#Downframe
dow_frame=tk.Frame(window,width=640,height=420-120)
dow_frame.pack()
#label at downframe
lb=tk.Label(dow_frame,text="下載狀態",fg="black",font=("新細明體",10))
lb.place(rely=0.05,relx=0.5,anchor="center")
#ListBox
listbox=tk.Listbox(dow_frame,width=65,height=15)
listbox.place(rely=0.5,relx=0.5,anchor="center")

#捲動軸
sbar=tk.Scrollbar(dow_frame)
sbar.place(rely=0.5,relx=0.87,anchor="center",relheight=0.7)

#link listbox and sbar
listbox.config(yscrollcommand=sbar.set)
sbar.config(command=listbox.yview)

window.mainloop()