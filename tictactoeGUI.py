import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.font as font

root = Tk()
root.geometry('400x500')  
root.title('Tic Tac Toe')  
cnt=0
myFont = font.Font(size = 40)

# make btns
btn1 = tk.Button(root, text = " ", height=3, width=5)
btn2 = tk.Button(root, text = " ", height=3, width=5)
btn3 = tk.Button(root, text = " ", height=3, width=5)
btn4 = tk.Button(root, text = " ", height=3, width=5)
btn5 = tk.Button(root, text = " ", height=3, width=5)
btn6 = tk.Button(root, text = " ", height=3, width=5)
btn7 = tk.Button(root, text = " ", height=3, width=5)
btn8 = tk.Button(root, text = " ", height=3, width=5)
btn9 = tk.Button(root, text = " ", height=3, width=5)

# grid btns
btn1.grid(row = 0, column = 0)
btn2.grid(row = 0, column = 1)
btn3.grid(row = 0, column = 2)
btn4.grid(row = 1, column = 0)
btn5.grid(row = 1, column = 1)
btn6.grid(row = 1, column = 2)
btn7.grid(row = 2, column = 0)
btn8.grid(row = 2, column = 1)
btn9.grid(row = 2, column = 2)

# add command functionality
btn1.configure(command=lambda: update_button(btn1))
btn2.configure(command=lambda: update_button(btn2))
btn3.configure(command=lambda: update_button(btn3))
btn4.configure(command=lambda: update_button(btn4))
btn5.configure(command=lambda: update_button(btn5))
btn6.configure(command=lambda: update_button(btn6))
btn7.configure(command=lambda: update_button(btn7))
btn8.configure(command=lambda: update_button(btn8))
btn9.configure(command=lambda: update_button(btn9))

# create list of btns
btnList = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]

# use font
for btn in btnList:
    btn['font'] = myFont


# update button
def update_button(btn):
    global cnt 
    if cnt%2 == 0:
        btn.config(text="X")
        cnt += 1
        check_x_win()
    else:
        btn.config(text="O")
        cnt += 1
        check_o_win()
    btn.configure(state=DISABLED)


# check for Player X win 
def check_x_win():

    # check for horizontal win
    if (
        btn1['text'] != " " and btn1['text'] == btn2['text'] == btn3['text'] or \
        btn4['text'] != " " and btn4['text'] == btn5['text'] == btn6['text'] or \
        btn7['text'] != " " and btn7['text'] == btn8['text'] == btn9['text'] or \

    # check for vertical win 
        btn1['text'] != " " and btn1['text'] == btn4['text'] == btn7['text'] or \
        btn2['text'] != " " and btn2['text'] == btn5['text'] == btn8['text'] or \
        btn3['text'] != " " and btn3['text'] == btn6['text'] == btn9['text'] or \

    # check for diagonal win 
        btn1['text'] != " " and btn1['text'] == btn5['text'] == btn9['text'] or \
        btn3['text'] != " " and btn3['text'] == btn5['text'] == btn7['text']
    ):
        messagebox.showinfo("Winner", "Player X wins!")
        root.quit()

    if cnt==9:
        messagebox.showinfo("Stalemate", "Stalemate")
        root.quit()


# check for Player O win
def check_o_win():

    # check for horizontal win
    if (
        btn1['text'] != " " and btn1['text'] == btn2['text'] == btn3['text'] or \
        btn4['text'] != " " and btn4['text'] == btn5['text'] == btn6['text'] or \
        btn7['text'] != " " and btn7['text'] == btn8['text'] == btn9['text'] or \

    # check for vertical win 
        btn1['text'] != " " and btn1['text'] == btn4['text'] == btn7['text'] or \
        btn2['text'] != " " and btn2['text'] == btn5['text'] == btn8['text'] or \
        btn3['text'] != " " and btn3['text'] == btn6['text'] == btn9['text'] or \

    # check for diagonal win 
        btn1['text'] != " " and btn1['text'] == btn5['text'] == btn9['text'] or \
        btn3['text'] != " " and btn3['text'] == btn5['text'] == btn7['text']
    ):
        messagebox.showinfo("Winner", "Player O wins!")
        root.quit()

    if cnt==9:
        messagebox.showinfo("Stalemate", "Stalemate")
        root.quit()



root.mainloop()

