def demande():
    Cc = float(input("Cap compas (Cc) ="))
    W = float(input("Variation (W) ="))
    Rs = float(input("Route surface (Rs) ="))
    return Cc, W, Rs
def calcul(Cc,W,Rs):
    der = Rs - Cc - W
    print("der=", der)

Cc, W,  Rs = demande()
print(Cc)
calcul(Cc,W,Rs)
