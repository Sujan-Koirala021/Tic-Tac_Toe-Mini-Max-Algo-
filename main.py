# Tic Tac Toe
# March 27, 2022

from tkinter import *
from tkinter import messagebox
import random, time


root = Tk()
root.title("Tic-Tac-Toe")
root.geometry('495x440')
root.iconbitmap('appIcon.ico')
state = 0
buttonList = []
oList = []
xList = []


#   Winning posture (Child list)
ticTakWin = [[1, 2, 3], [4, 5, 6], [7, 8, 9], 
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7] ]  
#   Make window unresizable
root.resizable(False, False)

def buttonClick(buttonVal):
    # Disable button after click
    buttonList[buttonVal-1].config(state = DISABLED)
    
    # global state
    # state += 1
    
    #   User's turn
    buttonList[buttonVal-1].config(text = "O")
    oList.append(buttonVal)
    if checkWin(oList):
        highlightWin()
        showInformation("O is winner")
        numbAllButtons()
        return

    
    #   Bot's turn
    availList = [item for item in [1, 2, 3, 4, 5, 6, 7, 8, 9] if (item not in  oList and item not in xList)]

    buttonVal = random.choice(availList)
    
    buttonList[buttonVal-1].config(text = "X")
    xList.append(buttonVal)
    if checkWin(xList):
        highlightWin()
        showInformation("X is winner")
        numbAllButtons()
        return
            
    if (state == 9):
        showInformation("Draw")

#   Check winning condition 
def checkWin(parentList):
    for item in ticTakWin:
        if (set(item).issubset(set(parentList))):
            global toHighlightItem;
            toHighlightItem = item;     #   List of buttons to be highlighted
            return 1
        
def highlightWin():
    for item in toHighlightItem:
        buttonList[item-1].config(bg = '#013220')

def createButton( flag):
    return Button(root, text="",font = ('Helvetica', 23), bg = '#121212', fg = 'white', height = 3, width =8, command=lambda:buttonClick(flag))

#   Check for draw
def checkDraw():
    for item in buttonList:
        if (item['state'] == DISABLED):  
            return 1
        else:
            return 0
            break

#   Numb button after gameover
def numbAllButtons():
    for item in buttonList:
        item['state'] = DISABLED
        pass

#   Show information as message box
def showInformation(text):
    messagebox.showinfo("GAME OVER",text)
    

#    Creating buttons
b1 = createButton(1)  # Parameters -> flag
b2 = createButton(2)
b3 = createButton(3)
b4 = createButton(4)
b5 = createButton(5)
b6 = createButton(6)
b7 = createButton(7)
b8 = createButton(8)
b9 = createButton(9)

#   Adding all buttons to a list
buttonList += [b1, b2, b3, b4, b5, b6, b7, b8, b9]

#   Griding buttons
b1.grid(row = 0, column = 0, padx =5, pady =5)
b2.grid(row = 0, column = 1, padx =5, pady =5)
b3.grid(row = 0, column = 2, padx =5, pady =5)
b4.grid(row = 1, column = 0, padx =5, pady =5)
b5.grid(row = 1, column = 1, padx =5, pady =5)
b6.grid(row = 1, column = 2, padx =5, pady =5)
b7.grid(row = 2, column = 0, padx =5, pady =5)
b8.grid(row = 2, column = 1, padx =5, pady =5)
b9.grid(row = 2, column = 2, padx =5, pady =5)

root.mainloop()