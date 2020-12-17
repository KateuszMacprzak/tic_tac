board=[' ' for x in range(10)] 
#all the 9 positions are inputs
#to jest lista, w której to mamy pustą pozycję, ale w samym programie ma tam być X/O, które wprowadzi użytkownik

def insertLetter(letter, pos): #pos=position
    board[pos]= letter  #pos to zmienna dla pozycji, dzięki niej określimy jaki numer chcemy podać
    #space in this position will be equal to letter
    #nie potrzebujemy nic więcej, po prostu ta konkretna pozcycja będzie zastąpiona literą

def spaceIsFree(pos): #we hace to use pos(position), becouse the space will be free for particular position
    return board [pos]==' ' #when the space is free, then it's returning true

def printBoard(board):
    print('   |   |   ')
    print(' '+ board[1] + ' | '+board[2]+' | '+board[3])   #tutaj mamy zaznaczone pierwsze 3 elementy z listy board, mamy dla nich puste przestrzenie, które wprowadzamy
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

def IsWinner(b,l):
    return (b[1] == l and b[2] == l and b[3] == l) or  #l is x/o, l=letter
    (b[4] == l and b[5] == l and b[6] == l) or 
    (b[7] == l and b[8] == l and b[9] == l) or 
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or 
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l)

def playerMove():
    run = True 
    while run:
        move = input('please select a position to etner the X between 1 to 9: ')
        try: #poniżej wszystko bedzie działało, gdy użykownik wpisze liczbę, w innym przypadku mamy except 
            move = int(move) #to jest zmiana typu input move z string na int 
            if move > 0 and move <10: #to jest zmienna, która skupia się na tym, aby ruch użykownika był  w zakresie 1-9
                if spaceIsFree(move): # to jest funkcja sprawdzająca wolną przestrzeń, jeżeli taka jest to wtedy wykonują się kolejne instrukcje 
                    run=False          #to dzieję się tylko wtedy,  jeżeli ta konkretna (1-9) przestrzeń jest wolna 
                    insertLetter('X', move) #x to znak użykownika, a pos, na którym jest zdefiniowa funkcja move użykownik wprowadza na początku
                else: #jeżeli pozycja jest zajęta, to wtedy wyskakuje nam komunikat, że ta pozycja jest zajęta. Działa na podstawie funkcji spaceIsFree
                    print('Sorry, this space is occupied') 
            else:
                print("Please type a number between 1 and 9 ") # to jest komunikat, który będzie, gdy użykownik wpisze liczbę, która nie jest w zakresie 
        except:
            print('Please type a number')  #to się dzieję, gdy użytkownik wpiszę słowa zamiast liczb

def computerMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x!=0 ] #jeżeli te warunki są spełnione, funkcja enumerate wstawia ruch komputera w pustą pozycję, i jest różna od 0(gdyż ta liczba może być w zasięgu)
    move = 0

    for let in ['O', 'X']: #here we checking by taking variable by 'let' and that's perform a list in which we have two elements-'O' and 'X'
        for i in possibleMoves: 
            boardcopy = board[:] #to jest wyświetlenie ostatniego ruchu lub na początku pustej tablicy
            boardcopy[i]=let #and here we update list in this particular location
            if IsWinner(boardcopy, let):
                move=i
                return move
    #_________SZTUCZNA INTELIGENCJA KOMPUTERA_____________            
    cornersOpen=[] #nazwa listy, tutaj zapisują się narożniki
    for i in possibleMoves: #dla każdego z możliwych ruchów do wykonania
        if i in [1, 3, 7, 9]: #jeżeli element jest w pozycjach 1,3,7,9
            cornersOpen.append(i) #wtedy komputer dodaje możliwość ruchu do listy
    if len(cornersOpen) > 0: #system sprawdza czy jest jakaś możliwość w tym zakresie, w tym przypadku są to narożniki
        move = selectRandom(cornersOpen) #tutaj jest losowy wybór z tych pozycji wskazanych wyżej
        return move #zwraca tę wartość jako move
    
    if 5 in possibleMoves: #jeżeli pozycja numer 5 jest w możliwościach
        move = 5 #wtedy ruch będzie jako 5
        return move #i tutaj się zwraca
    
    edgesOpen = [] #pusta lista dla krawędzi 
    for i in possibleMoves: 
        if i in [2,4,6,8]: #jeżeli pusta przestrzeń jest w możliwych, pustych pozycjach 
            edgesOpen.append(i) #wtedy do listy możliwych ruchów dodaje się pustą pozycję
    if len(edgesOpen) > 0: #system sprawdza czy jest jakaś możliwość w tym zakresie, w tym przypadku są to krawędzie
        move = selectRandom(edgesOpen) #wtedy ruch jest losdowo wybierany z narożników
        return move #tutaj jest on zwracany 

