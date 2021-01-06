from maree import*

print(
    'Bonjour et bienvenue à bord! '
    '\nSouhaitez vous calculez:'
    '\n\n1. La hauteur de la marée à une certaine heure'
    '\n\n2. L heure à laquelle la hauteur voulu est atteinte'
    '\n\n3. L heure à  laquelle vous souhaitez pouvoir passer une sonde')

rep=float(input('Quel est votre choix? \n Choix numéro:'))

while rep<1 or rep>3:
    print('Veuillez choisir un chiffre entre 1 et 3')
    rep = float(input('Quel est votre choix? \n Choix numéro:'))

if rep>=1 and rep<=3:
    if rep==1:
        calculmarees()
    if rep==2:
        hauteur()
    if rep==3:
        sondecarte()



