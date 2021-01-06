def calculmarees():                                                                    #fonction qui me donne la hauteur de la mer à l'heure que je veux
    print('  haute mer ')                                                              #on demande à l'utilisateur les différentes caractéristiques de la marée
    dh=int(input("heure:"))
    if dh>23:                                                                          # on sécurise le programme au cas ou l'utilisatuer rentre un chiffre dingo pour une heure afin de ne pas avoir à le relancer
        print('Attention l heure est comprise entre 0 et 23!')
        dh = int(input("heure:"))
    dm=int(input("minute:"))
    if dm > 59:                                                                         #idem, on sécurise
        print('Attention les minutes sont comprises entre 0 et 59!')
        dm=int(input("minute:"))
    dhauteur=float(input("hauteur d'eau:"))

    print('\n  basse mer')
    fh=int(input("heure:"))
    fm=int(input("minute:"))
    if fh > 23:                                                                         #idem, on sécurise
        print('Attention l heure est comprise entre 0 et 23!')
        fh = int(input("heure:"))
    if fm > 59:                                                                         #idem, on sécurise
        print('Attention les minutes sont comprises entre 0 et 59!')
        fm = int(input("minute:"))
    fhauteur=float(input("hauteur d'eau:"))

    Hm=(((dh*60)+dm)-((fh*60)+fm))/6                                                    #calcul Heure marée
    print('\nheure marée: ',Hm,'minutes')

    dz=(dhauteur-fhauteur)/12                                                           #calcul douzième de marnage
    print('\ndouzième de marnage: ',dz)

    qh=int(input('quelle heure?'))                                                      # on demande à l'utilisateur à quelle heure veut t-il connaitre la hauteur de la mer
    qm=int(input('quelle minute?'))
    t=qh*60+qm                                                                          #on mets le temps en minutes afin de pouvoir l'exploiter correctement
    if t<fh*60+fm+Hm :                                                                  #série de "if" afin de donner à l'utilisateur la bonne hauteur en fonction de l'horaire
        evolution=(t-(fh*60+fm))*(dz/Hm)
        total=fhauteur+evolution
        print("Nous aurons donc a",qh,'h',qm,'min',total,'metres d eau')

    if fh*60+fm+Hm<t<fh*60+fm+2*Hm :
        evolution = (t - (fh * 60 + fm + Hm)) * (2*dz / Hm)
        total = fhauteur + dz + evolution
        print("Nous aurons donc a", qh, 'h', qm, 'min', total, 'metres d eau')

    if fh*60 + fm + 2*Hm < t < fh*60 + fm + 3*Hm :
        evolution = (t - (fh * 60 + fm+2*Hm)) * (3 * dz / Hm)
        total = fhauteur + 3*dz + evolution
        print("Nous aurons donc a", qh, 'h', qm, 'min', total, 'metres d eau')

    if fh*60 + fm + 3*Hm < t < fh*60 + fm + 4*Hm :
        evolution = (t - (fh * 60 + fm+3*Hm)) * (3 * dz / Hm)
        total = fhauteur + 6*dz + evolution
        print("Nous aurons donc a", qh, 'h', qm, 'min', total, 'metres d eau')

    if fh*60 + fm + 4*Hm < t < fh*60 + fm + 5*Hm :
        evolution = (t - (fh * 60 + fm+4*Hm)) * (2 * dz / Hm)
        total = fhauteur + 9*dz + evolution
        print("Nous aurons donc a", qh, 'h', qm, 'min', total, 'metres d eau')
    if fh*60 + fm + 6*Hm < t < fh*60 + fm + 7*Hm :
        evolution = (t - (fh * 60 + fm+5*Hm)) * (dz / Hm)
        total = fhauteur + 11*dz + evolution
        print("Nous aurons donc a", qh, 'h', qm, 'min', total, 'metres d eau')

    if t==fh*60+fm:
        total = fhauteur
        print("Nous aurons donc a", qh, 'h', qm, 'min', total, 'metres d eau')
    if t==fh*60+fm+Hm:
        total=fhauteur+dz
        print("Nous aurons donc a",qh,'h',qm,'min',total,'metres d eau')
    if t==fh*60+fm+2*Hm:
        total=fhauteur+3*dz
        print("Nous aurons donc a",qh,'h',qm,'min',total,'metres d eau')
    if t==fh*60+fm+3*Hm:
        total=fhauteur+6*dz
        print("Nous aurons donc a",qh,'h',qm,'min',total,'metres d eau')
    if t==fh*60+fm+4*Hm:
        total=fhauteur+9*dz
        print("Nous aurons donc a",qh,'h',qm,'min',total,'metres d eau')
    if t==fh*60+fm+5*Hm:
        total=fhauteur+11*dz
        print("Nous aurons donc a",qh,'h',qm,'min',total,'metres d eau')
    if t==fh*60+fm+6*Hm:
        total=fhauteur+12*dz
        print("Nous aurons donc a",qh,'h',qm,'min',total,'metres d eau')

def hauteur():                                                      # fonction qui permet de donner l'heure à laquelle la hauteur rentrée par l'utilisateur est atteinte
    global heure
    global fh
    global fm
    print('  haute mer ')                                           #idem que la fonction calculmarees: on demande à l'utilisateur de rentrer les différetes variables que l'on connait de la marée
    dh=int(input("heure:"))
    if dh>23:
        print('Attention l heure est comprise entre 0 et 23!')
        dh = int(input("heure:"))
    dm=int(input("minute:"))
    if dm > 59:
        print('Attention les minutes sont comprises entre 0 et 59!')
        dm=int(input("minute:"))
    dhauteur=float(input("hauteur d'eau:"))

    print('\n  basse mer')
    fh=int(input("heure:"))
    fm=int(input("minute:"))
    if fh > 23:
        print('Attention l heure est comprise entre 0 et 23!')
        fh = int(input("heure:"))
    if fm > 59:
        print('Attention les minutes sont comprises entre 0 et 59!')
        fm = int(input("minute:"))
    fhauteur=float(input("hauteur d'eau:"))

    Hm=(((dh*60)+dm)-((fh*60)+fm))/6                                                            #calcul Heure marée
    print('\nheure marée: ',Hm,'minutes')

    dz=(dhauteur-fhauteur)/12                                                                   #calcul douzième de marnage
    print('\ndouzième de marnage: ',dz)

    h=float(input('quelle hauteur?'))                                                          # on demande à l'utilisateur quelle hauteur est concernée

    if h<fhauteur+dz:                                                                          #série de "if" qui permette de donner l'heure à laquelle la hauteur est atteinte
        evolution=(h-fhauteur)*(Hm/dz)
        total=fh*60+fm+evolution
        heure=total*0.016667
        print("Les",h,'seront atteinds à',heure)

    if fhauteur+dz<h<fhauteur+3*dz:
        evolution=(h-fhauteur-2*dz)*(Hm/2*dz)
        total=fh*60+fm+evolution+Hm
        heure=total*0.016667
        print("Les",h,'seront atteinds à',heure)

    if fhauteur+3*dz<h<fhauteur+6*dz:
        evolution=(h-fhauteur-3*dz)*(Hm/3*dz)
        total=fh*60+fm+evolution +2*Hm
        heure=total*0.016667
        print("Les",h,'seront atteinds à',heure)

    if fhauteur+6*dz<h<fhauteur+9*dz:
        evolution=(h-fhauteur-6*dz)*(Hm/3*dz)
        total=fh*60+fm+evolution + 3*Hm
        heure=total*0.016667
        print("Les",h,'seront atteinds à',heure)

    if fhauteur+9*dz<h<fhauteur+11*dz:
        evolution=(h-fhauteur-9*dz)*(Hm/2*dz)
        total=fh*60+fm+evolution +4*Hm
        heure=total*0.016667
        print("Les",h,'seront atteinds à',heure)

    if fhauteur+11*dz<h<fhauteur+12*dz:
        evolution=(h-fhauteur-11*dz)*(Hm/dz)
        total=fh*60+fm+evolution+5*Hm
        heure=total*0.016667
        print("Les",h,'seront atteinds à',heure)

    if h==fhauteur:
        total=fh*60+fm
        heure=total*0.016667
        print("Les", h, 'seront atteinds à', heure)

    if h==fhauteur + dz:
        total=fh*60+fm +Hm
        heure=total*0.016667
        print("Les", h, 'seront atteinds à', heure)

    if h==fhauteur +2*dz:
        total=fh*60+fm +2*Hm
        heure=total*0.016667
        print("Les", h, 'seront atteinds à', heure)

    if h==fhauteur +3*dz:
        total=fh*60+fm +3*Hm
        heure=total*0.016667
        print("Les", h, 'seront atteinds à', heure)

    if h==fhauteur+4*dz:
        total=fh*60+fm +4*Hm
        heure=total*0.016667
        print("Les", h, 'seront atteinds à', heure)

    if h==fhauteur+5*dz:
        total=fh*60+fm +5*Hm
        heure=total*0.016667
        print("Les", h, 'seront atteinds à', heure)

    if h==fhauteur+6*dz:
        total=fh*60+fm + 6*Hm
        heure=total*0.016667
        print("Les", h, 'seront atteinds à', heure)

def sondecarte(): #fonction permettant de donner l'heure ou la hauteur d'eau voulue est atteinte ainsi que le temps par rapport au début de la marée ou la hauteur d eau voulue est atteinte
    global heure
    global fh
    global fm
    tiraneau=float(input('tiran deau:'))
    PiedDePilote=float(input('Pied de pilote:'))
    sonde=float(input('Sonde:'))
    dhauteur=tiraneau+PiedDePilote+sonde
    print(dhauteur)
    hauteur()
    tempsparrapportaudebut=heure*60-fh*60-fm
    print('le temps par rapport au début de la marée ou la hauteur d eau voulue est atteinte est:',tempsparrapportaudebut,' minutes')
