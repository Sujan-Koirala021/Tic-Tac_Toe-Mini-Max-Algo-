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
        bestMove = 0    
        bestScore = -1000
        
        #   X is the bot in this game 
        #   In X(bot) turn we try to maximize the result
        
        for item in range(1,10):
            if item in self.availList:
                
                #   Evaulate every available positions
                self.addNewXPosition(item)  # as its X(bot) turn ,we try to maximize

                score = self.minimax(item, 0, False) #  'False' recursive call to next turn where bot(X) minimizes result to return score
                
                self.removeNewXPosition(item)
                
                if (score>bestScore):
                    bestScore = score
                    bestMove = item
                
        return bestMove
        
    #   Recursive function used for tree implementation
    def minimax(self,pos,depth, isMaximizing):
        
        #   Termination condition(game lost or won or draw) for recursive call
        if self.isWin(self.xList):
            return 1
        
        if self.isWin(self.oList):
            return -1
        
        if self.isDraw():
            return 0
        
        
        
        if isMaximizing:
            #   Find high score
            bestScore = -1000
            
            for item in range(1,10):
                if item in self.availList:
                    self.addNewXPosition(item)
                    score = self.minimax(item,depth+1, False)   # in next turn, we minimize as it is O's turn
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
            
        
        
        
        