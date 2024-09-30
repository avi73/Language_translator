from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

# Function to handle translation
def change(text="type", src="English", dest="Hindi"):
    trans = Translator()
    trans1 = trans.translate(text, src=src, dest=dest)
    return trans1.text

# Function to fetch data from input boxes
def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = Sor_txt.get(1.0, END)
    textget = change(text=masg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)

# Main window setup
root = Tk()
root.title("Language Translator")
root.geometry("600x700")
root.config(bg='#F0F8FF')  # Light blue background

# Main heading
lab_title = Label(root, text="Language Translator", font=("Arial", 30, "bold"), fg="#4B0082", bg="light pink")
lab_title.place(x=100, y=30, height=50, width=400)

# Label for source text box (aligned to the left)
lab_src = Label(root, text="Enter Your Text", font=("Arial", 14, "bold"), fg="black", bg='#F0F8FF')
lab_src.place(x=50, y=100, height=30, width=200)  # Adjusted font size and width for better fit

# Source text input box
Sor_txt = Text(root, font=("Arial", 14), wrap=WORD, relief=GROOVE, bd=2)
Sor_txt.place(x=50, y=150, height=150, width=500)

# List of available languages
list_text = list(LANGUAGES.values())

# Dropdown for selecting source language
comb_sor = ttk.Combobox(root, value=list_text, font=("Arial", 12))
comb_sor.place(x=50, y=320, height=40, width=200)
comb_sor.set("English")  # Default source language

# Button for translating the text
button_change = Button(root, text='Translate', fg="white", bg="#FF4500", font=("Arial", 12, "bold"), command=data)
button_change.place(x=250, y=320, height=40, width=100)

# Dropdown for selecting destination language
comb_dest = ttk.Combobox(root, value=list_text, font=("Arial", 12))
comb_dest.place(x=360, y=320, height=40, width=200)
comb_dest.set("Hindi")  # Default destination language

# Label for translated text (aligned to the left)
lab_dest = Label(root, text="Translated Text", font=("Arial", 14, "bold"), fg="black", bg='#F0F8FF')
lab_dest.place(x=50, y=380, height=30, width=200)  # Adjusted font size and width for better fit

# Translated text output box
dest_txt = Text(root, font=("Arial", 14), wrap=WORD, relief=GROOVE, bd=2)
dest_txt.place(x=50, y=420, height=150, width=500)

root.mainloop()
