board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentplayer = "X"
winner = None
gamerunning = True

def printboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

def input_user(board):
    num = int(input("Enter  a number between 1-9:"))
    if num >= 1 and num<=9 and board[num-1] == "-":
        board[num-1] = currentplayer
    else:
        print("oops player is already their!")

def checkhorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
         winner = board[3]
         return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
         winner = board[6]
         return True

def checkvertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
         winner = board[0]
         return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
         winner = board[1]
         return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkdiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def checktie(board):
    if "-" not in board:
        printboard(board)
        print("It's a Tie!")
        gamerunning = False

def checkwin():
    if checkhorizontal(board) or checkvertical(board) or checkdiagonal(board):
        gamerunning = False
        return True

def switch():
    global currentplayer
    if currentplayer == "X":
        print("player2's Turn")
        currentplayer = "O"
    else:
        print("player1's Turn")
        currentplayer = "X"    

        

while gamerunning:
    printboard(board)
    input_user(board)
    if checkwin() == True:
        printboard(board)
        print(f"The winner is {winner}")
        break
    checktie(board)
    switch()


