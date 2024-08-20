import random
dug = []
def home():
    while True:
        start = int(input("Would you like to play?\n1.Yes \n2.No \n"))
        if start == 1:
            game()
        elif start == 2:
            print("\nGoodbye!")
            break
        else:
            print("\nWrong input!")
def print_board(board_to_print):
    print("   ", end="")
    for i in range(1, 11):
        print(f"{i:2} ", end=" ")
    print() 
    print("   " + "----" * 10)
    for row in range(1, 11):
        print(f"{row:2} |", end=" ")  
        for col in range(1, 11):
            print(board_to_print[row - 1][col - 1], end=" | ")
        print()
def game():
    global dug
    dug = []
    board = [[None for _ in range(10)] for _ in range(10)]
    numofbombs = int(input("Enter number of bombs: "))
    bomb_planter(board, numofbombs)
    for row in range(10):
        for col in range(10):
            if board[row][col] != "*":
                square = (row, col)
                num_filler(square, board)
    hidden_board = [[" " for _ in range(10)] for _ in range(10)]
    gameover = 0
    total_cells = 100
    safe_cells = total_cells - numofbombs
    
    while len(dug) != safe_cells and gameover == 0:
        print_board(hidden_board)
        try:
            userinputrow = int(input("\nEnter row (1-10): "))
            userinputcol = int(input("Enter col (1-10): "))
        except ValueError:
            print("Invalid input! Please enter numbers.")
            continue
        if not (1 <= userinputrow <= 10) or not (1 <= userinputcol <= 10):
            print("Invalid input! Please enter numbers between 1 and 10.")
            continue
        state = dig(userinputrow - 1, userinputcol - 1, hidden_board, board)
        if state == -1:
            gameover = -1
        elif len(dug) == safe_cells:
            gameover = 1
    if gameover == -1:
        print_board(board)
        print("You stepped on a bomb! Game over.")
    else:
        print_board(board)
        print("Congratulations! You win!")

def bomb_planter(area, targets):
    bombs_planted = 0
    while bombs_planted < targets:
        r = random.randint(0, 9)
        c = random.randint(0, 9)
        if area[r][c] == "*":
            continue
        else:
            area[r][c] = "*"
            bombs_planted += 1
    return area
def num_filler(block, field):
    number = 0
    row = block[0]
    col = block[1]
    for r in range(max(0, row - 1), min(9, row + 1) + 1):
        for c in range(max(0, col - 1), min(9, col + 1) + 1):
            if field[r][c] == "*":
                number += 1
    field[row][col] = number
    return field
def dig(row, col, empty, filled):
    if filled[row][col] == "*":
        empty[row][col] = "*"
        return -1
    elif filled[row][col] == 0:
        empty[row][col] = 0
        dug.append((row, col))
        for r in range(max(0, row - 1), min(9, row + 1) + 1):
            for c in range(max(0, col - 1), min(9, col + 1) + 1):
                if (r, c) in dug:
                    continue
                dig(r, c, empty, filled)
    else:
        empty[row][col] = filled[row][col]
        dug.append((row, col))
    return 0

home()