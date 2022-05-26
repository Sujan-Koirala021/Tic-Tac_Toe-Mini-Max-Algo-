from tkinter import *

root = Tk()
root.title("Tic-Tac-Toe")
root.geometry('440x390')
state = 0
buttonList = []
#   Make window unresizable
root.resizable(False, False)

def buttonClick(buttonVal):
    global state
    state += 1
    if (state % 2 == 0):
        buttonList[buttonVal-1].config(text = "O")
    else:
        buttonList[buttonVal-1].config(text = "X")
        
    print(state)
    # pass


def createButton( flag):
    return Button(root, text="", height = 7, width =18, command=lambda:buttonClick(flag))


#    Nine buttons
b1 = createButton(1)  # Parameters -> flag
b2 = createButton(2)
b3 = createButton(3)
b4 = createButton(4)
b5 = createButton(5)
b6 = createButton(6)
b7 = createButton(7)
b8 = createButton(8)
b9 = createButton(9)

buttonList += [b1, b2, b3, b4, b5, b6, b7, b8, b9]

b1.grid(row = 0, column = 0, padx =5, pady =5)
b2.grid(row = 0, column = 1, padx =5, pady =5)
b3.grid(row = 0, column = 2, padx =5, pady =5)
b4.grid(row = 1, column = 0, padx =5, pady =5)
b5.grid(row = 1, column = 1, padx =5, pady =5)
b6.grid(row = 1, column = 2, padx =5, pady =5)
b7.grid(row = 2, column = 0, padx =5, pady =5)
b8.grid(row = 2, column = 1, padx =5, pady =5)
b9.grid(row = 2, column = 2, padx =5, pady =5)




#   Adjust Buttons to list

root.mainloop()