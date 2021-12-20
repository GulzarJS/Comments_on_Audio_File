import os
import tkinter as tk

from src.audio import Audio

HEIGHT = 200
WIDTH = 400

class UI:

    def __init__(self):
        self.audio = Audio()
        self.window = tk.Tk()  # to create UI window
        self.window.title("PlaySound World")
        self.create_canvas()  # to create canvas of window
        self.canvas.grid(row=0, column=0, columnspan=3)
        self.create_buttons()
        self.info = tk.Label(self.window, text="")  # information label of game
        self.info.grid(row=1, column=0, columnspan=3)



    # Function to create new canvas of window
    def create_canvas(self):
        global HEIGHT
        global WIDTH

        self.canvas = tk.Canvas(self.window, bg="navy", width=WIDTH, height=HEIGHT)
        self.canvas.pack()

    def create_buttons(self):
        button1 = tk.Button(self.window, text='Record', command= self.pop_up_window_record)
        button1.grid(row=4, column=0)

        button2 = tk.Button(self.window, text='Play', command=self.pop_up_window_play)
        button2.grid(row=4, column=1)

        button3 = tk.Button(self.window, text='Quit', command=self.window.destroy)
        button3.grid(row=4, column=2)

    def pop_up_window_record(self):
        global HEIGHT
        global WIDTH

        win = tk.Toplevel(self.window)
        win.geometry("400x200")
        #
        # child_canvas = tk.Canvas(win, bg="white", width=WIDTH, height=HEIGHT)
        # child_canvas.pack()

        tk.Label(win, text="Please, enter name of new audio file").place(x=50, y=50)
        e = tk.Entry(win)
        e.pack()
        button = tk.Button(win, text = 'Start to record' , command = lambda:[self.audio.create_audio_file(e.get()), win.destroy()])
        button.pack()
        win.mainloop()


    def pop_up_window_play(self):
            global HEIGHT
            global WIDTH

            win = tk.Toplevel(self.window)
            win.geometry("400x200")

            tk.Label(win, text="Which audio file do you want to play?").place(x=50, y=50)

            directory = "./audio_files/"
            file_list = os.listdir(directory)
            print(file_list)
            #
            # options = tk.StringVar()
            var = tk.StringVar(win)
            menu = tk.OptionMenu(win,var, *file_list )
            menu.pack()
            button = tk.Button(win, text = 'Select' , command = lambda:[self.audio.play_audio_file(var.get()), win.destroy()])
            button.pack()



ui = UI()
ui.window.mainloop()