from playsound import playsound
import sounddevice as sd
import pygame as pg
from pydub import AudioSegment
import scipy.io.wavfile as wf
import os
from mutagen.mp3 import MP3
import json

HEIGHT = 300
WIDTH = 500
STEP = 8

class Audio:

    def __init__(self):
        pg.init()
        self.pause = True
        self.filename = ""
        self.comment_dictionary = {}


    def set_filename(self, filename):
        self.filename = filename
        pg.mixer.music.stop()
        self.load_audio_file()


    def refresh_current_position(self):
        self.current_position = -1

    def get_current_position(self):
        return int(pg.mixer.music.get_pos() / 1000)

    def get_duration(self):
        self.duration = (MP3("audio_files/" + self.filename)).info.length
        return int(self.duration)

    def set_progress_bar(self, progress_bar):
        self.progress_bar = progress_bar

    def set_comment_label(self, comments):
        self.comment_label = comments

    def set_comment_box(self, entry):
        self.comment_entry = entry

    def set_canvas(self, canvas):
        self.canvas = canvas

    def load_audio_file(self):
        pg.mixer.music.load("audio_files/" + self.filename)
        # self.refresh_current_position()
        pg.mixer.music.rewind()
        print(pg.mixer.music.get_pos())

    def play_audio_file_new(self):
        pg.mixer.music.play(1, 0.0)
        self.pause = False
        self.audio_progress()

    def pause_audio_file(self):
        if self.pause:
            pg.mixer.music.unpause()
            self.pause = False
        else:
            pg.mixer.music.pause()
            self.pause = True


    def create_audio_file(self, filename):
        duration = 10
        fs = 44100

        my_recording = sd.rec(duration * fs)
        sd.wait()

        wf.write("audio_files/" + filename + ".wav", fs, my_recording)  # Save as WAV file

        sound = AudioSegment.from_wav("audio_files/" + filename + ".wav")

        sound.export("audio_files/" + filename + ".mp3", format='mp3')
        os.remove("audio_files/" + filename + ".wav")



    def comment_on_audio_file(self):

        if self.current_position in self.comment_dictionary.keys():
            self.comment_dictionary[self.current_position].append(self.comment_entry.get())
        else:
            self.comment_dictionary[self.current_position] = [self.comment_entry.get()]

        with open("audio_comments/" + self.filename + ".json", "w") as json_file:
            json.dump(self.comment_dictionary, json_file)

        json_file.close()


    def audio_progress(self):

        self.current_position = int(pg.mixer.music.get_pos() / 1000)
        self.progress_bar.config(text=str(self.current_position) + "|" + str(self.get_duration()))

        if os.path.exists("audio_comments/" + self.filename + ".json"):
            with open("audio_comments/" + self.filename + ".json", "r") as json_file:
                temp_dict = json.load(json_file)
                if str(self.current_position) in temp_dict.keys():
                    self.comment_label.config(text=temp_dict.get(str(self.current_position)))
                else:
                    self.comment_label.config(text=" ")
            json_file.close()


        self.progress_bar.after(1000, self.audio_progress)
        self.progress_bar.after(1000, self.audio_progress_animation_color_change)

    def audio_progress_animation_color_change(self):
        global WIDTH
        global STEP

        duration = self.get_duration()
        change_second = WIDTH // duration
        current_progress = self.current_position
        change_position = change_second * current_progress // STEP

        i = 0
        while(i <= change_position):
            self.canvas.itemconfigure(str(i), fill = "#C21B5F")
            i = i + 1





