import tkinter as tk
from tkinter import ttk
from gttk import GTTK
from tkinter import *
from googletrans import Translator, LANGUAGES
from tkinter import messagebox
import speech_recognition as sr
from pygame import mixer
import os
from langdetect import detect
from gtts import gTTS
import cv2
import webbrowser

root = tk.Tk()
root.title("Language Translator 2.0")
root.geometry('550x350')
root.minsize(550, 350)
gttk = GTTK(root)
style = ttk.Style()
style.theme_use("vista")
gttk.set_gtk_theme("scidgreen")
root.configure(bg='black')
root.iconbitmap(r'C:\Users\A.GOWTHAMI\Downloads\PngItem_130136.png')

app_name = Label(root, text='Language Translator', font=('Bookman Old Style', 26), bg='black', fg='white', height=2)
app_name.pack(side=TOP, fill=BOTH, pady=0)
version = Label(root, text='2.O', fg='white', bg='black').place(x=450, y=48)

photo = PhotoImage(file=r'C:\Users\A.GOWTHAMI\Downloads\PngItem_343069.png').subsample(30, 30)
photo1 = PhotoImage(file=r'C:\Users\A.GOWTHAMI\Downloads\bidirectional arrow png.png').subsample(20, 20)
photo2 = PhotoImage(file=r'C:\Users\A.GOWTHAMI\Downloads\camera  PNG.png').subsample(40, 40)


def translate():
    language_1 = textbox1.get("1.0", "end-1c")
    lan1 = auto_detect.get()

    if lan1 not in auto_detect['values']:
        messagebox.showerror("Language Translator 2.0", "Please choose a valid language!")

    lan2 = choose_language.get()
    if lan2 not in choose_language['values']:
        messagebox.showerror("Language Translator 2.0", "Please choose a valid language!")

    if language_1 == "":
        messagebox.showwarning("Language Translator 2.0", "Please fill up the box")
    else:
        translator = Translator()
        output = translator.translate(text=language_1, src=lan1, dest=lan2)
        f"{output.origin} ({output.src}) --> {output.text} ({output.dest})"
        textbox2.insert('end', output.text)


def translate_it():
    language_1 = textbox1.get("1.0", "end-1c")
    lan1 = auto_detect.get()
    lan2 = choose_language.get()
    translator = Translator()
    output = translator.translate(text=language_1, src=lan1, dest=lan2)
    f"{output.origin} ({output.src}) --> {output.text} ({output.dest})"
    detect_it = detect(output.text)
    result = gTTS(text=output.text, lang=detect_it, slow=False)
    result.save("Welcome.mp3")
    os.system("Welcome.mp3")


def buttonclick():
    mixer.init()
    mixer.music.load(r'C:\Users\A.GOWTHAMI\Downloads\chime1.mp3')
    mixer.music.play()
    read = sr.Recognizer()
    read.pause_threshold = 0.7
    read.energy_threshold = 400
    with sr.Microphone() as source:
        try:
            audio = read.listen(source, timeout=5)
            message = str(read.recognize_google(audio))
            textbox1.insert('end', message)
            mixer.music.load(r'C:\Users\A.GOWTHAMI\Downloads\chime2.mp3')
            mixer.music.play()
            textbox1.focus()
            textbox1.delete(0, END)
            textbox1.insert(0, message)
        except sr.UnknownValueError:
            print('Google Speech Recognition could not understand audio')

        except sr.RequestError:
            print('Could not request results from Google Speech Recognition Service')


def wiki():
    language_1 = textbox1.get("1.0", "end-1c")
    lan1 = auto_detect.get()
    lan2 = choose_language.get()
    translator = Translator()
    output = translator.translate(text=language_1, src=lan1, dest=lan2)
    f"{output.origin} ({output.src}) --> {output.text} ({output.dest})"
    if textbox2 != '':
        webbrowser.open('https://www.google.com/search?q=' + output.text)
    else:
        pass


def webcam():
    frame_width = 640
    frame_height = 480
    cap = cv2.VideoCapture(0)
    cap.set(3, frame_width)
    cap.set(4, frame_height)
    while True:
        success, img = cap.read()
        cv2.imshow("Result", img)
        if cv2.waitKey(1) & 0xFF == ord('c'):
            break


def exit_():
    ask = messagebox.askquestion(title='Language Translator 2.0', message='Do you want to quit?', icon='question')
    if ask == 'yes':
        root.destroy()
    else:
        pass


def clear():
    textbox1.delete(1.0, 'end')
    textbox2.delete(1.0, 'end')


var = tk.StringVar()
auto_detect = ttk.Combobox(root, width=20, textvariable=var, state="readandwrite", font=('sans-serif', 10, 'bold'))
auto_detect['values'] = list(LANGUAGES.values())
auto_detect.place(x=30, y=70)
auto_detect.current(0)

var1 = tk.StringVar()
choose_language = ttk.Combobox(root, width=20, textvariable=var1, state='readandwrite', font=('Arial', 10, 'bold'))


choose_language['values'] = list(LANGUAGES.values())


choose_language.place(x=290, y=70)
choose_language.current(0)

textbox1 = Text(root, width=30, height=10, borderwidth=5, relief=RIDGE)
textbox1.place(x=10, y=100)

textbox2 = Text(root, width=30, height=10, borderwidth=5, relief=RIDGE)
textbox2.place(x=260, y=100)

button = Button(root, image=photo1, relief=RIDGE, borderwidth=3, font=('verdana', 10, 'bold'), cursor='hand2',
                command=translate)
button.place(x=250, y=70)

clear = Button(root, text='Clear', relief=RIDGE, borderwidth=3, font=('verdana', 10, 'bold'), cursor='hand2',
               command=clear)
clear.place(x=0, y=318)

speak = Button(root, image=photo, relief=RIDGE, borderwidth=3, font=('verdana', 10, 'bold'), cursor='hand2',
               command=buttonclick)
speak.place(x=190, y=70)

translate_speech = Button(root, image=photo, relief=RIDGE, font=('verdana', 10, 'bold'), cursor='hand2',
                          command=translate_it)
translate_speech.place(x=450, y=70)

exit_it = Button(root, text='Exit', relief=RIDGE, font=('verdana', 10, 'bold'), cursor='hand2',
                 command=exit_)
exit_it.place(x=505, y=318)

search = Button(root, text='search', relief=FLAT, font=('verdana', 10, 'bold'), cursor='hand2', bg='white',
                command=wiki)
search.place(x=440, y=240)

camera = Button(root, image=photo2, relief=FLAT, cursor='hand2', bg='white', command=webcam)
camera.place(x=400, y=240)

root.wm_attributes('-topmost', 1)
root.mainloop()
