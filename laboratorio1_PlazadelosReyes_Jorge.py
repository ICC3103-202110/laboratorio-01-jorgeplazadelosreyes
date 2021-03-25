from numpy import *
cards = []
scorep1 = 0
scorep2 = 0
n = int(input('Numero de cartas a jugar: '))
a = n+1

for i in range(a):
    if i > 0:
        cards.append(i)
        cards.append(i)

def row_and_column(n):
    root = (n*2)**(1/2)
   
    if root % int(root) == 0:
        row = root
        col = root
        return row, col
    else:
        row = 0
        col = 0
        n1 = int(root)
        n2 = int(root)+1
        while row == 0 and col == 0:
            if n*2 % n1 == 0:
                row = n1
            else:
                n1 += -1
            if n*2 % n2 == 0:
                col = n2
            else:
                n2 += 1
        return row,col

def create_board1(row,col):
    board1 = []
    for i in range(col):
        line = []
        for j in range(row):
            line.append('*')
        board1.append(line)
    return board1

def create_board2(row,col,cards):
    board2 = []
    for i in range(col):
        line = []
        for j in range(row):
            if len(cards) == 1:
                line.append(cards[0])
            else:
                r = random.randint(len(cards)-1)
                line.append(cards[r])
                cards.pop(r)
        board2.append(line)
    return board2

def show_board(board1,row,col):
    for i in range(row):
      line = ''
      for j in range(col):
        line += str(board1[j][i]) + " "
      print(line)

def check_coordenates(c1,c2,row,col):
    c1 = c1.split(',')
    c2 = c2.split(',')

    if (int(c1[0]) < 0 or int(c2[0]) < 0):
        return False
    if (int(c2[1]) < 0 or int(c2[1]) < 0):
        return False
    if (int(c1[0]) > (col-1) or int(c2[0]) > (col-1) ):
        return False
    if (int(c2[1]) > (row-1) or int(c2[1]) > (row-1)):
        return False
    return True





row = row_and_column(n)[0]
col = row_and_column(n)[1]

board1 = create_board1(row,col)
board2 = create_board2(row,col,cards)
show_board(board1,row,col)
print('\n')
show_board(board2,row,col)
print(board2[0][0])
print(board2[0][1])

print("Comienza el juego\nJugador 1 empieza\n")
while True:
    print("Puntaje jugador 1:", scorep1)
    print("Puntaje jugador 2:", scorep2)
    c1 = input("Jugador 1 ingrese coordenadas de su primera carta con coma y sin parentesis: ")
    c2 = input("Ingrese coordenadas segunda carta con coma y sin parentesis: ")
    while not check_coordenates(c1, c2, row, col):
        print("coordenadas invalidas")
        c1 = input("Jugador 1 ingrese coordenadas de su primera carta con coma y sin parentesis: ")
        c2 = input("Ingrese coordenadas segunda carta con coma y sin parentesis: ")
        check_coordenates(c1, c2, row, col)
    c1 = c1.split(',')
    c2 = c2.split(',')
    board1[int(c1[0])][int(c1[1])] = board2[int(c1[0])][int(c1[1])]
    board1[int(c2[0])][int(c2[1])] = board2[int(c2[0])][int(c2[1])]

    show_board(board1, row, col)
    r = input()
    if r == 'salir':
        break










