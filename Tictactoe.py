import random

#returns the winner
def isWinner(array):
    noneValue = 0
    for i in range(0,3):
        for j in range(0,3):
            if(array[i][j] == "-"):
                noneValue = noneValue + 1
    if(array[0][0] == array[0][1] == array[0][2] != "-"):
        return array[0][0]
    elif(array[1][0] == array[1][1] == array[1][2] != "-"):
        return array[1][0]
    elif(array[2][0] == array[2][1] == array[2][2] != "-"):
        return array[2][0]
    elif(array[0][0] == array[1][0] == array[2][0] != "-"):
        return array[0][0]
    elif(array[0][1] == array[1][1] == array[2][1] != "-"):
        return array[0][1]
    elif(array[0][2] == array[1][2] == array[2][2] != "-"):
        return array[0][2]
    elif(array[0][0] == array[1][1] == array[2][2] != "-"):
        return array[0][0]
    elif(array[0][2] == array[1][1] == array[2][0] != "-"):
        return array[0][2]
    elif(noneValue == 0):
        return "Tie"

def gameOver(array):
    check = isWinner(array)
    if(check == "X" or check == "O" or check == "Tie"):
        return True
    else:
        return False

def boardPrint(array):
    for i in range(0,3):
        print(array[i][0],"|", array[i][1],"|", array[i][2])
    print("\n")

def miniMax(array,depth,maximizer):
    #checking if the game is over
    over = gameOver(array)
    if(over == True):
        #evaluation function
        score = 0
        winner = isWinner(array)
        if(winner == "X"):
            score = 10
        elif(winner == "O"):
            score = -10
        else:
            score = 0
        return score
    if(maximizer):
        bestScore = -1000
        for i in range(0,3):
            for j in range(0,3):
                if(Game[i][j] == "O" or Game[i][j] == "X"):
                    continue
                else:
                    Game[i][j] = "X"
                    score = miniMax(array,depth + 1,False)
                    Game[i][j] = "-"
                    bestScore = max(score,bestScore)
        return bestScore
    else:
        bestScore = 1000
        for i in range(0,3):
            for j in range(0,3):
                if(Game[i][j] == "O" or Game[i][j] == "X"):
                    continue
                else:
                    Game[i][j] = "O"
                    score = miniMax(array,depth + 1,True)
                    Game[i][j] = "-"
                    bestScore = min(score,bestScore)
        return bestScore
    




#MAIN    
Game = [["-","-","-"],["-","-","-"],["-","-","-"]]

bestRow = 0
bestColumn = 0
while(True):
    
    print("X's turn. Complete the position of X")
    
    #Player turn
    while(True):
        print("Insert the number of row")
        rowInput = int(input())
        print("Insert the number of column")
        columnInput = int(input())
        if(Game[rowInput-1][columnInput-1] == "O" or Game[rowInput-1][columnInput-1] == "X"):
            print("Invalid entry\n")
            print("Insert again the position of X")
        else:
            Game[rowInput-1][columnInput-1] = "X"
            break
    
    boardPrint(Game)
    
    over1 = gameOver(Game)
    if(over1 == True):
        winner = isWinner(Game)
        if(winner == "X" or winner == "O"):
            print("Game Over,",winner,"is the winner\n")
        else:
            print("Game Over, it's a tie\n") 
        break


    #AI turn
    bestScore = 1000
    print("O's turn")
    for i in range(0,3):
        for j in range(0,3):
            if(Game[i][j] == "O" or Game[i][j] == "X"):
                continue
            else:
                Game[i][j] = "O"
                score = miniMax(Game,0,True)
                Game[i][j] = "-"
                if(score < bestScore):
                    bestScore = score
                    bestRow = i
                    bestColumn = j
    Game[bestRow][bestColumn] = "O"
    boardPrint(Game)
    over2 = gameOver(Game)
    if(over2 == True):
        winner = isWinner(Game)
        if(winner == "X" or winner == "O"):
            print("Game Over,",winner,"is the winner\n")
        else:
            print("Game Over, it's a tie\n") 
        break
