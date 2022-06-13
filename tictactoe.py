def createZeroMatrix(r,c):
    output = []
    for i in range(r):
        row = []
        for j in range(c):
            row.append(0)
        output.append(row)
    return output

def printTTT(game):
    for i in range(3):
        print(f'{game[i][0]}|{game[i][1]}|{game[i][2]}')
        if i !=2:
            print( '-----')
piece = ['X','O']

def checkValidMove(game,inp):
    # A valid input must be between 1 to 9, and cannot have been previously selected
    if inp < 1 or inp > 9: # out of valid range
        return False
    elif game[(inp-1)//3][(inp-1)%3] == 'X' or game[(inp-1)//3][(inp-1)%3] == 'O':
        return False
    else:
        return True

def checkWin(game):
    
    # check for horizontal win
    for row in range(len(game)): # for each row
        if all(c == 'X' for c in game[row]): # check if all columns are 'X'
            #print('Player X won!')
            return 'X'
        elif all(c == 'O' for c in game[row]): # similarly for 'O'
            #print('Player O won!')
            return 'O'

    # check for vertical win
    for col in range(len(game[0])): # for each column
        if all(r[col] == 'X' for r in game): # check if all rows are 'X'
            #print('Player X won!')
            return 'X'
        elif all(r[col] == 'O' for r in game): # check if all rows are 'X'
            #print('Player O won!')
            return 'O'
        
    # check for diagonal win
    diagonal1 = [] # initialize
    diagonal2 = [] # initialize
    for row in range(len(game)):
        for col in range(len(game[0])):
            if row == 1 and col == 1:
                diagonal1.append(game[row][col])
                diagonal2.append(game[row][col])
            elif row == col:
                diagonal1.append(game[row][col])
            elif row == 2 - col or col == 2 - row:
                diagonal2.append(game[row][col])
    diagonals = [diagonal1, diagonal2]
    #print(diagonals) # for checking only
    for row in range(len(diagonals)):
        if all(c == 'X' for c in diagonals[row]):
            #print('Player X won!')
            return 'X'
        elif all(c == 'O' for c in diagonals[row]):
            #print('Player O won!')
            return 'O'

    return False


def tttGamePlay():
    game = createZeroMatrix(3,3)
    for i in range(3):
        for j in range(3):
            game[i][j] = i*3+j+1
    player = 0

    printTTT(game)
    for i in range(9): 
        print()
        inp = int(input(f'Player {piece[player]} move:'))
        while checkValidMove(game,inp) == False:
            print('Invalid Move!')
            inp = int(input(f'Player {piece[player]} move:'))
        pos = inp - 1
        game[pos//3][pos%3] = piece[player]
        printTTT(game)
        winner = checkWin(game)
        if checkWin(game) != False:
            print(f'Player {winner} won!')
            break
        player = 1 - player

