import tkinter as tk
import random
from src.audio import *

HEIGHT = 420
WIDTH = 500
STEP = 8

class UI:

    def __init__(self):
        self.audio = Audio()
        self.window = tk.Tk()  # to create UI window
        self.window.title("PlaySound World")
        self.create_canvas()  # to create canvas of window
        self.canvas.grid(row=0, column=0, columnspan=6)
        self.audio_wire()
        self.comments = tk.Label(self.window, text=" ")
        self.comments.grid(row=3, column =0, columnspan=6)
        self.audio.set_comment_label(self.comments)
        self.create_progress_bar()
        self.create_comment_box()
        self.create_buttons()


    def new_file(self):
        global WIDTH
        global STEP

        self.comment_dictionary = {}
        self.audio.refresh_current_position()

        i = 0
        while i <= WIDTH:
            self.canvas.itemconfigure(str(i), fill="white")
            i = i + 1

    def audio_wire(self):
        global HEIGHT
        global WIDTH
        global STEP

        i = 0
        while (i < WIDTH):
            self.canvas.create_line(i, random.randint(20, HEIGHT // 2), i,(random.randint(HEIGHT // 2, HEIGHT - 20)), fill="white", tag = str(i))
            i = i + STEP


    # Function to create new canvas of window
    def create_canvas(self):
        global HEIGHT
        global WIDTH

        self.canvas = tk.Canvas(self.window, bg="black", width=WIDTH, height=HEIGHT)
        self.canvas.pack()
        self.audio.set_canvas(self.canvas)


    def create_buttons(self):
        button1 = tk.Button(self.window, text='Record', command=self.pop_up_window_record)
        button1.grid(row=4, column=0)

        button2 = tk.Button(self.window, text='Select file', command=self.pop_up_window_play)
        button2.grid(row=4, column=1)

        button3 = tk.Button(self.window, text='Play', command=self.audio.play_audio_file_new)
        button3.grid(row=4, column=2)

        button4 = tk.Button(self.window, text='Pause', command=self.audio.pause_audio_file)
        button4.grid(row=4, column=3)

        button5 = tk.Button(self.window, text='Comment', command=self.audio.comment_on_audio_file)
        button5.grid(row=4, column=4)

        button6 = tk.Button(self.window, text='Quit', command=self.window.destroy)
        button6.grid(row=4, column=5)

    def create_comment_box(self):
        self.entry = tk.Entry(self.window)
        self.entry.grid(row=5, column=3, columnspan=2, pady=20)
        entry_label = tk.Label(self.window, text="Add comment")
        entry_label.grid(row=5, column=1, columnspan=2)
        self.audio.set_comment_box(self.entry)

    def pop_up_window_record(self):
        global HEIGHT
        global WIDTH

        win = tk.Toplevel(self.window)
        win.geometry("400x200")

        tk.Label(win, text="Please, enter name of a new audio file").place(x=80, y=10)
        e = tk.Entry(win)
        e.pack()
        e.place(x=120, y=50, height=30, width=150)
        button = tk.Button(win, text='Start to record',
                           command=lambda: [self.audio.create_audio_file(e.get()), win.destroy()])
        button.pack()
        button.place(x=140, y=90, height=30, width=110)
        win.mainloop()

    def pop_up_window_play(self):
        global HEIGHT
        global WIDTH

        win = tk.Toplevel(self.window)
        win.geometry("400x200")

        tk.Label(win, text="Which audio file do you want to play?").place(x=90, y=10)

        directory = "./audio_files/"
        file_list = os.listdir(directory)
        print(file_list)

        var = tk.StringVar(win, "Tap to choose audio")
        menu = tk.OptionMenu(win, var, *file_list)
        menu.pack()
        menu.place(x=90, y=50, height=40, width=165)
        button = tk.Button(win, text='Select',
                           command=lambda: [self.audio.set_filename(var.get()), self.new_file(), win.destroy()])
        button.pack()
        button.place(x=265, y=50, height=38)


    def create_progress_bar(self):
        self.progress_bar = tk.Label(self.window, text=' ')
        self.progress_bar.grid(row=1, column=0, columnspan=6)
        self.audio.set_progress_bar(self.progress_bar)
