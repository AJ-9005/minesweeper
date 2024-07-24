import random
dug=[]
def home():
    while True:
        start=int(input("Would you like to play?\n1.Yes \n2.No \n"))
        if start==1:
            game()
        elif start==2:
            print("\nGoodbye!")
            break
        else:
            print("\nWrong input!")
def print_board(board_to_print):
    # print((i for i in range(11)),end=" ")
    # for row in range(10):
    #     print("\n")
    #     for col in range(10):
    #         print(col,end="|")
    #         print(board_to_print[row][col],end="|")
       # Print column headers
        # Print column headers
    print("   ", end="")  # Initial spacing for row indices
    for i in range(1, 11):
        print(f"{i:2} ", end=" ")
    print()  # Newline after headers

    # Print a separator line
    print("   " + "----" * 10)

    # Print each row with its index
    for row in range(1, 11):
        print(f"{row:2} |", end=" ")  # Print row index
        for col in range(1, 11):
            print(board_to_print[row - 1][col - 1], end=" | ")
        print()  # Newline after each row
def game():
    board=[[None for _ in range(10)] for _ in range(10)]
    numofbombs=int(input("Enter no of bombs: "))
    bomb_planter(board,numofbombs)
    for row in range(10):
        for col in range(10):
            if board[row][col]!="*":
                square=(row,col)
                num_filler(square,board)
    hidden_board=[[" " for _ in range(10)] for _ in range(10)]
    gameover=0
    while len(dug) != (100 - sum(row.count('*') for row in board)) and gameover==0:
        while True:
            print_board(hidden_board)
                # for rows in hidden_board:
                #     print(rows)
            userinputrow=int(input("\nEnter row: "))
            userinputcol=int(input("Enter col: "))
            if userinputrow+userinputcol>20:
                print("Wrong input!")
            else:
                state=dig(userinputrow-1,userinputcol-1,hidden_board,board)
                if state==-1:
                    gameover=-1
                    break
                elif state==0:
                    continue
                else:
                    gameover=1
                    break
    if gameover==-1:
        print_board(board)
        print("You stepped on a bomb!")
    else:
        print_board(board)
        print("You win!")
def bomb_planter(area,targets):
    bombs_planted=0
    while bombs_planted<targets:
        r=random.randint(0,9)
        c=random.randint(0,9)
        if area[r][c]=="*":
            continue
        else:
            area[r][c]="*"
            bombs_planted+=1
    return area
def num_filler(block,field):
    number=0
    row=block[0]
    col=block[1]
    for r in range(max(0,row-1),min(9,row+1)+1):
        for c in range(max(0,col-1),min(9,col+1)+1):
            if field[r][c]=="*":
                number+=1
    field[row][col]=number
    return field
def dig(row,col,empty,filled):
    result=0
    if filled[row][col]=="*":
        result=-1
    elif filled[row][col]==0:
        empty[row][col]=0
        dug.append((row,col))
        for r in range(max(0,row-1),min(9,row+1)+1):
            for c in range(max(0,col-1),min(9,col+1)+1):
                if (r,c) in dug:
                    continue
                else:
                    dig(r,c,empty,filled)
    elif filled==empty:
        result=1
    else:
        empty[row][col]=filled[row][col]
        result=0
        dug.append((row,col))
    return result,dug
home()