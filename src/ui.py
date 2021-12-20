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
        self.canvas.grid(row=0, column=0, columnspan=2)
        self.create_buttons()
        self.info = tk.Label(self.window, text="")  # information label of game
        self.info.grid(row=1, column=0, columnspan=2)



    # Function to create new canvas of window
    def create_canvas(self):
        global HEIGHT
        global WIDTH

        self.canvas = tk.Canvas(self.window, bg="navy", width=WIDTH, height=HEIGHT)
        self.canvas.pack()

    def create_buttons(self):
        button2 = tk.Button(self.window, text='Record', command= self.pop_up_window)
        button2.grid(row=4, column=0)

        # button2 = tk.Button(self.window, text='Play', command=self.audio.play_audio_file("newfile"))
        # button2.grid(row=4, column=1)

        button = tk.Button(self.window, text='Quit', command=self.window.destroy)
        button.grid(row=4, column=2)

    def pop_up_window(self):
        global HEIGHT
        global WIDTH

        win = tk.Toplevel(self.window)
        # win.geometry("400x200")

        child_canvas = tk.Canvas(win, bg="white", width=WIDTH, height=HEIGHT)
        child_canvas.pack()

        tk.Label(child_canvas, text="Please, enter name of new audio file").place(x=50, y=50)
        e = tk.Entry(child_canvas)
        e.pack()
        button = tk.Button(win, text = 'Start to record' , command = lambda:[self.audio.create_audio_file(e.get()), win.destroy()])
        button.pack()



ui = UI()
ui.window.mainloop()