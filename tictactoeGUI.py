import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.font as font

root = Tk()
root.geometry('400x500')  
root.title('Tic Tac Toe')  
cnt=0
myFont = font.Font(size = 40)

btn1 = tk.Button(root, text = " ", height=3, width=5)
btn1.config(command=lambda: update_button(btn1))
btn2 = tk.Button(root, text = " ", height=3, width=5)
btn2.configure(command=lambda: update_button(btn2))
btn3 = tk.Button(root, text = " ", height=3, width=5)
btn3.configure(command=lambda: update_button(btn3))
btn4 = tk.Button(root, text = " ", height=3, width=5)
btn4.configure(command=lambda: update_button(btn4))
btn5 = tk.Button(root, text = " ", height=3, width=5)
btn5.configure(command=lambda: update_button(btn5))
btn6 = tk.Button(root, text = " ", height=3, width=5)
btn6.configure(command=lambda: update_button(btn6))
btn7 = tk.Button(root, text = " ", height=3, width=5)
btn7.configure(command=lambda: update_button(btn7))
btn8 = tk.Button(root, text = " ", height=3, width=5)
btn8.configure(command=lambda: update_button(btn8))
btn9 = tk.Button(root, text = " ", height=3, width=5)
btn9.configure(command=lambda: update_button(btn9))

btnList = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]

for btn in btnList:
    btn['font'] = myFont
    for i in range(3):
        for j in range(3):
            btn.grid(row = i, column = j)

def update_button(btn):
    global cnt 
    if cnt%2 == 0:
        btn.config(text="X")
    else:
        btn.config(text="O")
    cnt += 1
    btn.configure(state=DISABLED)
    check_win()

    
def check_win():

    # check for horizontal win
    if btn1['text'] != " " and btn1['text'] == btn2['text'] == btn3['text']:
        messagebox.showinfo("Winner!")
    elif btn4['text'] != " " and btn4['text'] == btn5['text'] == btn6['text']:
        messagebox.showinfo("Winner!")
    elif btn7['text'] != " " and btn7['text'] == btn8['text'] == btn9['text']:
        messagebox.showinfo("Winner!")

    # check for vertical win 
    elif btn1['text'] != " " and btn1['text'] == btn4['text'] == btn7['text']:
        messagebox.showinfo("Winner!")
    elif btn2['text'] != " " and btn2['text'] == btn5['text'] == btn8['text']:
        messagebox.showinfo("Winner!")
    elif btn3['text'] != " " and btn3['text'] == btn6['text'] == btn9['text']:
        messagebox.showinfo("Winner!")

    # check for diagonal win 
    elif btn1['text'] != " " and btn1['text'] == btn5['text'] == btn9['text']:
        messagebox.showinfo("Winner!")
    elif btn3['text'] != " " and btn3['text'] == btn5['text'] == btn7['text']:
        messagebox.showinfo("Winner!")
    
    else:
        return False




root.mainloop()

