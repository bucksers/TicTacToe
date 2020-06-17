import tkinter as tk
from tkinter import *

root = Tk()

root.geometry('300x250')  # size window
root.title('Tic Tac Toe')  
cnt=0

def update_button(btn):
    global cnt 
    if cnt%2 == 0:
        btn.config(text="X")
    else:
        btn.config(text="O")
    cnt += 1
    btn.configure(state=DISABLED)

# NEXT TIME: disable button after changing it (in update_button)
    # Check for win
    


def play():
    
    btn1 = tk.Button(root, text = " ")
    btn1.grid(row = 0, column = 0)
    btn1.config(command=lambda: update_button(btn1))
    btn2 = tk.Button(root, text = " ")
    btn2.grid(row = 0, column = 1)
    btn2.configure(command=lambda: update_button(btn2))
    btn3 = tk.Button(root, text = " ")
    btn3.grid(row = 0, column = 2)
    btn3.configure(command=lambda: update_button(btn3))
    btn4 = tk.Button(root, text = " ")
    btn4.grid(row = 1, column = 0)
    btn4.configure(command=lambda: update_button(btn4))
    btn5 = tk.Button(root, text = " ")
    btn5.grid(row = 1, column = 1)
    btn5.configure(command=lambda: update_button(btn5))
    btn6 = tk.Button(root, text = " ")
    btn6.grid(row = 1, column = 2)
    btn6.configure(command=lambda: update_button(btn6))
    btn7 = tk.Button(root, text = " ")
    btn7.grid(row = 2, column = 0)
    btn7.configure(command=lambda: update_button(btn7))
    btn8 = tk.Button(root, text = " ")
    btn8.grid(row = 2, column = 1)
    btn8.configure(command=lambda: update_button(btn8))
    btn9 = tk.Button(root, text = " ")
    btn9.grid(row = 2, column = 2)
    btn9.configure(command=lambda: update_button(btn9))

play()

root.mainloop()

