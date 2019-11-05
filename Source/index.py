
from Tkinter import *
import configparser
import tkFileDialog
import pdftotext
import ScrolledText
import tkMessageBox
import main
from functools import partial



'''------------------------------------Converting text to speech----------------------------------------'''
# Function: TextBox
# It firstly changes the speed by calling main.setStretchFactor() and then converts the text to speech.
#
#Parameters:
#   et - Entry object that stores the input.
#   w - Object to store value returned by slider widget.
#   var1 - The value of radio button chosen


def TextBox(et,w,var1):
  x = 2 - (w.get()*1.0)/100
  if x <0.1:
		x = 0.1
#For inter-line and inter-para pausing
  main.setStretchFactor(x)
  ad = str(et.get('1.0', END))
  if et.tag_ranges(SEL):
    ad = et.get(SEL_FIRST ,SEL_LAST)
  if ad == '\n':
		return 1
  if var1.get() == 2:
    ad=ad.split('\n')
    for i in range(len(ad)):
      if not ad[i].strip():
        continue
      main.sayText(ad[i])
      result = tkMessageBox.askyesno("Python","Do you want to continue?")
      if not result:
        break
  if var1.get() == 1  :
    ad=ad.split('.')
    for i in range(len(ad)):
      if not ad[i].strip():
        continue
      main.sayText(ad[i])
      result = tkMessageBox.askyesno("Python","Do you want to continue?")
      if not result:
        break
  if var1.get() == 3 or var1.get() == 0:
    main.sayText(ad)



'''------------------------------------Opening a File----------------------------------------'''
# Function: TextFromFile
# Function to open the file to read the text from.
#
# Parameters:
#   fun_edit - Entry object that stores the input.
#   w - Object to store value returned by slider widget.
#   var1 - The value of radio button chosen
def TextFromFile(fun_edit,w,var1):
  x = 2 - (w.get()*1.0)/100
  if x < 0.1:
    x = 0.1
  main.setStretchFactor(x)
  ad = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("txt","*.txt"),("pdf","*.pdf"),("all files","*.*")))
  if(".pdf" in ad):
    with open(ad, "rb") as f:
      pdf = pdftotext.PDF(f)
      main.sayText("\n\n".join(pdf))
  else:
    with open(ad, 'r') as myfile:
      s = myfile.read()
      # print s
      if s == '\n':
        return 1
      if var1.get() == 2:
        s=s.split('\n')
        for i in range(len(s)):
          if not s[i].strip():
            continue
          main.sayText(s[i])
          result = tkMessageBox.askyesno("Python","Do you want to continue?")
          if not result:
            break
      if var1.get() == 1  :
        s=s.split('.')
        for i in range(len(s)):
          if not s[i].strip():
            continue
          main.sayText(s[i])
          result = tkMessageBox.askyesno("Python","Do you want to continue?")
          if not result:
            break
      if var1.get() == 3 or var1.get() == 0:
        main.sayText(s)



'''------------------------------------Clearing the text box----------------------------------------'''
# Function: clear_
# Function to clear the text box.
#
# Parameters:
#   fun_edit - Entry object that stores the input.
def clear_(fun_edit):
	fun_edit.delete('1.0', END)



'''------------------------------------Creating the Tkinter Window----------------------------------------'''
master = Tk()
master.title("Evoice: a Text-To-Speech Synthesizer")



'''------------------------------------Text Box For Input---------------------------------------'''
edit_space = ScrolledText.ScrolledText(
    wrap   = 'word',
    height = "8",
    )
edit_space.grid(row = 2,column = 0,padx=(25, 25),columnspan=4)


'''------------------------------------Pause options----------------------------------------'''
var1 = IntVar()
R1 = Radiobutton( text = "Line", variable = var1, value = 1)
R1.grid(row=1, column=0, padx=(20,0),pady=20)
R2 = Radiobutton( text = "Paragraph", variable = var1, value = 2)
R2.grid(row=1, column=1, pady=20)
R3 = Radiobutton( text = "No break", variable = var1, value = 3)
R3.grid(row=1, column=2, pady=20, padx=(0,25))



'''------------------------------------Slider for speed----------------------------------------'''
w = Scale(master, from_=0, to=200, orient=HORIZONTAL, tickinterval=0.01)
w.grid(row=3, column=3, padx=(0,25), pady=(10,25))
w.set(100)



'''------------------------------------Buttons for play, open file, clear----------------------------------------'''
button2 = Button(
                   text="Play",activebackground="CadetBlue4",
                   command=partial(TextBox,edit_space,w, var1))
button2.grid(row=3,column=0,pady="25", padx=(25,15))


button1 = Button(
                   text="Choose a File", activebackground="CadetBlue4",
                   command=partial(TextFromFile,edit_space,w,var1))
button1.grid(row=3,column=1, pady="15",padx="15",sticky="ew")


button = Button(
                   text="Clear", activebackground="CadetBlue4",
                   command=partial(clear_,edit_space))
button.grid(row=3,column=2, pady="15", padx="15")


'''------------------------------------End----------------------------------------'''
mainloop()
