import tkinter as tk              # Tkinter library for GUI
import sounddevice as sd          # SoundDevice library to record the audio
import pygame as pg               # PyGame library to manipulate the audio files
from pydub import AudioSegment    # PyDub library to take .wav files
import scipy.io.wavfile as wf     # Scipy library to manipulate the .wav files
import os                         # to work with directories
from mutagen.mp3 import MP3       # to take the duration of the .mp3 files
import json                       # to convert dictionaries into the JSON format and store them into the .json files

# global variables
# size of the main window
HEIGHT = 300
WIDTH = 500

# a value, which is added when audio seconds pass by to change color of the audio pattern correspondingly
STEP = 8

class Audio:

    # constructor
    def __init__(self):
        pg.init()
        self.pause = True
        self.filename = ""
        self.comment_dictionary = {}

    # sets the audio file name
    def set_filename(self, filename):
        self.filename = filename

        # it is necessary to stop the previous audio completely before opening a new recording
        pg.mixer.music.stop()
        self.load_audio_file()

    # sets the audio seconds to 0
    def refresh_current_position(self):
        self.current_position = -1

    # gets the current second of the playing audio
    def get_current_position(self):
        return int(pg.mixer.music.get_pos() / 1000) # turning milliseconds to seconds

    # gets the duration of the current audio
    def get_duration(self):
        self.duration = (MP3("audio_files/" + self.filename)).info.length
        return int(self.duration)

    # sets the audio progress bar
    def set_progress_bar(self, progress_bar):
        self.progress_bar = progress_bar

    # sets the given comments as a comment label
    def set_comment_label(self, comments):
        self.comment_label = comments

    # sets the comment from the input
    def set_comment_box(self, entry):
        self.comment_entry = entry

    # sets the main canvas
    def set_canvas(self, canvas):
        self.canvas = canvas

    # load the selected audio file from the directory
    def load_audio_file(self):
        pg.mixer.music.load("audio_files/" + self.filename)
        pg.mixer.music.rewind()

    # play the audio file
    def play_audio_file(self):
        pg.mixer.music.play(1, 0.0)
        self.pause = False
        self.audio_progress()

    # pause and unpause the audio file
    def pause_audio_file(self):
        if self.pause:
            pg.mixer.music.unpause()
            self.pause = False
        else:
            pg.mixer.music.pause()
            self.pause = True


    # creates the new file after the recording
    def create_audio_file(self, filename):
        duration = 60       # setting the time of the recording
        fs = 44100          # setting the frequency (for 2 channels together)

        # setting the default input channels
        sd.default.channels = 2

        # taking the recording file
        my_recording = sd.rec(duration * fs)
        sd.wait()

        # storing the recording as a wav file
        wf.write("audio_files/" + filename + ".wav", fs, my_recording)
        sound = AudioSegment.from_wav("audio_files/" + filename + ".wav")

        # converting the wav file to mp3 format and deleting the one in wav format
        sound.export("audio_files/" + filename + ".mp3", format='mp3')
        os.remove("audio_files/" + filename + ".wav")


    # puts comments to the seconds of the audio
    def comment_on_audio_file(self):

        # if the .json file of the audio already exists, the program should read the existing comments for the given file
        if os.path.exists("audio_comments/" + self.filename + ".json"):
            with open("audio_comments/" + self.filename + ".json", "r") as json_file:
                # assingns the values from .json file to the dictionary
                self.comment_dictionary = json.load(json_file)

        # if the second already has at least one comment, appent to the comments array
        if str(self.current_position) in self.comment_dictionary.keys():
            self.comment_dictionary[str(self.current_position)].append(self.comment_entry.get())
        else:
            # if not, create a first array value with the first entered comment
            self.comment_dictionary[str(self.current_position)] = [self.comment_entry.get()]

        # write the comment to the audio file and add it to the corresponding .json file
        with open("audio_comments/" + self.filename + ".json", "w") as json_file:
            json.dump(self.comment_dictionary, json_file)
        self.comment_entry.delete(0, tk.END)
        json_file.close()


    def audio_progress(self):
        # get the current second of the audio
        self.current_position = int(pg.mixer.music.get_pos() / 1000)  # convert milliseconds to seconds
        # display the current second out of the total seconds
        self.progress_bar.config(text=str(self.current_position) + "|" + str(self.get_duration()))

        # if the .json file of the audio already exists, the program should read the existing comments for the given file on specific seconds
        if os.path.exists("audio_comments/" + self.filename + ".json"):
            with open("audio_comments/" + self.filename + ".json", "r") as json_file:
                temp_dict = json.load(json_file)
                # if the second has a comment then display it
                if str(self.current_position) in temp_dict.keys():
                    self.comment_label.config(text=temp_dict.get(str(self.current_position)))
                else:
                    # or display nothing
                    self.comment_label.config(text=" ")
            json_file.close()

        # chaging the progress bar every passing second
        self.progress_bar.after(1000, self.audio_progress)
        self.progress_bar.after(1000, self.audio_progress_animation_color_change)


    # sets up the changing animation for progress bar
    def audio_progress_animation_color_change(self):
        # getting the values of the global variables
        global WIDTH
        global STEP

        # get total duration of the audio
        duration = self.get_duration()

        # calculate the changing rate
        change_second = WIDTH // duration

        # get the current position
        current_progress = self.current_position

        # calculate the change of the position with steps
        change_position = change_second * current_progress // STEP

        i = 0
        # change the color of the progress bar as the position value changes with seconds
        while(i <= change_position):
            self.canvas.itemconfigure(str(i), fill = "#C21B5F")
            i = i + 1





