import copy
import numpy as np

EMPTY = 'LIVRE'
board = [[EMPTY, 'X', 'O'],
         [EMPTY, 'O', 'X'],
         ['O', 'O', 'X']]


valido = 0
tam = int(len(board))
print('////////////////////////////////////////////////////////////////////')

for i in range(tam):
    for j in range(tam):
        if board[i][j] != EMPTY:
            valido += 1

if valido < pow(tam, 2):
    if valido % 2 == 0:
        print('vez de X')
    else:
        print('vez de O')



print('////////////////////////////////////////////////////////////////////')

tam = len(board)
list_possibility = set()
for i in range(tam):
    for j in range(tam):
        if board[i][j] == EMPTY:
            list_possibility.add((i,j))

print(list_possibility)

print('////////////////////////////////////////////////////////////////////')
action = (2,1)
if action not in list_possibility:
    print('INVALIDO')
ii = action[0]
jj = action[1]
newboard = copy.deepcopy(board)
newboard[ii][jj] = 'X'

print('////////////////////////////////////////////////////////////////////')

def linhasecolunas(board): # Check lines
    tam = len(board)
    for i in range(tam):
        checar = True
        for item in board[i]:
            if item == EMPTY:
                checar = False
                break
        if checar: # Só checo as linhas que nao estao vazias
            chk = True
            ele = board[i][0]
            for item in board[i]:
                if ele != item:
                    chk = False
                    break
            if (chk == True):
                return ele
    return None

def winner(board): # Returns the winner of the game, if there is one.

    winner_row = linhasecolunas(board) # ROW
    if winner_row:
        return winner_row

    arr1 = np.array(board)
    arr1_transpose = arr1.transpose()
    winner_col = linhasecolunas(arr1_transpose.tolist()) # COLUMN
    if winner_col:
        return winner_col

    tam = len(board)
    diag1 = []
    k = int(tam) - 1
    diag2 = []

    for i in range(tam):
        for j in range(tam):
            if i == j:
                diag1.append(board[i][j]) # DIAGONAL
            elif i == (j - k):
                diag2.append(board[i][j]) # DIAGONAL2
                k -= 2
    chk = True
    ele = diag1[0]
    for item in diag1:
        if item != ele:
            chk = False
    if chk:
        return ele

    chk = True
    ele = diag2[0]
    for item in diag2:
        if item != ele:
            chk = False
    if chk:
        return ele

    return None


print(winner(board))


'''
k = int(tam) - 1
diag1 = []
diag2 = []
for i in range(tam):
    for j in range(tam):
        if i == j:
            diag1.append(board[i][j])
        if i == (j - k):
            diag2.append(board[i][j])
            k -= 2
print(diag1)
print(diag2)
chk = True
ele = diag1[0]
for item in diag1:
    if item != ele:
        chk = False
if chk:
    print(ele)
'''