import tkinter as tk
from tkinter import * 

root = Tk()

root.geometry('300x250')  # size window
root.title('Tic Tac Toe')  

def update_button(cnt):
    if cnt%2 == 0:
        btn.config(text="X")
    else:
        btn.config(text="O")
    cnt += 1
    
for i in range(0,3):
    for j in range(0,3):
        btn = tk.Button(root, text=" ")  # make initial button
        btn.grid(row = i, column = j)  # put button on grid
        btn.configure(command=update_button)  # give button command

def play():
    cnt = 0
    while cnt <= 9:
        print(cnt)
        update_button(cnt)
        cnt += 1

play()

root.mainloop()

