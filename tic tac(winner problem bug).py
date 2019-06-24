import os
import time
board = [['-','-','-'],
         ['-','-','-'],
         ['-','-','-'],]

'''def board(row=0,col=0):
    print("   a  b  c")
    for i in range(3):
        print(i,board[i])
            
board()'''

def markit(row,col,mark):
    try:
        if board[row-1][col-1]!='-':
            print("Already Marked!!")
            time.sleep(1)
        else:
            board[row-1][col-1]=mark
    except IndexError:
        print("Out of Range...Reverting back")
        time.sleep(1)
def reset():
    global board
    board = [['-','-','-'],
             ['-','-','-'],
             ['-','-','-'],]

def check():
    def hor_win():
        i,j,k=0,0,0
        for i in range(len(board)):
            x=board[i][0]
            for j in range(len(board)):  
                if x==board[i][j]:
                    k+=1
            if k==3:
                print(board[i][0]," is a winner")
                time.sleep(1.5)
                y=input("Play Again?(y/n):")
                if y==y:
                    reset()
                else:
                    quit()
                break   

'''def check():
    for i in range(len(board)):
        if board[i][i]==board[i-1][i-1] and board[i][i]!='-':
            print(board[i][i]," is a winner")
            time.sleep(1.5)
            y=input("Play Again?(y/n):")
            if y==y:
                reset()
            else:
                quit()
            break

'''




while True:
    print("    1    2    3")
    for i in range(len(board)):
        print(i+1,board[i])      
    row=int(input("P1||Enter row:"))
    col=int(input("P1||Enter col:"))
    markit(row,col,mark='X')
    check()
    os.system('cls')
    print("    1    2    3")
    for i in range(len(board)):
        print(i+1,board[i])
    row=int(input("P2||Enter row:"))
    col=int(input("P2||Enter col:"))
    markit(row,col,mark='O') 
    check()
    os.system('cls')   
