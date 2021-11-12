import tkinter as tk
from tkinter import ttk
import os

window = tk.Tk()
window.geometry("500x300")
window.title("Wine")
window.resizable(False, False)
window.configure(background="#525150")

txt = tk.Text(window)
txt.grid()

img = tk.PhotoImage(file="../img/wine.png")
background= tk.Label(window, image=img)
background.place(x=0,y=0,relwidth=1,relheight=1)

photo = tk.PhotoImage(file='../img/wine.png')
tk.Label(window, image=photo).place(x=0, y=0)

title = tk.Label(text="Menu", fg="#C90860", font=("Georgia", 20)).place(x=220, y=0)

def ins_wine_command():
    window.destroy()
    os.system('python inserimento_vino.py')


def search_wine_command():
    window.destroy()
    os.system('python ricerca_vino.py')

# Import the image using PhotoImage function
click_ins = tk.PhotoImage(file='../img/valuta.png')
click_search = tk.PhotoImage(file='../img/ricerca.png')

# Let us create a label for button event
img_ins = tk.Label(image=click_ins)
img_search = tk.Label(image=click_search)

# Let us create a dummy button and pass the image
ins_button= tk.Button(window, image=click_ins, command=ins_wine_command,
                           borderwidth=0).place(x=100, y=70)
search_button = tk.Button(window, image=click_search, command=search_wine_command,
                           borderwidth=0).place(x=100, y=170)

if __name__ == '__main__':
    window.mainloop()