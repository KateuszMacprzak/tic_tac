board=[' ' for x in range(10)] 
#instead of define it again and again we make a loop in this list

def insertLetter(letter, pos): #pos=position
    board[pos]= letter  #if user click '6', then we will get position number 6
    #position is equal to letter

def spaceIsFree(pos): #we hace to use pos(position), becouse the space will be free for particular position
    return board [pos]==' ' #when the space is free, then it's returning true

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

#this function is check is board full or not 
def isBoardFull(board): #here we use board value, becouse we use it only when the board is full
    if board.count(' ') > 1: #tutaj wywołujemy funkcję, która sprawdza dokładną ilość czegoś
        # w naszym przypadku sprawdza ona czy w tablicy są puste przestrzenie
        return False #to jest przypadek, gdy tablica nie jest pełna
    else:
        return True #to jest przypadek, gdy tablica jest pełna