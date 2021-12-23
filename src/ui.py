import tkinter as tk            # Tkinter library for GUI
import random
from src.audio import *

# global variables
# size of the main window
HEIGHT = 420
WIDTH = 500

# a value, which is added when audio seconds pass by to change color of the audio pattern correspondingly
STEP = 8

class UI:

    # constructor
    def __init__(self):
        self.audio = Audio()                                # instantiate the audio
        self.window = tk.Tk()                               # to create UI window
        self.window.title("PlaySound World")                # set the window title
        self.create_canvas()                                # to create canvas of window
        self.canvas.grid(row=0, column=0, columnspan=6)     # setting up the canvas grid
        self.audio_wire()
        self.comments = tk.Label(self.window, text=" ")
        self.comments.grid(row=3, column=0, columnspan=6)
        self.audio.set_comment_label(self.comments)
        self.create_progress_bar()
        self.create_comment_box()
        self.create_buttons()


    # opening a new file
    def new_file(self):
        # getting the values of the global variables
        global WIDTH
        global STEP

        # create an emtpy dictionary or refresh the previous one
        self.comment_dictionary = {}

        # set the audio seconds to 0
        self.audio.refresh_current_position()

        i = 0
        # makes the music pattern white again in case it was previously used for another file
        while i <= WIDTH:
            self.canvas.itemconfigure(str(i), fill="white")
            i = i + 1

    def audio_wire(self):
        # getting the values of the global variables
        global HEIGHT
        global WIDTH
        global STEP

        i = 0
        # creates the white music pattern as many as fits to the given with by adding STEP value
        while (i < WIDTH):
            self.canvas.create_line(i, random.randint(20, HEIGHT // 2), i,(random.randint(HEIGHT // 2, HEIGHT - 20)), fill="white", tag = str(i))
            i = i + STEP


    # creates a new canvas of the window
    def create_canvas(self):
        # getting the values of the global variables
        global HEIGHT
        global WIDTH

        # setting the background for audio pattern
        self.canvas = tk.Canvas(self.window, bg="black", width=WIDTH, height=HEIGHT)
        self.canvas.pack()
        self.audio.set_canvas(self.canvas)

    # creates the row of buttons
    def create_buttons(self):

        # Record button - opens a new pop-up window to start recording a new audio file
        button1 = tk.Button(self.window, text='Record', command=self.pop_up_window_record)
        button1.grid(row=4, column=0)

        # Select file button - opens a new pop-up window to select the file to be used by a program
        button2 = tk.Button(self.window, text='Select file', command=self.pop_up_window_play)
        button2.grid(row=4, column=1)

        # Play button - plays the loaded audio from the beginning
        button3 = tk.Button(self.window, text='Play', command=self.audio.play_audio_file)
        button3.grid(row=4, column=2)

        # Pause button - allows to pause and unpause the audio
        button4 = tk.Button(self.window, text='Pause', command=self.audio.pause_audio_file)
        button4.grid(row=4, column=3)

        # Comment button - adds the comment that is written in the input
        button5 = tk.Button(self.window, text='Comment', command=self.audio.comment_on_audio_file)
        button5.grid(row=4, column=4)

        # Quit button - closes the program
        button6 = tk.Button(self.window, text='Quit', command=self.window.destroy)
        button6.grid(row=4, column=5)

    # creates the comment box and the label next to it
    def create_comment_box(self):
        # creating an input field
        self.entry = tk.Entry(self.window)

        # positioning the input field
        self.entry.grid(row=5, column=3, columnspan=2, pady=20)

        # creating a label
        entry_label = tk.Label(self.window, text="Add comment")

        # positioning the label
        entry_label.grid(row=5, column=1, columnspan=2)
        self.audio.set_comment_box(self.entry)

    # sets up the UI for the pop-up window for recording
    def pop_up_window_record(self):
        # getting the values of the global variables
        global HEIGHT
        global WIDTH

        # setting up the pop-up and its sizes
        win = tk.Toplevel(self.window)
        win.geometry("400x200")

        # positioning the label
        tk.Label(win, text="Please, enter name of a new audio file").place(x=80, y=10)

        # creating an input field
        e = tk.Entry(win)
        e.pack()

        # positioning the input field
        e.place(x=120, y=50, height=30, width=150)

        # creating a button
        button = tk.Button(win, text='Start to record',
                           command=lambda: [self.audio.create_audio_file(e.get()), win.destroy()])
        button.pack()

        #positioning a button
        button.place(x=140, y=90, height=30, width=110)
        win.mainloop()

    # sets up the UI for the pop-up window for selecting an audio to work with
    def pop_up_window_play(self):
        # getting the values of the global variables
        global HEIGHT
        global WIDTH

        # setting up the pop-up and its sizes
        win = tk.Toplevel(self.window)
        win.geometry("400x200")

        # positioning the label
        tk.Label(win, text="Which audio file do you want to play?").place(x=90, y=10)

        # specifying the directory from which the files can be chosen
        directory = "./audio_files/"
        file_list = os.listdir(directory)

        # creating an option menu
        var = tk.StringVar(win, "Tap to choose audio")
        menu = tk.OptionMenu(win, var, *file_list)
        menu.pack()

        # positioning the option meny=u
        menu.place(x=90, y=50, height=40, width=165)

        # creating a button and assigining its functionality
        button = tk.Button(win, text='Select',
                           command=lambda: [self.audio.set_filename(var.get()), self.new_file(), win.destroy()])
        button.pack()

        # positioning the button
        button.place(x=265, y=50, height=38)

    # creates the progress bar
    def create_progress_bar(self):
        self.progress_bar = tk.Label(self.window, text=' ')
        self.progress_bar.grid(row=1, column=0, columnspan=6)
        self.audio.set_progress_bar(self.progress_bar)
