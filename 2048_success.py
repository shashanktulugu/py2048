import random
import copy

board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

boardSize = 4
def display():
    largest = board[0][0]
    for row in board:
        for element in row:
            if element > largest:
                largest = element
    numSpaces = len(str(largest))

    for row in board:
        currRow = "|"
        for element in row:
            if element == 0:
                currRow += " " * numSpaces + "|"
            else:
                currRow += (" " * (numSpaces - len(str(element)))) + str(element) + "|"
        print(currRow)
    print()

display()

def mergeOneRowL(row):

    for j in range(boardSize - 1):
        for i in range(boardSize - 1, 0, -1):

            if row[i - 1] == 0:
               row[i - 1] = row[i]
               row[i] = 0

    for i in range(boardSize - 1):
        if row[i] == row[i + 1]:
            row[i] *= 2
            row[i + 1] = 0

    for i in range(boardSize - 1, 0, -1):
        if row[i - 1] == 0:
            row[i - 1] =row[i]
            row[i] = 0
    return row

def merge_left(currentBoard):
    for i in range(boardSize):
        currentBoard[i] = mergeOneRowL(currentBoard[i])

    return currentBoard

def reverse(row):

    new = []
    for i in range(boardSize - 1, -1, -1):
        new.append(row[i])
    return new

def merge_right(currentBoard):

    for i in range(boardSize):

        currentBoard[i] = reverse(currentBoard[i])
        currentBoard[i] = mergeOneRowL(currentBoard[i])
        currentBoard[i] = reverse(currentBoard[i])
    return currentBoard

def transpose(currentBoard):
    for j in range(boardSize):
        for i in range(j, boardSize):
            if not i == j:
                temp = currentBoard[j][i]
                currentBoard[j][i] = currentBoard[i][j]
                currentBoard[i][j] = temp
    return currentBoard

def merge_up(currentBoard):

    currentBoard = transpose(currentBoard)
    currentBoard = merge_left(currentBoard)
    currentBoard = transpose(currentBoard)

    return currentBoard

def merge_down(currentBoard):

    currentBoard = transpose(currentBoard)
    currentBoard = merge_right(currentBoard)
    currentBoard = transpose(currentBoard)

    return currentBoard


def picknewvalue():
    if random.randint(1, 8) == 1:
        return 4
    else:
        return 2

def addnewvalue():
    rownum = random.randint(0, boardSize - 1)
    colnum = random.randint(0, boardSize - 1)

    while not board[rownum][colnum] == 0:
        rownum = random.randint(0, boardSize - 1)
        colnum = random.randint(0, boardSize - 1)

    board[rownum][colnum] = picknewvalue()
def won():
    for row in board:
        if 2048 in row:
            return  True
    return False

def nomoves():
    tempboard1 = copy.deepcopy(board)
    tempboard2 = copy.deepcopy(board)

    tempboard1 = merge_down(tempboard1)
    if tempboard1 == tempboard2:
        tempboard1 = merge_up(tempboard1)
    if tempboard1 == tempboard2:
        tempboard1 = merge_left(tempboard1)
        if tempboard1 == tempboard2:
            tempboard1 = merge_right(tempboard1)
            if tempboard1 == tempboard2:
                return True
    return False


board = []
for i in range(boardSize):
    row = []
    for j in range(boardSize):
        row.append(0)
    board.append(row)

nums = 2
while nums > 0:
    rownum = random.randint(0, boardSize - 1)
    colnum = random.randint(0, boardSize - 1)

    if board[rownum][colnum] == 0:
        board[rownum][colnum] = picknewvalue()
        nums -= 1

print("hi this is 2048 game. type d to right , a to left , s to down and w to up to merge numbers accordingly")

display()

gameover = False

while not gameover:
    move = input(" which direction want to move")

    validinput = True


    tempboard = copy.deepcopy(board)

    if move == "d":
        board = merge_right(board)
    elif move == "w":
        board = merge_up(board)
    elif move == "a":
        board = merge_left(board)
    elif move == "s":
        board = merge_down(board)
    else:
        validinput = False


    if not validinput:
        print("input wrong, try other")

    else:
        if board == tempboard:
            print("try some another direction!")
        else:
           if won():
               display()
               print("won")
               gameover = True

           else:

             addnewvalue()

           display()

           if nomoves():
               print("lost")
               gameover = True