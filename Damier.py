from turtle import *
def damier():
    nbcases = int(input("Entrez un nombre paire de colonnes"))
    if nbcases%2 != 0:
        print('Entrez un nombre de lignes paire.')
        return
    Lc = 40
    up()
    color('black')
    right(135)
    forward((nbcases*Lc*2**(1/2))/2)
    left(135)
    down()
    for i in range(nbcases):
        for j in range(nbcases//2):
            for k in range(5):
                forward(Lc)
                left(90)
            right(90)
            begin_fill()
            for k in range(5):
                forward(Lc)
                left(90)
            end_fill()
            right(90)
        if i%2 == 0:
            left(90)
            forward(2*Lc)
            left(90)
        else:
            right(180)
damier()
