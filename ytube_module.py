#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/7 上午 11:11
# @Author : condal36
# @Site : 
# @File : ytube_module.py
# @Software: PyCharm
from pytube import YouTube
import os
from bs4 import BeautifulSoup
import requests
import threading
import tkinter as tk

def get_urls(url):
    urls = []
    if "&list=" not in url: return urls  # 單一影片判斷式
    response = requests.get(url)  # GET
    if response.status_code != 200:
        print("請求失敗")
        return
    # 請求成功，解析網頁
    bs = BeautifulSoup(response.text, "lxml")
    a_list = bs.find_all("a")  # 所有<a>標籤
    base = "https://youtube.com/"
    for a in a_list:
        href = a.get('href')
        url = base + href
        if ("&index=" in url) and (url not in urls):
            urls.append(url)
    return urls
lock=threading.Lock()
def start_dload(url,listbox):
    yt=YouTube(url)
    name=yt.title
    lock.acquire()
    no=listbox.size()
    listbox.insert(tk.END, f"{no:02d}:{name}下載中")
    print("插入:",no,name)
    lock.release()
    yt.streams.first().download("./videos")
    lock.acquire()
    print("更新:",no,name)
    listbox.delete(no)
    listbox.insert(no,f"{no:02d}:*{name}")
    lock.release()
if __name__=="__main__":
    while True:
        print("Welcome to youtube downloader！！！")
        urla=input()
        urlb=get_urls(urla)
        print(urlb)
        for a in urlb:
            try:
                yt=YouTube(a)
                print("開始下載")
                if os.path.isdir("./videos"):
                    yt.streams.first().download("./videos")
                    print(f"下載完成{yt.title}")
                else:
                    os.mkdir("./videos")
                    yt.streams.first().download("./videos")
                    print(f"下載完成{yt.title}")
            except:
                pass