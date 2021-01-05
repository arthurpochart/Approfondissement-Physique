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

def unameruncapunedistance(longitude,latitude,cap,distance):
    R = 6378137.0
    Xamer = R * cos(longitude) * sin(latitude)
    Yamer = R * sin(longitude) * sin(latitude)
    m = tan(pi/2 - cap*pi/180)
    b=Yamer-m*Xamer
    print("y=", m, "x+", b)
    x=sin(cap*pi/180)*distance
    y=m*x+b
    print(x, y)


longitude = float(input("Ta position x de l amer"))
latitude = float(input("Ta position y de l amer"))
cap = float(input("angle Beta entre l'axe du Nord et la droite MA (en degré)"))
distance=float(input('quelle distance parcours le bateau ?'))
unameruncapunedistance(longitude,latitude,cap,distance)


