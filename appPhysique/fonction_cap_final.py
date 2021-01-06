print('// ---------------- DEBUT EN TETE --------------------------------------//\n // NOM :                    PRINCIPAL_AEGS_BATEAUX                       //\n// ALGO - REFERENCES :                                                  //\n//                                                                      //\n// AUTEURS :                                                    //\n// VERSION :    1.1         P.SCHOTT              janvier 2020           //\n//                  Création en Scilab d après le programme de mélanges //\n// HISTORIQUE : Aucun                                                   //\n//                                                                      //\n// ENTREES :                                                            //\n//                                                                      //\n// SORTIES :                                                            //\n//                                                                      //\n// MODIFIEES :                                                          //\n//                                                                      //\n// LOCALES :                                                            //\n//                                                                      //\n// FONCTIONS APPELEES :                                                 //\n//                                                                      //\n// ---------------- FIN EN TETE ----------------------------------------//')
#CAP VRAI
    #capvraichoix1
def cap_vrai_Cm_D():
    Cm = float(input("Cap magnétique (Cm) ="))
    D = float(input("Déclinaison (D) ="))
    return Cm, D

def calcul_cap_vrai_Cm_D(Cm,D):
    Cv = Cm + D
    

    #capvraichoix2
def cap_vrai_Rs_der():
    Rs = float(input("Route surface (Rs) ="))
    print("Attention pour la dérive, elle est négative si le vent vient de tribord. "
          "\n Dans ce cas de figure il faut donc mettre un - devant la valeur de la dérive. ")
    der = float(input("der ="))
    return Rs, der
def calcul_cap_vrai_Rs_der(Rs,der):
    Cv = Rs - der
    print(" Le calcul est Rs - der = Cv \nLe Cap vrai (Cv) est égal à", Cv, "°")

    #capvraichoix3
def cap_vrai_Cc_W():
    Cc = float(input("Cap compas (Cc) ="))
    W = float(input("Variation (W) ="))
def calcul_cap_vrai_Cc_W(Cc,W):
    Cv = Cc + W
    print(" Le calcul est Cc + W = Cv \nLe Cap vrai (Cv) est égal à", Cv, "°")

    #capvraichoix4
def cap_vrai_Cc_D_d():
    Cc = float(input("Cap compas (Cc) ="))
    D = float(input("Déclinaison (D) ="))
    d = float(input("déviation (d) ="))
    return Cc, D, d

def calcul_cap_vrai_Cc_D_d(Cc,D,d):
    Cv = Cc + D + d
    print(" Le calcul est Cc + D + d = Cv \nLe Cap vrai (Cv) est égal à", Cv, "°")

#CAP MAGNETIQUE
    #capmagnétique_choix_1
def cap_magnétique_Cv_D():
    Cv = float(input("Cap vrai (Cv) = "))
    D = float(input("Déclinaison (D) ="))
    return Cv , D

def calcul_cap_magnétique_Cv_D(Cv,D):
    Cm = Cv - D
    print(" Le calcul est Cv - D = Cm \nLe Cap magnétique (Cm) est égal à", Cm, "°")

    #capmagnétique_choix_2
def cap_magnétique_Cc_d():
    Cc = float(input("Cap compas (Cc) = "))
    d = float(input("déviation(d) ="))
    return Cc,d

def calcul_cap_magnétique_Cc_d(Cc,d):
    Cm=Cc+d
    print(" Le calcul est Cc + d = Cm \nLe Cap magnétique (Cm) est égal à", Cm, "°")

    #capmagnétique_choix_3
def cap_magnétique_Cc_W_D():
    Cc = float(input("Cap compas (Cc) = "))
    W = float(input("Variation (W) ="))
    D = float(input("Déclinaison (D) ="))
    return Cc,W,D

def calcul_cap_magnétique_Cc_W_D(Cc,W,D):
    Cm=Cc + W - D
    print(" Le calcul est Cc + W - D = Cm \nLe Cap magnétique (Cm) est égal à", Cm, "°")

    #capmagnétique_choix_4
def cap_magnétique_Cv_W_d():
    Cv = float(input("Cap vrai (Cv) = "))
    W = float(input("Variation (W) ="))
    d = float(input("déviation(d) ="))
    return Cv,W,d

def calcul_cap_magnétique_Cv_W_d(Cv,W,d):
    Cm=Cv - (W - d)
    print(" Le calcul est Cv - (W - d) = Cm \nLe Cap magnétique (Cm) est égal à", Cm, "°")

#CAP COMPAS

    #capcompaschoix1
def cap_compas_Cv_W():
    Cv = float(input("Cap vrai (Cv) = "))
    W = float(input("Variation (W) ="))
    return Cv, W

def calcul_cap_compas_Cv_W(Cv,W):
    Cc=Cv - W
    print(" Le calcul est Cv - W = Cc \nLe Cap compas (Cc) est égal à",Cc, "°")
    return Cc

    #capcompaschoix2
def cap_compas_Cm_d():
    Cm = float(input("Cap magnétique = "))
    d = float(input("déviation(d) ="))
    return Cm,d

def calcul_cap_compas_Cm_d(Cm,d):
    Cc = Cm - d
    print(" Le calcul est Cm - d = Cc \nLe Cap compas (Cc) est égal à", Cc, "°")

    #capcompaschoix3
def cap_compas_Cm_W_D():
    Cm = float(input("Cap magnétique = "))
    W = float(input("Variation (W) ="))
    D = float(input("Déclinaison (D) ="))
    return Cm, W, D

def calcul_cap_compas_Cm_W_D(Cm, W, D):
    Cc =Cm - (W - D)
    print(" Le calcul est Cm - (W - D) = Cc \nLe Cap compas (Cc) est égal à", Cc, "°")

    #capcompaschoix4
def cap_compas_Cv_d_D():
    Cv = float(input("Cap vrai (Cv) = "))
    d = float(input("déviation(d) ="))
    D = float(input("Déclinaison (D) ="))
    return Cv,d,D

def calcul_cap_compas_Cv_d_D(Cv,d,D):
    Cc=Cv - (D + d)
    print(" Le calcul est Cv - (d + D) = Cc \nLe Cap compas (Cc) est égal à", Cc, "°")


#Déclinaison (D)

    #Déclinaison_choix_1
def Déclinaison_d_W():
    d = float(input("déviation(d) = "))
    W = float(input("Variation (W) ="))
    print(" Le calcul est W - d = D \nLa Déclinaison (D) est égale à", W - d, "°")
    return d,W

def calcul_Déclinaison_d_W(d,W):
    D= W - d
    print(" Le calcul est W - d = D \nLa Déclinaison (D) est égale à", D, "°")

    #Déclinaison_choix_2
def Déclinaison_Cm_Cv():
    Cm = float(input("Cap magnétique = "))
    Cv = float(input("Cap vrai (Cv) = "))
    return Cm,Cv

def calcul_Déclinaison_Cm_Cv(Cm,Cv):
    D=Cv - Cm
    print(" Le calcul est Cv - Cm = D \nLa Déclinaison (D) est égale à", D, "°")

    #Déclinaison_choix_3
def Déclinaison_Cc_Cm_W():
    Cc = float(input("Cap compas (Cc) = "))
    Cm = float(input("Cap magnétique = "))
    W = float(input("Variation (W) ="))
    print(" Le calcul est Cc + W - Cm = D \nLa Déclinaison (D) est égale à", Cc + W - Cm, "°")
    return Cc,Cm,W
def calcul_Déclinaison_Cc_Cm_W(Cc,Cm,W):
    D = Cc + W - Cm
    print(" Le calcul est Cc + W - Cm = D \nLa Déclinaison (D) est égale à", D, "°")

    #Déclinaison_choix_4
def Déclinaison_Cc_Cv_d():
    Cc = float(input("Cap compas (Cc) = "))
    Cv = float(input("Cap vrai (Cv) = "))
    d = float(input("déviation(d) = "))
    return Cc,Cv,d

def calcul_Déclinaison_Cc_Cv_d(Cc,Cv,d):
    D=Cv - d - Cc
    print(" Le calcul est Cv - d - Cc = D \nLa Déclinaison (D) est égale à", D, "°")

    #Déclinaison_choix_5
def Déclinaison_Rs_der_Cm():
    Rs = float(input("Route surface (Rs) ="))
    print("Attention pour la dérive, elle est négative si le vent vient de tribord. "
          "\n Dans ce cas de figure il faut donc mettre un - devant la valeur de la dérive. ")
    der = float(input("der ="))
    Cm = float(input("Cap magnétique = "))
    return Rs,der,Cm

def calcul_Déclinaison_Rs_der_Cm(Rs,der,Cm):
    D=Rs - der - Cm
    print(" Le calcul est Rs - der - Cm = D \n La Déclinaison (D) est égale à", D, "°")

#déviation (d)

    #déviation_choix_1
def déviation_W_D():
    W = float(input("Variation (W) ="))
    D = float(input("Déclinaison (D) ="))
    return W,D

def calcul_déviation_W_D(W,D):
    d = W - D
    print(" Le calcul est W - D = d \nLa déviation (d) est égale à", d, "°")

#####déviation_choix_2
def déviation_Cm_Cc():
    Cm = float(input("Cap magnétique = "))
    Cc = float(input("Cap compas (Cc) = "))
    return Cm,Cc

def calcul_déviation_Cm_Cc(Cm,Cc):
    d = Cm -Cc
    print(" Le calcul est Cm - Cc = d \nLa déviation (d) est égale à", d, "°")

####déviation_choix_3
def déviation_Cv_D_Cc():
    Cv = float(input("Cap vrai (Cv) = "))
    D = float(input("Déclinaison (D) ="))
    Cc = float(input("Cap compas (Cc) = "))
    return Cv,D,Cc

def calcul_déviation_Cv_D_Cc(Cv,D,Cc):
    d = Cv - D - Cc
    print(" Le calcul est Cv - D - Cc = d \nLa déviation (d) est égale à", d, "°")

####déviation_choix_4
def déviation_Cm_W_Cv():
    Cm = float(input("Cap magnétique = "))
    W = float(input("Variation (W) ="))
    Cv = float(input("Cap vrai (Cv) = "))
    return Cm,W,Cv

def calcul_déviation_Cm_W_Cv(Cm,W,Cv):
    d = Cm + W - Cv
    print(" Le calcul est Cm + W - Cv = d \nLa déviation (d) est égale à", Cm + W - Cv, "°")

####déviation_choix_5
def déviation_Rs_der_Cm_W():
    Rs = float(input("Route surface (Rs) ="))
    print("Attention pour la dérive, elle est négative si le vent vient de tribord. "
          "\n Dans ce cas de figure il faut donc mettre un - devant la valeur de la dérive. ")
    der = float(input("der ="))
    Cm = float(input("Cap magnétique = "))
    W = float(input("Variation (W) ="))

    return Rs,der,Cm,W

def calcul_déviation_Rs_der_Cm_W(Rs,der,Cm,W):
    d = -Rs + der + W + Cm
    print(" Le calcul est -Rs + der + W + Cm = d \nLa déviation (d) est égale à", d, "°")


#Variation (W)
    # Variation_choix_1
def Variation_D_d():
    D = float(input("Déclinaison (D) ="))
    d = float(input("déviation(d) = "))
    return D,d

def calcul_Variation_D_d(D,d):
    W = D+d
    print(" Le calcul est D + d = W \nLa variation (W) est égale à", W, "°")

    # Variation_choix_2
def Variation_Cv_Cc():
    Cv = float(input("Cap vrai (Cv) = "))
    Cc = float(input("Cap compas (Cc) = "))
    return Cv,Cc

def calcul_Variation_Cv_Cc(Cv,Cc):
    W = Cv - Cc
    print(" Le calcul est Cv - Cc = W \nLa variation (W) est égale à", W, "°")

    # Variation_choix_3
def Variation_Rs_der_Cc():
    Rs = float(input("Route surface (Rs) ="))
    print("Attention pour la dérive, elle est négative si le vent vient de tribord. "
            "\n Dans ce cas de figure il faut donc mettre un - devant la valeur de la dérive. ")
    der = float(input("der ="))
    Cc = float(input("Cap compas (Cc) = "))
    return Rs,der,Cc

def calcul_Variation_Rs_der_Cc(Rs,der,Cc):
    W = Rs - der - Cc
    print(" Le calcul est Rs - der - Cc = W \nLa variation (W) est égale à", W, "°")

    # Variation_choix_4
def Variation_Cm_Cc_D():
    Cm = float(input("Cap magnétique = "))
    Cc = float(input("Cap compas (Cc) = "))
    D = float(input("Déclinaison (D) ="))
    return Cm,Cc,D

def calcul_Variation_Cm_Cc_D(Cm,Cc,D):
    W = Cm + D - Cc
    print(" Le calcul est Cm + D - Cc = W \nLa variation (W) est égale à", W, "°")

    # Variation_choix_5
def Variation_Cv_Cc_d():
    Cv = float(input("Cap vrai (Cv) = "))
    Cm= float(input("Cap magnétique(Cm) = "))
    d = float(input("déviation(d) = "))
    return Cv,Cm,d

def calcul_Variation(Cv,Cm,d):
    W = Cv + d - Cm
    print(" Le calcul est Cv + d - Cm = W \nLa déviation (d) est égale à", W, "°")


