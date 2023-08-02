# Libraries Imports
import tkinter as tk
import pyshorteners as pyshorts
from tkinter import Button

# FUNCTION TO ACCEPT THE URL AND CONVERT 
def MiniURL(args):
    getUrl = textfield.get()
    try:
        urlcall = pyshorts.Shortener()
        shortened_url = urlcall.tinyurl.short(getUrl)
        textfield2.delete(0, tk.END)
        textfield2.insert(0, shortened_url)
    except Exception as e:
        textfield2.delete(0, tk.END)
        textfield2.insert(0, f"Error: {str(e)}")

# FUNCTION TO RESET THE OUTPUT COLUMN
def Reset():
    textfield2.delete('1', tk.END)

# FRAME DECLARATION
frame = tk.Tk()
frame.geometry('650x310')
frame.title('URL Minimizer')
frame.configure(bg='light blue')

# TEXT PROPERTIE DECLARATION
fontProperty = ('Cascadia Mono SemiBold', 12)
textProperty = ('Cascadia Mono SemiBold', 10)

text0 = tk.Label(frame, font=textProperty)
text0.configure(bg='red')
text0.pack()

textfield = tk.Entry(frame, font=fontProperty, justify='center', width=80)
textfield.pack(pady=10)
textfield.bind('<Return>', MiniURL)

text1 = tk.Label(frame, font=textProperty)
text1.configure(bg='light blue')
text1.pack()

textfield2 = tk.Entry(frame, font=textProperty, justify='center', width= 80)
textfield2.configure()
textfield2.pack(pady=15)

specify = 'ENTER URL : '
instructions = '\n' + 'THIS IS URL SHORTENER' + '\n\n' + 'RULE #1> Enter the URL you want to Shorten in the given above Input BOX.' + '\n' + 'RULE #2> After Entering the URL PRESS ENTER BUTTON.' + '\n' + 'RULE #3> After Hitting the ENTER BUTTON the Shorten URL will be provided Below.' + '\n\n' + 'THE SHORTEN URL!!'
text0.configure(text=specify)
text1.configure(text=instructions, justify='center')

button = Button(frame, text='RESET', command=Reset, bg='orange')
button.pack()

# TO MAKE FRAMES/WINDOW VISIBLE
frame.mainloop()
