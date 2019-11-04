
from Tkinter import *
import configparser
import tkFileDialog
import pdftotext
import ScrolledText

import main
from functools import partial

var1=0


#choosing language
def sel():
    print("English\n")
def sel1():
    print("English-US\n")
def sel2():
    print("Italian\n")



#To convert the content in text field to speech
def do(et,w, var1):
    print(var1.get())
    x = 2 - (w.get()*1.0)/100
    if x == 0:
		x = 0.001
    main.setStretchFactor(x)
    ad = str(et.get('1.0', END))
    if ad == '\n':
		return 1
    main.sayText(ad)





#To open a file and covert it's content to speech
def open_(fun_edit, w):
  x = 2 - (w.get()*1.0)/100
  if x == 0:
    x = 0.001
  main.setStretchFactor(x)
  ad = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("txt","*.txt"),("pdf","*.pdf"),("all files","*.*")))
  if(".pdf" in ad):
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




#function for pause
def pause_(fun_edit):
    print("pause")
# mycolor = '#%02x%02x%02x' % (64, 204, 208)
master = Tk()
# master.configure(background="")
master.title("Evoice: a Text-To-Speech Synthesizer")





#Scroll Text Box
edit_space = ScrolledText.ScrolledText(
    wrap   = 'word',
    # width  = "60",
    height = "8",
    # bg="azure3"
    )

edit_space.grid(row = 2,column = 0,padx=(25, 25),columnspan=4)


#pause line/paragraph
var1 = IntVar()
R1 = Radiobutton( text = "Line", variable = var1, value = 1)
R1.grid(row=1, column=0, padx=(20,0),pady=20)
R2 = Radiobutton( text = "Paragraph", variable = var1, value = 2)
R2.grid(row=1, column=1, pady=20)
R3 = Radiobutton( text = "No break", variable = var1, value = 3)
R3.grid(row=1, column=2, pady=20, padx=(0,25))

# #adding options for voice type
# var = IntVar()
# R1 = Radiobutton( text = "English-UK", variable = var, value = 1,
#                   command = sel)
# R1.grid(row=5, column=0,sticky="ew")
# R2 = Radiobutton( text = "English-US", variable = var, value = 2,
#                   command = sel1)
# R2.grid(row=6, column=0,sticky="ew", pady=(0,50))






#Speed of speech
# Label(master, text='Speed').grid(row=4, column=0, pady=(20,25))
w = Scale(master, from_=0, to=200, orient=HORIZONTAL, tickinterval=0.01)
w.grid(row=3, column=3, padx=(0,25), pady=(10,25))
w.set(100)
# Label(master, text='Enter the text or choose from a file').grid(row=0, column=3, sticky="ew")
# Label(master, text='Specify the pause point: Line, Paragraph or no pause.').grid(row=0, column=1, sticky="ew", pady=(25,0))



#Play Button
button2 = Button(
                   text="Play",activebackground="CadetBlue4",
                   # fg="red",
                   command=partial(do,edit_space,w, var1))
button2.grid(row=3,column=0,pady="25", padx=(25,15))





#Choose File button
button1 = Button(
                   text="Choose a File", activebackground="CadetBlue4",
                   # fg="red",
                   command=partial(open_,edit_space,w))
button1.grid(row=3,column=1, pady="15",padx="15")


#
# #pause button
# button4 = Button(
#                    text="Pause",
#                    # fg="red",
#                    command=partial(pause_,edit_space))
#
# button4.grid(row=2,column=0, pady="15", padx="15",sticky="ew")




#Clear Button
button = Button(
                   text="Clear", activebackground="CadetBlue4",
                   # fg="red",
                   command=partial(clear_,edit_space))

button.grid(row=3,column=2, pady="15", padx="15")
mainloop()
