
from Tkinter import *
import configparser
import tkFileDialog
import pdftotext
# import Tkinter.scrolledtext as scrolledtext
import ScrolledText

import main
from functools import partial

#To convert the content in text field to speech
def do(et,w):
	x = 2 - (w.get()*1.0)/100
	if x == 0:
		x = 0.001
	main.setStretchFactor(x)
	ad = str(et.get('1.0', END))
	if ad == '\n':
		return 1
	main.sayText(ad)

#To open a file and covert it's content to speech

def open_(fun_edit):
	ad = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("txt","*.txt"),("pdf","*.pdf"),("all files","*.*")))
	if(".pdf" in ad):
		# Load your PDF
		with open(ad, "rb") as f:
    		pdf = pdftotext.PDF(f)
    	main.sayText("\n\n".join(pdf))
    else:
    	file = open(ad, 'r')
		fun_edit.insert('insert', file.read())
		main.sayFile(ad)

#To delete the content in the text box

def clear_(fun_edit):
	fun_edit.delete('1.0', END)

master = Tk()
master.title("TTS")

#Scroll Text Box
edit_space = ScrolledText.ScrolledText(
    wrap   = 'word',
    width  = "150",
    height = 20
    )
edit_space.grid(row = 0 , column = 0, padx="5")
#Clear Button
button = Button(
                   text="Clear",
                   fg="red",
                   command=partial(clear_,edit_space))

button.grid(row=0,column=1)

#Speed of speech
Label(master, text='Speed').grid(row=1, column=1)
w = Scale(master, from_=0, to=200, orient=HORIZONTAL, tickinterval=0.01)
w.grid(row=1, column=3)
w.set(100)

#Play Button
button = Button(
                   text="Play",
                   fg="red",
                   command=partial(do,edit_space,w))
button.grid(row=0,column=2)

#Choose File button
button1 = Button(
                   text="Choose File",
                   fg="red",
                   command=partial(open_,edit_space,))

button1.grid(row=0,column=3)

mainloop()
