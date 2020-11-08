from math import*

def deuxpoints():
    Xa=int(input("Ta position Xa"))
    Ya=int(input("Ta position Ya"))

    Xm=int(input("Ta position Xm"))
    Ym=int(input("Ta position Ym"))

    m=(Ym-Ya)/(Xm-Xa)
    b=Ym-m*Xm
    print(m)
    print(b)
    print("y=", m,"x+",b)

def unpointunangle():
    Xb = int(input("Ta position Xb"))
    Yb = int(input("Ta position Yb"))
    B = int(input("angle Beta entre l'axe du Nord et la droite MA"))

    m = tan(B)
    b=Yb-m*Xb
    print("y=", m,"x+",b)


unpointunangle()





