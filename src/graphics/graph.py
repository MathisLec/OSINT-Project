import tkinter as tk

BACKGROUND_COLOR = "#34495e"
BUTTON_COLOR = "#bdc3c7"
LABEL_COLOR = "#ecf0f1"

def buttonFactory(frame,comm,txt):
    return tk.Button(frame,relief="flat",text=txt,bg=BUTTON_COLOR,font=("Arial Black",20),command=comm,height=2,width=10)

def startButtonFactory(frame, comm, txt):
    button = buttonFactory(frame, comm, txt)
    button["fg"] = "green"
    button["activeforeground"] = "green"
    return button

def say_hi():
    print("hi there, everyone!")
    
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
dns_button = buttonFactory(menuButton_frame, say_hi, "DnsScan")
dns_button.pack(side="left")

#Shodan button
shodan_button = buttonFactory(menuButton_frame, say_hi, "Shodan")
shodan_button.pack(side="left")

#TheHarvester button
TH_button = buttonFactory(menuButton_frame, say_hi, "TheHarvester")
TH_button.pack(side="left")

#URLScan button
URLScan_button = buttonFactory(menuButton_frame, say_hi, "URLScan")
URLScan_button.pack(side="left")

#Entry for the URL
url_entry = tk.Entry(app,width=30,font=("Arial Black",20))
url_entry.focus_set()
url_entry.pack(expand=1)

#Start button
start_button = startButtonFactory(app, say_hi, "Start")
start_button.pack(expand=1)

app.mainloop()