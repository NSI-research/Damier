from verificator import intVerif
from turtle import *

reponse = intVerif("\nDonnez un nombre pair : ", peer=True, pos=True, nul=False)

color("black")
speed(1000)
casepaire = 0
for i in range(reponse):
    for j in range(reponse):
        if casepaire % 2 == 0:
            begin_fill()
        for k in range(4):
            forward(40)
            right(90)
        forward(40)
        casepaire += 1
        end_fill()
    right(180)
    forward(40 * reponse)
    left(90)
    forward(40)
    left(90)
    casepaire += 1
ht()
