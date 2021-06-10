from tkinter import *
from googletrans import Translator, LANGUAGES
# create tkinter window 
Window= Tk()
#add title
Window.title("Convertor")
#add dimensions 
Window.configure(bg = "#42ff30")

font_tup = ("Comic Sans MS", 15, "bold")
font_tup_head = ("Algerian", 20, "underline")
#heading 
heading1 = Label(Window, text = "Language Convertor",font = font_tup_head, bg = "#42ff30")
heading1.grid(row=0,column=1,padx=20,pady=20)


#label and entry box 
label1= Label(Window, text = "Enter your text in English:", font= font_tup, bg = "#42ff30")
label1.grid(row=1,column=0,padx=10)

entry = Entry(Window, width = 50, font= font_tup) 
entry.grid(row=1,column=1,pady = 20,padx=20)


#Text label
label1= Label(Window, text = "Text in Hindi:", font= font_tup, bg = "#42ff30")
label1.grid(row=2,column=0,padx=10)

Output_text = Text(Window, height= 2, width = 50 , font= font_tup)
Output_text.grid(row=2,column=1,pady = 20,padx=20)




#function for Translation    
def Translate():
  translator = Translator()
  translated = translator.translate(text = entry.get(), src = "en", dest="hi")
  Output_text.delete(1.0, END)
  Output_text.insert(END, translated.text)

# our Translate function using command = Translate 
trans_btn = Button(Window, text = 'Translate', font= font_tup, command = Translate,width=20)
trans_btn.grid(row=3,column=1,pady = 20,padx=20)


# start the gui 
Window.mainloop() 

