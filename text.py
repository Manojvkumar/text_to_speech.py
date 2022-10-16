from gtts import gTTS
from io import BytesIO
import pygame
from tkinter import *

root = Tk()
root.geometry('500x300')
root.title('Text To Speech')
root.config(bg='white')
root.maxsize(500,300)
root.minsize(500,300)

Label(root, text = 'TEXT TO SPEECH' , font='arial 20 bold' , bg ='white smoke').pack()
Label(root, text ='Enter Text', font ='arial 15 bold', bg ='white smoke').place(x=20,y=60)

#text variable
Msg = StringVar()
#Entry
input_field = Entry(root, textvariable=Msg, width = '60')
input_field.place(x=20, y=100)



def speak():
    a=Msg.get()
    pygame.init()
    pygame.mixer.init()
    mp3_fo = BytesIO()
    tts = gTTS(a, lang='en')
    tts.write_to_fp(mp3_fo)
    pygame.mixer.music.load(mp3_fo, 'mp3')
    pygame.mixer.music.play()
    #return mp3_fo
def Exit():
    root.destroy()
def Reset():
    Msg.set("")
    


# sound.seek(0)
Button(root, text = "PLAY" , font = 'arial 15 bold', command =speak, width =4).place(x=25, y=140)
Button(root,text = 'EXIT',font = 'arial 15 bold' , command = Exit, bg = 'Red').place(x=100,y=140)
Button(root,text = 'RESET', font='arial 15 bold', command = Reset).place(x=180 , y =140)




