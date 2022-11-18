import random

def drawboard(board):
    print(' | |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(' | |')
    print('---+---+---')
    print(' | |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(' | |')
    print('---+---+---')
    print(' | |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print(' | |')

def inputplayerlatter():
    letter = ""
    while not (letter == "X" or letter == "O"):
        print('x or O')
        letter = input().upper()
        if letter == "X":
            return ['X','O']
        else:
            return ['O', 'X']
def whofirst():
    if random.randint(0,1) == 0:
        return 'BOT'
    else:
        return 'Player'

def againplay():
    print('again play ? ')
    return input().lower().startswith('y')

def movemake(board,letter,move):
    board[move] = letter

def iswin(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or 
     (bo[4] == le and bo[5] == le and bo[6] == le) or 
     (bo[1] == le and bo[2] == le and bo[3] == le) or 
     (bo[7] == le and bo[4] == le and bo[1] == le) or 
     (bo[8] == le and bo[5] == le and bo[2] == le) or 
     (bo[9] == le and bo[6] == le and bo[3] == le) or 
     (bo[7] == le and bo[5] == le and bo[3] == le) or 
     (bo[9] == le and bo[5] == le and bo[1] == le))

def getcopyboard(board):
    dupeboard = []
    for i in board:
        dupeboard.append(i)
    return dupeboard

def isSpaceFree(board, move):
    return board[move] == ' '

def getplayermove(board):
    move = ''
    while move not in '1,2,3,4,5,6,7,8,9'.split() or not isSpaceFree(board, int(move)):
        print('you 1-9')
        move = input()
    return int(move)

def chooserandommove(board,moveList):
    possiblemove = []
    for i in moveList:
        if isSpaceFree(board, i):
            possiblemove.append(i)
    if len(possiblemove) != 0:
        return random.choice(possiblemove)
    else:
        return None
def getcompmove(board,computerletter):
    if computerletter == "X":
        playerletter = "O"
    else:
        playerletter = "X"
    
    for i in range(1,10):
        copy = getcopyboard(board)
        if isSpaceFree(copy, i):
            movemake(copy,computerletter,i)
            if iswin(copy,computerletter):
                return i

    for i in range(1,10):
        copy = getcopyboard(board)
        if isSpaceFree(copy, i):
            movemake(copy,playerletter,i)
            if iswin(copy, playerletter):
                return i

    move = chooserandommove(board,[1,3,7,9])
    if move != None:
        return move
    
    if isSpaceFree(board,5):
        return 5
    
    return chooserandommove(board,[2,4,6,8])

def isboardfull(board):
    for i in range(1,10):
        if isSpaceFree(board,i):
            return False
    return True

print('go play tic-tac')

while True:
    theboard = [' ']*10
    playerletter,computerletter = inputplayerlatter()
    turn = whofirst()
    print('first'+turn+'\n')
    gameisplaying = True

    while gameisplaying:
        if turn == 'player':
            drawboard(theboard)
            move = getplayermove(theboard)
            movemake(theboard,playerletter,move)
            if iswin(theboard,playerletter):
                drawboard(theboard)
                print('win')
                gameisplaying = False
            else:
                if isboardfull(theboard):
                    drawboard(theboard)
                    print('fail')
                    break
                else:
                    turn = "computer"
        else:
             #pc road
             move = getcompmove(theboard, computerletter)
             movemake(theboard, computerletter, move)
             if iswin(theboard, computerletter):
                 drawboard(theboard)
                 print('bot win')
                 gameIsPlaying = False
             else:
                 if isboardfull(theboard):
                     drawboard(theboard)
                     print('bot fail')
                     break
                 else:
                     turn = 'player'
 
        if not againplay():
          break
