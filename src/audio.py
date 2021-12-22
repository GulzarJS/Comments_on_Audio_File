from playsound import playsound
import sounddevice as sd
import soundfile as sf
import pygame as pg
from pydub import AudioSegment
import scipy.io.wavfile as wf
import os
from mutagen.mp3 import MP3
import json



class Audio:

    def __init__(self):
        self.pause = True
        self.filename = ""
        self.comment_dictionary = {}

    def set_filename(self, filename):
        self.filename = filename
        print(self.get_duration())

    # def read_audio_file(self):
    #     sound, samplerate = sf.read("audio_files/" + self.filename)
    #     return sound, samplerate

    def get_current_position(self):
        return int(pg.mixer.music.get_pos() / 1000)

    def get_duration(self):
        self.duration = (MP3("audio_files/" + self.filename)).info.length
        return int(self.duration)

    def play_audio_file(self, filename):
        playsound("audio_files/" + filename)

    def set_progress_bar(self, progress_bar):
        self.progress_bar = progress_bar

    def set_comment_label(self, comments):
        self.comment_label = comments

    def set_comment_box(self, entry):
        self.comment_entry = entry


    def play_audio_file_new(self):
        pg.init()
        pg.mixer.music.load("audio_files/" + self.filename)
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
        # sd.default.samplerate = 44100
        fs = 44100
        sd.default.channels = 2

        myrecording = sd.rec(duration * fs)
        sd.wait()

        wf.write("audio_files/" + filename + ".wav", fs, myrecording)  # Save as WAV file

        sound = AudioSegment.from_wav("audio_files/" + filename + ".wav")

        sound.export("audio_files/" + filename + ".mp3", format='mp3')
        os.remove("audio_files/" + filename + ".wav")

    def comment_on_audio_file(self):

        # json_file = self.create_JSON_file(self.filename)



        if self.current_position in self.comment_dictionary.keys():
            self.comment_dictionary[self.current_position].append(self.comment_entry.get())
        else:
            self.comment_dictionary[self.current_position] = [self.comment_entry.get()]
        # print(self.comment_dictionary)

        with open("audio_comments/" + self.filename + ".json", "w") as json_file:
            json.dump(self.comment_dictionary, json_file)

        json_file.close()


    def audio_progress(self):
        self.current_position = int(pg.mixer.music.get_pos() / 1000)
        self.progress_bar.config(text=str(self.current_position) + "|" + str(self.get_duration()))
        with open("audio_comments/" + self.filename + ".json", "r") as json_file:
            dict = json.load(json_file)
            print(dict)
            if str(self.current_position) in dict.keys():
                self.comment_label.config(text=dict.get(str(self.current_position)))
            else:
                self.comment_label.config(text=" ")

        json_file.close()

        self.progress_bar.after(1000, self.audio_progress)

    # def create_JSON_file(self, filename):
    #
    #     json_file = open("audio_comments/" + filename + ".json", "w")
    #
    #     return json_file


#      TO DO
#       Create normal popup windows(add positions)
#       Correct recording(make duration 60 second and try to add stop button)
#       Create text box with slider.
#       Visualize audio Progress bar




