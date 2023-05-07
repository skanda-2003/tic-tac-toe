board=["-","-","-",
       "-","-","-",
       "-","-","-"]

def printBoard(board):
    print(board[0]+"|"+board[1]+"|"+board[2])
    print(board[3]+"|"+board[4]+"|"+board[5])
    print(board[6]+"|"+board[7]+"|"+board[8])
    print()

def playerInput(board,ch):
    ele=int(input("Enter a number from 1-9: "))
    print()
    if ele>=1 and ele<=9 and board[ele-1] == "-":
        board[ele-1]=ch
    else:
        print("Wrong Input")

def winORlose(board,n):
    b=0
    if board[0]==board[3] and board[3]==board[6] and board[3]!="-":
        b=1
    if board[1]==board[4] and board[4]==board[7] and board[4]!="-":
        b=1
    if board[2]==board[5] and board[5]==board[8] and board[5]!="-":
        b=1
    if board[0]==board[1] and board[1]==board[2] and board[11]!="-":
        b=1
    if board[3]==board[4] and board[4]==board[5] and board[4]!="-":
        b=1
    if board[6]==board[7] and board[7]==board[8] and board[7]!="-":
        b=1
    if board[0]==board[4] and board[4]==board[8] and board[4]!="-":
        b=1
    if board[2]==board[4] and board[4]==board[6] and board[4]!="-":
        b=1
    if b:
        print("Player "+str(n)+" wins")
        exit()

while(1):
    if "-" not in board:
        print("It is a tie")
        exit()
    print("Player 1's turn")
    playerInput(board,"X")
    winORlose(board,1)
    printBoard(board)

    if "-" not in board:
        print("It is a tie")
        exit()
    
    print("Player 2's turn")
    playerInput(board,"O")
    winORlose(board,2)
    printBoard(board)