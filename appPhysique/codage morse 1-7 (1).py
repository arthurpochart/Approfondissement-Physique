from random import *
morse = ['.-', '-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..',]

def mode1():
    lettre = input("Choisir une lettre : ")
    print(ord(lettre)-97)
    print(morse[ord(lettre)-97])
    mot = input("Choisir un mot : ")
    nouveaumot = ""
    for i in mot :
        nouveaumot = nouveaumot + morse[ord(i)-97] + " "
    print(nouveaumot)

def mode2():
    signe=input("Choisir un signe : ")
    print(chr(morse.index (signe)+ 97))
    mot2= input ("Choisir un mot en morse :")
    nouveaumot2= ""
    caracteremorse =""
    for i in mot2 :
        if i != " ":
            caracteremorse= caracteremorse + i
 
        else :
            nouveaumot2 = nouveaumot2 + chr(morse.index(caracteremorse)+97)  
            caracteremorse =""
    
    nouveaumot2 = nouveaumot2 + chr(morse.index(caracteremorse)+97)     
    print(nouveaumot2)

en_jeu = True


while en_jeu == True:
    print("depuis morse(2) ou french(1)")
    reponse = []
    mode = input()
    try:
        if mode == "":
            raise ValueError
        mode = int(mode)
    except ValueError:
        print("un chiffre")
    if mode == 1:
        mode1()
    elif mode == 2:
        mode2()   