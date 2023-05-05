import random
import math


class BotPlayer:
    
    def __init__(self, availList, oList, xList):
        self.availList = availList
        self.oList = oList
        self.xList = xList
        
            #   Winning posture (Child list)
        self.ticTakWin = [[1, 2, 3], [4, 5, 6], [7, 8, 9], 
            [1, 4, 7], [2, 5, 8], [3, 6, 9],
            [1, 5, 9], [3, 5, 7] ]  
    
    def isFirstMove(self):
        if (len(self.availList)) >=8:
            return True
        return False
    
        #   Check winning condition 
    def isWin(self, parentList):
        for item in self.ticTakWin:
            if (set(item).issubset(set(parentList))):
                return 1
            
    def isDraw(self):
        if (len(self.availList) == 0):
            return 1
        
    #   Add the X's new position to Xlist and remove from available 
    #   Then undo the above work as we just need to consider state after new X insertion
    def addNewXPosition(self, pos):
        self.availList.remove(pos)
        self.xList.append(pos)
        

    
    def removeNewXPosition(self,pos):
        self.availList.append(pos)
        self.xList.remove(pos)
        
        
    def addNewOPosition(self, pos):
        self.availList.remove(pos)
        self.oList.append(pos)
        

    
    def removeNewOPosition(self,pos):
        self.availList.append(pos)
        self.oList.remove(pos)
        

    def getBestMove(self):
        bestMove = 0    # might give issue
        bestScore = -1000
        count = 0
        
        for item in self.availList:
            self.addNewXPosition(item)  # as its X turn ie bot turn which we try to maximize
            print(self.xList)
            score = self.minimax(item, 0, False)
            print(f"Score : {score}")          
            
            self.removeNewXPosition(item)
            count += 1
            if (score>bestScore):
                bestScore = score
                bestMove = item
        print(f"BEst move is {bestMove}")
        return bestMove
        
    #   Recursive function used for tree implementation
    def minimax(self,pos,depth, isMaximizing):
        
        #   Issue in these checkwin
        if self.isWin(self.xList):
            return 1
        
        if self.isWin(self.oList):
            return -1
        
        if self.isDraw():
            return 0
        
        
        
        
        if isMaximizing:
            bestScore = -1000
            
            for item in range(1,10):
                if item in self.availList:
                    self.addNewXPosition(item)
                    score = self.minimax(item,depth+1, False)
                    self.removeNewXPosition(item)
                    bestScore = max(bestScore, score)

            return bestScore
        
        else:
            
            bestScore = 1000
            
            for item in range(1,10):
                if item in self.availList:
                    self.addNewOPosition(item)
                    score = self.minimax(item, depth+1, True)
                    self.removeNewOPosition(item)
                    bestScore = min(bestScore, score)

            return bestScore
            
        
        
        
        