def printBoard(board):
    print()
    for i in range(3):
        print(board[i], end=" ")
    print()
    for i in range(3, 6):
        print(board[i], end=" ")
    print()
    for i in range(6, 9):
        print(board[i], end=" ")
    print()
        

def getSpace(board):
    valid = False
    while not valid: 
        space = int(input("\n\nPick an open space (1-9)\n"))
        if space > 9 or space < 1:
            print("ERROR. Input a number between 1 and 9.")
        elif board[int(space) - 1] == 0:
            valid = True
            return space
        else:
            print("ERROR. This space is already filled.") 


def playTurn(board, space):
    # determine whose turn based on numbers of open spaces left 
    if board.count(0) % 2 != 0:
        board[space - 1] = "X"
    else:
        board[space - 1] = "O"
    return board


def checkWin(board):
    # check row win
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] and board[i] != 0:
            return True
    
    # check column win
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] and board[i] != 0:
            return True

    # check diagonal win
    if board[4] != 0:
        if board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:
            return True
    
    # else
    return False


def shouldContinue():
    validInput = False
    while not validInput:
        keepPlaying = input("Would you like to keep playing (y/n)?\n").lower()
        if keepPlaying == "y":
            validInput = True
            return True
        elif keepPlaying == "n":
            validInput = True
            return False
        else:
            print("Invalid input.")


def main():
    keepPlaying = True
    while keepPlaying:
        board = [0,0,0,0,0,0,0,0,0]
        printBoard(board)
        win = checkWin(board)
        while win == False:
            space = int(getSpace(board))
            playTurn(board, space)
            printBoard(board)
            win = checkWin(board)
        print("We have a winner!")
        keepPlaying = shouldContinue()
    print("Goodbye!")


main()


