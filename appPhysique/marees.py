print('// ---------------- DEBUT EN TETE --------------------------------------//\n // NOM :                    PRINCIPAL_AEGS_BATEAUX                       //\n// ALGO - REFERENCES :                                                  //\n//                                                                      //\n// AUTEURS :                                                    //\n// VERSION :    1.1         P.SCHOTT              janvier 2020           //\n//                  Création en Scilab d après le programme de mélanges //\n// HISTORIQUE : Aucun                                                   //\n//                                                                      //\n// ENTREES :                                                            //\n//                                                                      //\n// SORTIES :                                                            //\n//                                                                      //\n// MODIFIEES :                                                          //\n//                                                                      //\n// LOCALES :                                                            //\n//                                                                      //\n// FONCTIONS APPELEES :                                                 //\n//                                                                      //\n// ---------------- FIN EN TETE ----------------------------------------//')

def calculmarees():
    print('  haute mer ')
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

    Hm=(((dh*60)+dm)-((fh*60)+fm))/6
    print('\nheure marée: ',Hm,'minutes')

    dz=(dhauteur-fhauteur)/12
    print('\ndouzième de marnage: ',dz)

    qh=int(input('quelle heure?'))
    qm=int(input('quelle minute?'))
    t=qh*60+qm
    if t<fh*60+fm+Hm :
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