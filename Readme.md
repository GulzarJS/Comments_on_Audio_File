# Comments on Audio File Application

The repository contains the implementation for Comments on Audio file Application.

The code uses Python3, `matplotlib`, `numpy`, `tkinter`, `pygame`, 
`scipy`, `sounddevice`, `pydub`, `mutagen`, `json` and `os` libraries of Python. 

## Table of contents
- [Installation of libraries](#installation-of-libraries)
- [Running user interface](#running-user-interface)
- [Recording new audio file](#recording-new-audio-file)
- [Playing audio file](#playing-audio-file)
- [Pausing audio file](#pausing-audio-file)
- [Comment on audio file](#comment-on-audio-file)
- [Structure of the project](#structure-of-the-project)


## Installation of libraries
This repository can be run properly in the Linux Operating System.
Only the `mutagen` library cause problem in the Windows Operating System.

- pip install pygame
- pip install tk 
- pip install mutagen 
- pip install sounddevice 
- pip install mutagen / python3 -m pip install mutagen 
- pip install json 
- pip install scipy 
- pip install pydub 



## Running user interface
To run the user interface, you should run the `main.py` file in the terminal.
It will launch the whole program and will let you record a new audio file, select, play,
pause audio file and put comments on audio when you listen to it.
Newly created files are stored in the 'audio_files' directory. When you put comments on them, their JSON file
are stored in the 'audio_comments' directory.


## Recording new audio file
After running user interface:
- click the `Record` button
- input name of new audio file
- click the `Start_to_record` button and start to talk




## Playing audio file
After running user interface:
- click the `Select` button in the Main window
- choose name of file in option menu => `Tap to choose filename`
- click the `Select` button in the Pop-up window
- click the `Play` button in the Main window



## Pausing audio file
After playing the audio file:
- click the `Pause` button in the Main window to pause and unpause

## Comment on audio file
After playing the audio file:
- click the `Pause` button in the Main window
- write a comment in the comment text box
- click the `comment` button to submit a comment

## Structure of the project
The source code of the project is located in the 'src' folder. It's logically divided in
'.py' files and folders (which contain audio '.mp3' files and '.json' files) parts. Everything related to the user interface,
located in the 'src/ui.py' file.
Everything located in the 'src/audio.py' is related to the functionalities of the audio file (recording, playing, pausing, etc.)

The repository also contains a `comment_on_audio.ipynb` file which contains audio analysis of project.

