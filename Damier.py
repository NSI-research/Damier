from verificator import intVerif
from turtle import *
import time

Valid = False
while Valid is False:
    reponse = intVerif("\nDonnez un nombre pair : ")
    if reponse < 0:
        print("\nVous avez renseigner un nombre négatif, merci de réhitérer.")
    elif reponse % 2 != 0:
        print("\nCe nombre n'est pas pair.")
    elif reponse is False:
        print("\nLe nombre que vous avez renseigné est invalide. (décimal, texte, etc...)")
    else:
        Valid = True

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
