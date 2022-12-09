import tkinter as tk

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

is_On = {"DnsScan": 0, "Shodan":0, "TheHarvester":0, "URLScan":0}

def buttonFactory(frame,comm,txt):
    return tk.Button(frame,relief="flat",text=txt,bg=DEFAULT_BUTTON_COLOR,font=("Arial Black",20),command=comm,height=2,width=10)

def menuButtonFactory(frame,txt):
    button = buttonFactory(frame, lambda : switchButton(button), txt)
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

# app frame
app = tk.Tk()
app.geometry("800x800")
app.title("OSINT tool")
app.configure(bg=BACKGROUND_COLOR)

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
url_entry = tk.Entry(app,width=30,font=("Arial Black",20))
url_entry.focus_set()
url_entry.pack(expand=1)

#Start button
start_button = startButtonFactory(app, lambda: print("Hello"), "Start")
start_button.pack(expand=1)

app.mainloop()