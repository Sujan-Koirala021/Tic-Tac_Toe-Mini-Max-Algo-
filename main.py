from tkinter import *

root = Tk()
root.title("Tic-Tac-Toe")
root.geometry('440x390')

def createButton(rowPos, columnPos):
    return Button(root, text="", height = 7, width =18).grid(row = rowPos, column = columnPos, padx =5, pady =5)

#    Nine buttons
b1 = createButton(0, 0)
b2 = createButton(0, 1)
b3 = createButton(0, 2)
b4 = createButton(1, 0)
b5 = createButton(1, 1)
b6 = createButton(1, 2)
b7 = createButton(2, 0)
b8 = createButton(2, 1)
b9 = createButton(2, 2)

root.mainloop()