from numpy import *
cards = []
scorep1 = 0
scorep2 = 0
n = int(input('Numero de cartas a jugar: '))
a = n+1
print("LEER ANTES DE JUGAR: EXPLICACION COORDENADAS\n 0,0 1,0 2,0 ...\n 0,1 1,1 2,1 ...\n 0,2 1,2 2,2 ...\n ... ... ... ...")
j = str(input("Empezar juego?(s/n): "))
while j != 's':
    j = str(input("Empezar juego?(s/n): "))
    
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
        while row == 0 or col == 0:
            if n*2 % n1 == 0:
                row = int(n1)
            else:
                n1 += -1
            if n*2 % n2 == 0:
                col = int(n2)
            else:
                n2 += 1
        return row,col

def create_board1(row,col):
    board1 = []
    for i in range(int(col)):
        line = []
        for j in range(int(row)):
            line.append('*')
        board1.append(line)
    return board1

def create_board2(row,col,cards):
    board2 = []
    for i in range(int(col)):
        line = []
        for j in range(int(row)):
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

def check_coordenates(c1,row,col):
    c1 = c1.split(',')
    if (int(c1[0]) < 0 or int(c1[1]) < 0):
        return False
    if (int(c1[0]) > (col-1)):
        return False
    if (int(c1[1]) > (row-1)):
        return False
    n1 = board1[int(c1[0])][int(c1[1])]
    if n1 != "*":
        return False
    return True



row = int(row_and_column(n)[0])
col = int(row_and_column(n)[1])
board1 = create_board1(row,col)
board2 = create_board2(row,col,cards)
print("\nComienza el juego\nJugador 1 empieza\n")
show_board(board1,row,col)
contador = 0
r = False
while True:
    p1 = True
    p2 = False
    while p1:
        if contador == (n*2):
            r = 'salir'
            break
        print("\nPuntaje jugador 1:", scorep1)
        print("Puntaje jugador 2:", scorep2)
        c1 = input("\nJugador 1 ingrese coordenadas de su primera carta con coma y sin parentesis: ")
        while not check_coordenates(c1,row,col):
            print("coordenadas invalidas\n")
            show_board(board1, row, col)
            c1 = input("Jugador 1 ingrese coordenadas de su primera carta con coma y sin parentesis: ")
            check_coordenates(c1,row, col)
        c1 = c1.split(',')
        board1[int(c1[0])][int(c1[1])] = board2[int(c1[0])][int(c1[1])]
        show_board(board1, row, col)
        c2 = input("\nJugador 1: Ingrese coordenadas segunda carta con coma y sin parentesis: ")
        while not check_coordenates(c2,row,col):
            print("coordenadas invalidas\n")
            show_board(board1, row, col)
            c2 = input("Jugador 1: Ingrese coordenadas de su segunda carta con coma y sin parentesis: ")
            check_coordenates(c2,row, col)
        c2 = c2.split(',')
        board1[int(c2[0])][int(c2[1])] = board2[int(c2[0])][int(c2[1])]
        show_board(board1, row, col)
        n1 = board2[int(c1[0])][int(c1[1])]
        n2 = board2[int(c2[0])][int(c2[1])]
        if n1 == n2:
            print("\nCorrecto!")
            scorep1 += 1
            board1[int(c1[0])][int(c1[1])] = " "
            board1[int(c2[0])][int(c2[1])] = " "
            contador += 2
            if contador == (n*2):
                r = 'si'
                break
            print("\nTienes otro turno")
            continue
        else:
            print("\nIncorrecto")
            board1[int(c1[0])][int(c1[1])] = "*"
            board1[int(c2[0])][int(c2[1])] = "*"
            p1 = False
            p2 = True
            print("\nTurno del jugador 2\n")
            show_board(board1,row,col)
            break
    if r == 'si':
        break
    while p2:
        if contador == (n*2):
            r = 'salir'
            break
        print("\nPuntaje jugador 1:", scorep1)
        print("Puntaje jugador 2:", scorep2)
        c1 = input("\nJugador 2: Ingrese coordenadas de su primera carta con coma y sin parentesis: ")
        while not check_coordenates(c1,row,col):
            print("coordenadas invalidas\n")
            show_board(board1, row, col)
            c1 = input("Jugador 2: Ingrese coordenadas de su primera carta con coma y sin parentesis: ")
            check_coordenates(c1,row, col)
        c1 = c1.split(',')
        board1[int(c1[0])][int(c1[1])] = board2[int(c1[0])][int(c1[1])]
        show_board(board1, row, col)
        c2 = input("\nJugador 2: Ingrese coordenadas segunda carta con coma y sin parentesis: ")
        while not check_coordenates(c2,row,col):
            print("Coordenadas invalidas\n")
            show_board(board1, row, col)
            c2 = input("Jugador 2: Ingrese coordenadas de su segunda carta con coma y sin parentesis: ")
            check_coordenates(c2,row, col)
        c2 = c2.split(',')
        board1[int(c2[0])][int(c2[1])] = board2[int(c2[0])][int(c2[1])]
        show_board(board1, row, col)
        n1 = board2[int(c1[0])][int(c1[1])]
        n2 = board2[int(c2[0])][int(c2[1])]
        if n1 == n2:
            print("\nCorrecto!")
            scorep2 += 1
            board1[int(c1[0])][int(c1[1])] = " "
            board1[int(c2[0])][int(c2[1])] = " "
            contador += 2
            if contador == (n*2):
                r = 'si'
                break
            print("\nTienes otro turno")
            continue
        else:
            print("\nIncorrecto")
            board1[int(c1[0])][int(c1[1])] = "*"
            board1[int(c2[0])][int(c2[1])] = "*"
            p1 = True
            p2 = False
            print("\nTurno del jugador 1\n")
            show_board(board1,row,col)
            break
    if r == 'si':
        break

if scorep2 > scorep1:
    print('\nEl jugador 2 gana la partida!\n')
if scorep1 > scorep2:
    print('\nEl jugador 1 gana la partida!\n')
if scorep2 == scorep1:
    print('\nEmpate!')







