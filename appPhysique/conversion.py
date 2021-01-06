from math import*

x = longitude
y = math.sqrt((ynord)^2+(ysud)^2)
ynord = 5/4*math.log(math.tan(math.pi/4 + (2*latitude)/5))
ysud = 5/4*math.log(math.tan(math.pi/4 + (2*latitude/5))

from PIL import image
img = Image.open('SCHOM9999.png')
img.size

def conversionenx():
    largeur =  float(input("la largeur de l'image"))
    h = largeur/2*math.pi
    xmap = h*x
    print(largeur,h,xmap)

def conversioneny():
    longueur =  float(input("la longueur de l'image"))
    H = longueur/y
    ymap = H*y
    print(longueur,H,ymap)
    

longitude = float(input("Ta position x de l amer"))
latitude = float(input("Ta position y de l amer"))
