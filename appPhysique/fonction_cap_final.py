# CAP VRAI
# capvraichoix1
def cap_vrai_Cm_D():
    Cm = float(input("Cap magnétique (Cm) ="))
    D = float(input("Déclinaison (D) ="))
    return Cm, D


def calcul_cap_vrai_Cm_D(Cm, D):
    Cv = Cm + D
    return Cv

    # capvraichoix2


def cap_vrai_Rs_der():
    Rs = float(input("Route surface (Rs) ="))
    print("Attention pour la dérive, elle est négative si le vent vient de tribord. "
          "\n Dans ce cas de figure il faut donc mettre un - devant la valeur de la dérive. ")
    der = float(input("der ="))
    return Rs, der


def calcul_cap_vrai_Rs_der(Rs, der):
    Cv = Rs - der
    return Cv

    # capvraichoix3


def cap_vrai_Cc_W():
    Cc = float(input("Cap compas (Cc) ="))
    W = float(input("Variation (W) ="))


def calcul_cap_vrai_Cc_W(Cc, W):
    Cv = Cc + W
    return Cv

    # capvraichoix4


def cap_vrai_Cc_D_d():
    Cc = float(input("Cap compas (Cc) ="))
    D = float(input("Déclinaison (D) ="))
    d = float(input("déviation (d) ="))
    return Cc, D, d


def calcul_cap_vrai_Cc_D_d(Cc, D, d):
    Cv = Cc + D + d
    return Cv


# CAP MAGNETIQUE
# capmagnétique_choix_1
def cap_magnetique_Cv_D():
    Cv = float(input("Cap vrai (Cv) = "))
    D = float(input("Déclinaison (D) ="))
    return Cv, D


def calcul_cap_magnetique_Cv_D(Cv, D):
    Cm = Cv - D
    return Cm

    # capmagnétique_choix_2


def cap_magnetique_Cc_d():
    Cc = float(input("Cap compas (Cc) = "))
    d = float(input("déviation(d) ="))
    return Cc, d


def calcul_cap_magnetique_Cc_d(Cc, d):
    Cm = Cc + d
    return Cm

    # capmagnétique_choix_3


def cap_magnetique_Cc_W_D():
    Cc = float(input("Cap compas (Cc) = "))
    W = float(input("Variation (W) ="))
    D = float(input("Déclinaison (D) ="))
    return Cc, W, D


def calcul_cap_magnetique_Cc_W_D(Cc, W, D):
    Cm = Cc + W - D
    return Cm

    # capmagnétique_choix_4


def cap_magnetique_Cv_W_d():
    Cv = float(input("Cap vrai (Cv) = "))
    W = float(input("Variation (W) ="))
    d = float(input("déviation(d) ="))
    return Cv, W, d


def calcul_cap_magnetique_Cv_W_d(Cv, W, d):
    Cm = Cv - (W - d)
    return Cm


# CAP COMPAS

# capcompaschoix1
def cap_compas_Cv_W():
    Cv = float(input("Cap vrai (Cv) = "))
    W = float(input("Variation (W) ="))
    return Cv, W


def calcul_cap_compas_Cv_W(Cv, W):
    Cc = Cv - W
    return Cc

    # capcompaschoix2


def cap_compas_Cm_d():
    Cm = float(input("Cap magnétique = "))
    d = float(input("déviation(d) ="))
    return Cm, d


def calcul_cap_compas_Cm_d(Cm, d):
    Cc = Cm - d
    return Cc

    # capcompaschoix3


def cap_compas_Cm_W_D():
    Cm = float(input("Cap magnétique = "))
    W = float(input("Variation (W) ="))
    D = float(input("Déclinaison (D) ="))
    return Cm, W, D


def calcul_cap_compas_Cm_W_D(Cm, W, D):
    Cc = Cm - (W - D)
    return Cc

    # capcompaschoix4


def cap_compas_Cv_d_D():
    Cv = float(input("Cap vrai (Cv) = "))
    d = float(input("déviation(d) ="))
    D = float(input("Déclinaison (D) ="))
    return Cv, d, D


def calcul_cap_compas_Cv_d_D(Cv, d, D):
    Cc = Cv - (D + d)
    return Cc


# Déclinaison (D)

# Déclinaison_choix_1
def Declinaison_d_W():
    d = float(input("déviation(d) = "))
    W = float(input("Variation (W) ="))
    print(" Le calcul est W - d = D \nLa Déclinaison (D) est égale à", W - d, "°")
    return d, W


def calcul_Declinaison_d_W(d, W):
    D = W - d
    return D

    # Déclinaison_choix_2


def Declinaison_Cm_Cv():
    Cm = float(input("Cap magnétique = "))
    Cv = float(input("Cap vrai (Cv) = "))
    return Cm, Cv


def calcul_Declinaison_Cm_Cv(Cm, Cv):
    D = Cv - Cm
    return D

    # Déclinaison_choix_3


def Declinaison_Cc_Cm_W():
    Cc = float(input("Cap compas (Cc) = "))
    Cm = float(input("Cap magnétique = "))
    W = float(input("Variation (W) ="))
    print(" Le calcul est Cc + W - Cm = D \nLa Déclinaison (D) est égale à", Cc + W - Cm, "°")
    return Cc, Cm, W


def calcul_Declinaison_Cc_Cm_W(Cc, Cm, W):
    D = Cc + W - Cm
    return D

    # Déclinaison_choix_4


def Declinaison_Cc_Cv_d():
    Cc = float(input("Cap compas (Cc) = "))
    Cv = float(input("Cap vrai (Cv) = "))
    d = float(input("déviation(d) = "))
    return Cc, Cv, d


def calcul_Declinaison_Cc_Cv_d(Cc, Cv, d):
    D = Cv - d - Cc
    return D

    # Déclinaison_choix_5


def Declinaison_Rs_der_Cm():
    Rs = float(input("Route surface (Rs) ="))
    print("Attention pour la dérive, elle est négative si le vent vient de tribord. "
          "\n Dans ce cas de figure il faut donc mettre un - devant la valeur de la dérive. ")
    der = float(input("der ="))
    Cm = float(input("Cap magnétique = "))
    return Rs, der, Cm


def calcul_Declinaison_Rs_der_Cm(Rs, der, Cm):
    D = Rs - der - Cm
    return D


# déviation (d)

# déviation_choix_1
def deviation_W_D():
    W = float(input("Variation (W) ="))
    D = float(input("Déclinaison (D) ="))
    return W, D


def calcul_deviation_W_D(W, D):
    d = W - D
    return d


#####déviation_choix_2
def deviation_Cm_Cc():
    Cm = float(input("Cap magnétique = "))
    Cc = float(input("Cap compas (Cc) = "))
    return Cm, Cc


def calcul_deviation_Cm_Cc(Cm, Cc):
    d = Cm - Cc
    return d


####déviation_choix_3
def deviation_Cv_D_Cc():
    Cv = float(input("Cap vrai (Cv) = "))
    D = float(input("Déclinaison (D) ="))
    Cc = float(input("Cap compas (Cc) = "))
    return Cv, D, Cc


def calcul_deviation_Cv_D_Cc(Cv, D, Cc):
    d = Cv - D - Cc
    return d


####déviation_choix_4
def deviation_Cm_W_Cv():
    Cm = float(input("Cap magnétique = "))
    W = float(input("Variation (W) ="))
    Cv = float(input("Cap vrai (Cv) = "))
    return Cm, W, Cv


def calcul_deviation_Cm_W_Cv(Cm, W, Cv):
    d = Cm + W - Cv
    return d


####déviation_choix_5
def deviation_Rs_der_Cm_W():
    Rs = float(input("Route surface (Rs) ="))
    print("Attention pour la dérive, elle est négative si le vent vient de tribord. "
          "\n Dans ce cas de figure il faut donc mettre un - devant la valeur de la dérive. ")
    der = float(input("der ="))
    Cm = float(input("Cap magnétique = "))
    W = float(input("Variation (W) ="))

    return Rs, der, Cm, W


def calcul_deviation_Rs_der_Cm_W(Rs, der, Cm, W):
    d = -Rs + der + W + Cm
    return d


# Variation (W)
# Variation_choix_1
def Variation_D_d():
    D = float(input("Déclinaison (D) ="))
    d = float(input("déviation(d) = "))
    return D, d


def calcul_Variation_D_d(D, d):
    W = D + d
    return W

    # Variation_choix_2


def Variation_Cv_Cc():
    Cv = float(input("Cap vrai (Cv) = "))
    Cc = float(input("Cap compas (Cc) = "))
    return Cv, Cc


def calcul_Variation_Cv_Cc(Cv, Cc):
    W = Cv - Cc
    return W

    # Variation_choix_3


def Variation_Rs_der_Cc():
    Rs = float(input("Route surface (Rs) ="))
    print("Attention pour la dérive, elle est négative si le vent vient de tribord. "
          "\n Dans ce cas de figure il faut donc mettre un - devant la valeur de la dérive. ")
    der = float(input("der ="))
    Cc = float(input("Cap compas (Cc) = "))
    return Rs, der, Cc


def calcul_Variation_Rs_der_Cc(Rs, der, Cc):
    W = Rs - der - Cc
    return W

    # Variation_choix_4


def Variation_Cm_Cc_D():
    Cm = float(input("Cap magnétique = "))
    Cc = float(input("Cap compas (Cc) = "))
    D = float(input("Déclinaison (D) ="))
    return Cm, Cc, D


def calcul_Variation_Cm_Cc_D(Cm, Cc, D):
    W = Cm + D - Cc
    return W

    # Variation_choix_5


def Variation_Cv_Cm_d():
    Cv = float(input("Cap vrai (Cv) = "))
    Cm = float(input("Cap magnétique(Cm) = "))
    d = float(input("déviation(d) = "))
    return Cv, Cm, d


def calcul_Variation_Cv_Cm_d(Cv, Cm, d):
    W = Cv + d - Cm
    return W



#Route de surface (Rs)

    #Route_surface_choix_1

def Route_Surface_Cv_der():
    Cv = float(input("Cap vrai (Cv) = "))
    print("Attention pour la dérive, elle est négative si le vent vient de tribord. "
          "\n Dans ce cas de figure il faut donc mettre un - devant la valeur de la dérive. ")
    der = float(input("der ="))
    return Cv,der

def calcul_Route_Surface_Cv_der(Cv,der):
    Rs=Cv + der
    return Rs


    #Route_surface_choix_2

def Route_Surface_Cc_W_der():
    Cc = float(input("Cap compas (Cc) = "))
    W = float(input("Variation (W) ="))
    print("Attention pour la dérive, elle est négative si le vent vient de tribord. "
          "\n Dans ce cas de figure il faut donc mettre un - devant la valeur de la dérive. ")
    der = float(input("der ="))
    return Cc,W,der

def calcul_Route_Surface_Cc_W_der(Cc,W,der):
    Rs=Cc + W + der
    return Rs

    #Route_surface_choix_3

def Route_Surface_Cm_D_der():
    Cm = float(input("Cap magnétique = "))
    D = float(input("Déclinaison (D) ="))
    print("Attention pour la dérive, elle est négative si le vent vient de tribord. "
          "\n Dans ce cas de figure il faut donc mettre un - devant la valeur de la dérive. ")
    der = float(input("der ="))
    return Cm,D,der

def calcul_Route_Surface_Cm_D_der(Cm,D,der):
    Rs=Cm + D + der
    return Rs

#dérive(der)

    # dérive_choix_1
def derive_Cv_Rs():
    Cv = float(input("Cap vrai (Cv) = "))
    Rs = float(input("Route surface (Rs) ="))
    return Cv,Rs
def calcul_derive_Cv_Rs(Rs,Cv):
    der=Rs - Cv
    return der

    # dérive_choix_2

def derive_Cc_W_Rs():
    Cc = float(input("Cap compas (Cc) = "))
    W = float(input("Variation (W) ="))
    Rs = float(input("Route surface (Rs) ="))
    return Cc,W,Rs

def calcul_derive_Cc_W_Rs(Cc,W,Rs):
    der =Rs - Cc - W
    return der

    # dérive_choix_3

def derive_Cm_D_Rs():
    Cm = float(input("Cap magnétique = "))
    D = float(input("Déclinaison (D) ="))
    Rs = float(input("Route surface (Rs) ="))
    return Cm,D,Rs

def calcul_derive_Cm_D_Rs(Rs,Cm,D):
    der =Rs - Cm - D
    return der

#CASCADE

    #cascade_1

def cascade_1():
    Cc = float(input("Le Cap Compas (CC) ="))
    W = float(input("La variation (W)="))
    print("Attention pour la dérive, elle est négative si le vent vient de tribord. "
          "\n Dans ce cas de figure il faut donc mettre un - devant la valeur de la dérive. ")
    der = float(input("La dérive ="))
    return Cc,W,der

def calcul_cascade_1(Cc,W,der):
    Cv=Cc+W
    Rs=Cc+W+der
    return Cv,Rs

    #cascade_2
def cascade_2():
    Cc = float(input("Le Cap Compas (CC) ="))
    d = float(input("déviation(d) = "))
    D = float(input("Déclinaison (D) ="))
    print("Attention pour la dérive, elle est négative si le vent vient de tribord. "
          "\n Dans ce cas de figure il faut donc mettre un - devant la valeur de la dérive. ")
    der = float(input("La dérive ="))
    return Cc,d,D,der

def calcul_cascade_2(Cc,d,D,der):
    Cm=Cc + d
    Cv=Cc + d + D
    W=d + D
    Rs = Cc + d + D + der
    return Cm,Cv,W,Rs