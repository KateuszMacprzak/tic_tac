board=[' ' for x in range(10)] 
#instead of define it again and again we make a loop in this list

def insertLetter(letter, pos): #pos=position
    board[pos]= letter  #if user click '6', then we will get position number 6
    #position is equal to letter

def printBoard(board):
    print('   |   |   ')
    print(' '+ board[1] + ' | '+board[2]+' | '+board[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' '+ board[4] + ' | '+board[5]+' | '+board[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' '+board[7]+' | '+board[8]+' | '+board[9])
    print('   |   |   ')
print(printBoard)