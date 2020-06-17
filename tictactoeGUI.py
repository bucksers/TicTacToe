import tkinter as tk
from tkinter import *
from tkinter import messagebox


root = Tk()
root.geometry('300x250')  # size window
root.title('Tic Tac Toe')  
cnt=0

btn1 = tk.Button(root, text = " ", height=3, width=5)
btn1.grid(row = 0, column = 0)
btn1.config(command=lambda: update_button(btn1))
btn2 = tk.Button(root, text = " ", height=3, width=5)
btn2.grid(row = 0, column = 1)
btn2.configure(command=lambda: update_button(btn2))
btn3 = tk.Button(root, text = " ", height=3, width=5)
btn3.grid(row = 0, column = 2)
btn3.configure(command=lambda: update_button(btn3))
btn4 = tk.Button(root, text = " ", height=3, width=5)
btn4.grid(row = 1, column = 0)
btn4.configure(command=lambda: update_button(btn4))
btn5 = tk.Button(root, text = " ", height=3, width=5)
btn5.grid(row = 1, column = 1)
btn5.configure(command=lambda: update_button(btn5))
btn6 = tk.Button(root, text = " ", height=3, width=5)
btn6.grid(row = 1, column = 2)
btn6.configure(command=lambda: update_button(btn6))
btn7 = tk.Button(root, text = " ", height=3, width=5)
btn7.grid(row = 2, column = 0)
btn7.configure(command=lambda: update_button(btn7))
btn8 = tk.Button(root, text = " ", height=3, width=5)
btn8.grid(row = 2, column = 1)
btn8.configure(command=lambda: update_button(btn8))
btn9 = tk.Button(root, text = " ", height=3, width=5)
btn9.grid(row = 2, column = 2)
btn9.configure(command=lambda: update_button(btn9))


def update_button(btn):
    global cnt 
    if cnt%2 == 0:
        btn.config(text="X")
    else:
        btn.config(text="O")
    cnt += 1
    btn.configure(state=DISABLED)
    if cnt!=0:  # don't check win right at beginning
        check_win()

    
def check_win():
    
    # check for horizontal win
    if btn1['text'] == btn2['text'] == btn3['text']:
        return True
    elif btn4['text'] == btn5['text'] == btn6['text']:
        return True
    elif btn7['text'] == btn8['text'] == btn9['text']:
        return True

    # check for vertical win 
    elif btn1['text'] == btn4['text'] == btn7['text']:
        return True
    elif btn2['text'] == btn5['text'] == btn8['text']:
        return True
    elif btn3['text'] == btn6['text'] == btn9['text']:
        return True

    # check for diagonal win 
    elif btn1['text'] == btn5['text'] == btn9['text']:
        return True
    elif btn3['text'] == btn2['text'] == btn7['text']:
        return True
    
    else:
        return False
        


root.mainloop()

