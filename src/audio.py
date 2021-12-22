from playsound import playsound
import sounddevice as sd
import soundfile as sf
import pygame as pg
from pydub import AudioSegment
import scipy.io.wavfile as wf
import os


class Audio:

    def __init__(self):
        self.pause = True
        self.filename = "hello.mp3"

    def set_filename(self, filename):
        self.filename = filename

    def read_audio_file(self, filename):
        sound, samplerate = sf.read(filename)
        return sound, samplerate

    def play_audio_file(self, filename):
        playsound("audio_files/" + filename)

    def play_audio_file_new(self):
        pg.init()
        pg.mixer.music.load("audio_files/" + self.filename)
        pg.mixer.music.play(1, 0.0)
        self.pause = False

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

audio = Audio()
audio.create_audio_file("hello")