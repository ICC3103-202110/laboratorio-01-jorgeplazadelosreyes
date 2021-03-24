n = int(input('Numero de cartas a jugar: '))
cards = []
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

#def create_board(row,col,cards):


row = row_and_column(n)[0]
col = row_and_column(n)[1]
print(row,col)




