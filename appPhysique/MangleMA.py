from math import*

def deuxpoints():
    Xa=float(input("Ta position Xa"))
    Ya=float(input("Ta position Ya"))

    Xm=float(input("Ta position Xm"))
    Ym=float(input("Ta position Ym"))

    m=(Ym-Ya)/(Xm-Xa)
    b=Ym-m*Xm
    print(m)
    print(b)
    print("y=", m,"x+",b)

def unpointunangle():
    Xb = float(input("Ta position Xb"))
    Yb = float(input("Ta position Yb"))
    B = float(input("angle Beta entre l'axe du Nord et la droite MA (en degré)"))

    m = tan(pi/2 - B*pi/180)
    b=Yb-m*Xb
    print("y=", m,"x+",b)


unpointunangle()





