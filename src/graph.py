#!/usr/bin/env python3
# -*- coding:Utf-8 -*-
import tkinter as tk
import tkinter.scrolledtext
import os
import main

BACKGROUND_COLOR = "#34495e"

DEFAULT_BUTTON_COLOR = "#bdc3c7"

ACTIV_BUTTON_COLOR = "#2ecc71"
ACTIV_FONT_COLOR = "#42e085"
ACTIV_BUTTON_COLOR_OVER = "#42e085"
ACTIV_FONT_COLOR_OVER = "#56f499"

DEACTIV_BUTTON_COLOR = "#c0392b"
DEACTIV_FONT_COLOR = "#fb6050"
DEACTIV_BUTTON_COLOR_OVER = "#d44d3f"
DEACTIV_FONT_COLOR_OVER = "#ff7464"

LABEL_COLOR = "#ecf0f1"

TEXT_BACKGROUND_COLOR = "#2c3e50"

SCAN_PATH = ""

is_On = {"DnsScan": 0, "Shodan":0, "TheHarvester":0, "URLScan":0}

def cleanCanva(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def buttonFactory(frame,comm,txt):
    return tk.Button(frame,relief="flat",text=txt,bg=DEFAULT_BUTTON_COLOR,font=("Arial Black",20),command=comm,height=2,width=10)

def menuButtonFactory(frame,txt):
    button = buttonFactory(frame, lambda : switchButton(button), txt)
    button["bg"] = DEACTIV_BUTTON_COLOR
    button["fg"] = DEACTIV_FONT_COLOR
    button["activebackground"] = DEACTIV_BUTTON_COLOR_OVER
    button["activeforeground"] = DEACTIV_FONT_COLOR_OVER
    return button

def logMenuButtonFactory(frame, text_area, txt):
    button = buttonFactory(frame, lambda : switchLogButton(frame, text_area, button), txt)
    button["bg"] = DEACTIV_BUTTON_COLOR
    button["fg"] = DEACTIV_FONT_COLOR
    button["activebackground"] = DEACTIV_BUTTON_COLOR_OVER
    button["activeforeground"] = DEACTIV_FONT_COLOR_OVER
    return button

def startButtonFactory(frame, comm, txt):
    button = buttonFactory(frame, comm, txt)
    button["bg"] = ACTIV_BUTTON_COLOR
    button["activebackground"] = ACTIV_BUTTON_COLOR_OVER
    button["fg"] = "#ecf0f1"
    button["activeforeground"] = "#ecf0f1"
    return button

def switchButton(button):
    if is_On[button["text"]] == 0:
        button["bg"] = ACTIV_BUTTON_COLOR
        button["fg"] = ACTIV_FONT_COLOR
        button["activebackground"] = ACTIV_BUTTON_COLOR_OVER
        button["activeforeground"] = ACTIV_FONT_COLOR_OVER
        is_On[button["text"]] = 1
    else:
        button["bg"] = DEACTIV_BUTTON_COLOR
        button["fg"] = DEACTIV_FONT_COLOR
        button["activebackground"] = DEACTIV_BUTTON_COLOR_OVER
        button["activeforeground"] = DEACTIV_FONT_COLOR_OVER
        is_On[button["text"]] = 0

def switchLogButton(frame, text_area, button):
    for widget in frame.winfo_children():
        if widget != button:
            if is_On[widget["text"]] == 1:
                widget["bg"] = DEACTIV_BUTTON_COLOR
                widget["fg"] = DEACTIV_FONT_COLOR
                widget["activebackground"] = DEACTIV_BUTTON_COLOR_OVER
                widget["activeforeground"] = DEACTIV_FONT_COLOR_OVER
                is_On[widget["text"]] = 0
        else:
            if is_On[button["text"]] == 0:
                button["bg"] = ACTIV_BUTTON_COLOR
                button["fg"] = ACTIV_FONT_COLOR
                button["activebackground"] = ACTIV_BUTTON_COLOR_OVER
                button["activeforeground"] = ACTIV_FONT_COLOR_OVER
                is_On[button["text"]] = 1

                text_area.delete('1.0',tk.END)
                printfile(text_area, button["text"])

def printfile(text_area, file):
    scan_path = os.path.join(SCAN_PATH, file.lower()+".log")
    with open(scan_path, "r") as f:
        text_area.insert(tk.END, f.read())


def initLogMenu():
    #Log Menu Frame
    menuButton_log_frame = tk.Frame(app,bg=BACKGROUND_COLOR)
    menuButton_log_frame.pack()
    text_area = tk.scrolledtext.ScrolledText(app,height=500, width=800,font=("Arial Black",10),fg="#ecf0f1" , bg=TEXT_BACKGROUND_COLOR)
    text_area.pack(expand=1)
    #Update root buttons
    if is_On["DnsScan"]:
        dns_button = logMenuButtonFactory(menuButton_log_frame, text_area ,"DnsScan")
        switchButton(dns_button)
        dns_button.pack(side="left")
    if is_On["Shodan"]:
        shodan_button = logMenuButtonFactory(menuButton_log_frame, text_area, "Shodan")
        switchButton(shodan_button)
        shodan_button.pack(side="left")
    if is_On["TheHarvester"]:
        TH_button = logMenuButtonFactory(menuButton_log_frame, text_area, "TheHarvester")
        switchButton(TH_button)
        TH_button.pack(side="left")
    if is_On["URLScan"]:
        URLScan_button = logMenuButtonFactory(menuButton_log_frame, text_area, "URLScan")
        switchButton(URLScan_button)
        URLScan_button.pack(side="left")

def startButtonFunction(app_frame):
    cleanCanva(app_frame)
    main.launch_scans(TEXT_ENTRY.get(),is_On)
    global SCAN_PATH
    SCAN_PATH = os.path.join(os.getcwd(),"scan_"+TEXT_ENTRY.get())
    initLogMenu()


# app frame
app = tk.Tk()
app.geometry("800x800")
app.title("OSINT tool")
app.configure(bg=BACKGROUND_COLOR)

##### Main Menu #####
#label title
menu_label = tk.Label(app,text="OSINT tool",font=("Arial Black",50),bg=BACKGROUND_COLOR,fg=LABEL_COLOR)
menu_label.pack(expand=1)

#menuButton frame
menuButton_frame = tk.Frame(app,bg=BACKGROUND_COLOR)
menuButton_frame.pack(expand=1)

#DnsScan button
dns_button = menuButtonFactory(menuButton_frame, "DnsScan")
dns_button.pack(side="left")

#Shodan button
shodan_button = menuButtonFactory(menuButton_frame, "Shodan")
shodan_button.pack(side="left")

#TheHarvester button
TH_button = menuButtonFactory(menuButton_frame, "TheHarvester")
TH_button.pack(side="left")

#URLScan button
URLScan_button = menuButtonFactory(menuButton_frame, "URLScan")
URLScan_button.pack(side="left")

#Entry for the URL
TEXT_ENTRY = tk.StringVar()
url_entry = tk.Entry(app,width=30,font=("Arial Black",20), textvariable=TEXT_ENTRY)
url_entry.focus_set()
url_entry.pack(expand=1)

#Start button
start_button = startButtonFactory(app, lambda: startButtonFunction(app), "Start")
start_button.pack(expand=1)

app.mainloop()