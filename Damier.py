from verificator import *
from turtle import *
import time

reponse = intVerif("Donnez un nombre pair : ")
if reponse is not False:
    if reponse < 0:
        print("Vous avez renseigner un nombre négatif, merci de réhitérer.")
    elif reponse % 2 == 0:
        color("black")
        speed(1)
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
    else:
        print("pas pair")
ht()
time.sleep(30)