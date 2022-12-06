import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # DNSSCAN
        self.dnsscan_button = tk.Button(self)
        self.dnsscan_button["text"] = "DnsScan"
        self.dnsscan_button["command"] = self.say_hi
        self.dnsscan_button.pack(side="top")
        # SHODAN
        self.shodan_button = tk.Button(self)
        self.shodan_button["text"] = "Shodan"
        self.shodan_button["command"] = self.say_hi
        self.shodan_button.pack(side="top")
        # THEHARVESTER
        self.theharvester_button = tk.Button(self)
        self.theharvester_button["text"] = "TheHarvester"
        self.theharvester_button["command"] = self.say_hi
        self.theharvester_button.pack(side="top")
        # URLSCAN
        self.urlscan_button = tk.Button(self)
        self.urlscan_button["text"] = "URLScan"
        self.urlscan_button["command"] = self.say_hi
        self.urlscan_button.pack(side="top")
        # Domain Entry
        self.domain = tk.Entry(self, textvariable="hello")
        self.domain.focus_set()
        self.domain.pack()
        # Start Button
        self.start_button = tk.Button(self)
        self.start_button["text"] = "Start"
        self.start_button["fg"] = "green"
        self.start_button["command"] = self.say_hi
        self.start_button.pack(side="bottom")
        # Quit button
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
root.geometry("300x200")
app = Application(master=root)
app.mainloop()