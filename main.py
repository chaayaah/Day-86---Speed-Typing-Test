import tkinter
import tkinter as tk
import time
import random
import threading

class TypeSpeedGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Speed Typing Test App")
        self.root.geometry("800x600")

        self.texts = open("random_sentence.txt", "r").read().split("\n")
        self.frame = tk.Frame(self.root)

        self.sample_label = tk.Label(self.frame, text=random.choice(self.texts))
        self.sample_label.grid(column=0, row=0, columnspan=2, padx=5, pady=5)

        self.input_entry = tk.Entry(self.frame, width=40, font=("Helvetica", 20))
        self.input_entry.grid(column=0, row=1, columnspan=2, padx=5, pady=10)
        self.input_entry.bind("<KeyRelease>", self.start)

        self.speed_label = tk.Label(self.frame, text="SPEED: \n0.00 CPS\n0.00 WPS\n0.00 WPM", font=("Helvetica", 18))
        self.speed_label.grid(column=0, row=2, columnspan=2, padx=5, pady=10)

        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset, font=("Helvetica", 24))
        self.reset_button.grid(column=0, row=3, columnspan=2, padx=5, pady=10)

        self.frame.pack(expand=True)

        self.counter = 0
        self.running = False

        self.root.mainloop()


    def start(self, event):
        if not self.running:
            if not event.keycode in [16, 17, 18]:
                self.running = True
                t = threading.Thread(target=self.time_thread)
                t.start()
        if not self.sample_label.cget('text').startswith(self.input_entry.get()):
            self.input_entry.config(fg="red")
        else:
            self.input_entry.config(fg="black")

        if self.input_entry.get() == self.sample_label.cget('text'):
            self.running = False
            self.input_entry.config(fg="green")
            self.input_entry.config(state='disabled')

    def reset(self):
        self.running = False
        self.counter = 0
        self.speed_label.config(text="SPEED: \n0.00 CPS\n0.00 CPM")
        self.sample_label.config(text=random.choice(self.texts))
        self.input_entry.delete(0, tk.END)

    def time_thread(self):
        while self.running:
            time.sleep(0.1)
            self.counter = self.counter + 0.1
            cps = len(self.input_entry.get()) / self.counter
            cpm = cps * 60
            wps = len(self.input_entry.get().split(" ")) / self.counter
            wpm = wps * 60
            self.speed_label.config(text=f"Speed: \n{cps:.2f} CPS\n{cpm:.2f} CPM\n {wps:.2f} WPS\n{wpm:.2f} WPM")

TypeSpeedGUI()