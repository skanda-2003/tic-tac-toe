import numpy as np
board = np.arange(9).reshape(3,3)
print(board)
for i in range(3):
    for j in range(3):
        board[i][j]=0

print(board)

def printBoard(board):
    ch="-"
    for i in range(3):
        for j in range(3):
            if board[i][j]==1:
                ch="X"
            elif board[i][j]==2:
                ch="O"
            else:
                ch="-"
            if j==2:
                print(ch,end="\n")
            else:
                print(ch,end="|")
    print()
                

def playerInput(board,n):
    """row,col=int(input("Enter row and col: ")),int(input())"""
    print("Enter row and col:")
    row=int(input())
    col=int(input())
    print()
    if row>=1 and row<=3 and col>=1 and col<=3 and board[row-1][col-1] == 0:
        board[row-1][col-1]=n
    else:
        print("Wrong Input")
        playerInput(board,n)

def winORlose(board,n):
    b=0
    if board[0][0]==board[1][0] and board[1][0]==board[2][0] and board[1][0]!=0:
        b=1
    if board[0][1]==board[1][1] and board[1][1]==board[2][1] and board[1][1]!=0:
        b=1
    if board[0][2]==board[1][2] and board[1][2]==board[2][2] and board[1][2]!=0:
        b=1
    if board[0][0]==board[0][1] and board[0][1]==board[0][2] and board[0][1]!=0:
        b=1
    if board[1][0]==board[1][1] and board[1][1]==board[1][2] and board[1][1]!=0:
        b=1
    if board[2][0]==board[2][1] and board[2][1]==board[2][2] and board[2][1]!=0:
        b=1
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[1][1]!=0:
        b=1
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]!=0:
        b=1
    if b:
        print("Player "+str(n)+" wins")
        exit()

while(1):
    if 0 not in board:
        print("It is a tie")
        exit()
    print("Player 1's turn")
    playerInput(board,1)
    winORlose(board,1)
    printBoard(board)

    if 0 not in board:
        print("It is a tie")
        exit()
    
    print("Player 2's turn")
    playerInput(board,2)
    winORlose(board,2)
    printBoard(board)