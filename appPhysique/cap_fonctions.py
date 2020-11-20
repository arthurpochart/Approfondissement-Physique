def demandes_entree_utilisateur():
    global Cc, W, Rs
    Cc = float(input("Cap compas (Cc) ="))
    W = float(input("Variation (W) ="))
    Rs = float(input("Route surface (Rs) ="))
    return Cc, W, Rs

def calcul_der_test():
    der = Rs - Cc - W
    print("der=", der)
    return der

demandes_entree_utilisateur()
calcul_der_test()

