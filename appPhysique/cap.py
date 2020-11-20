print(
    "\n\nBienvenue sur notre application, \nElle va vous permettre de calculer différentes grandeurs nécessaires à la navigation. "
    "\n\nSouhaitez-vous calculer: "
    "\n\n 1. Le Cap vrai (Cv) \n  (angle entre l'axe du bateau et le Nord vrai (Nv)) "
    "\n\n 2. Le Cap magnétique (Cm) \n  (angle entre l'axe du bateau et le Nord magnétique (Nm))"
    "\n\n 3. Le Cap compas (Cc) \n  (angle entre l'axe du bateau et le Nord compas (Nc))"
    "\n\n 4. La Déclinaison (D) \n  (angle entre Nv et Nm)"
    "\n\n 5. La Déviation (d) \n  (angle entre Nm et Nc)"
    "\n\n 6. La Variation (W) \n  (angle entre Nv et Nc)"
    "\n\n 7. La Route surface (Rs) \n  (Route à tracer sur la carte en tenant compte de la dérive du vent)"
    "\n\n 8. La Dérive (der) \n  (force du vent qui provoque une déviation du bateau)"
    "\n\n 9. La Cascade \n  menu qui calcule toute la cascade du Cap Compas à la Route surface en affichant les différents caps au fur et à mesure"
    "\n\n\n ATTENTION les corrections D, d et W se mesurent négativement vers l'ouest et postivement vers l'est (sens des aiguilles d'une montre)")

rep = int(input("\nQuelle grandeur recherchez-vous? \nGrandeur recherhée :"))

while rep < 1 or rep > 9:
    print("Veuillez choisir un nombre entre 1 et 8")
    rep = int(input("\nQuelle grandeur recherchez-vous? \nGrandeur recherhée :"))

if rep >= 1 and rep <= 9:
    if rep == 1:
        print("\n\n/Vous cherchez le Cap Vrai(Cv)\ \n\nIl y a 3 façons de trouver le Cap Vrai")
        print("\nVous connaissez soit :"
              "\n 1.Cap magnétique (Cm) et Déclinaison (D)"
              "\n 2.Route surface (Rs) et der"
              "\n 3.Cap compas (Cc) et Variation (W)"
              "\n 4.Cap compas (Cc),la Déclinaison (D) et la déviation (d)")
        choix1 = int(input("\nVous disposez de :"))
        while choix1 < 1 or choix1 > 4:
            print("Veuillez choisir un nombre entre 1 et 4 qui correspondent aux options proposées")
            choix1 = int(input("\nVous disposez de :"))
        if choix1 == 1:
            Cm = float(input("Cap magnétique (Cm) ="))
            D = float(input("Déclinaison (D) ="))
            print(" Le calcul est Cm + D = Cv \nLe Cap vrai (Cv) est donc égal à", Cm + D, "°")
        if choix1 == 2:
            Rs = float(input("Route surface (Rs) ="))
            print("Attention pour la dérive, elle est négative si le vent vient de tribord. "
                  "\n Dans ce cas de figure il faut donc mettre un - devant la valeur de la dérive. ")
            der = float(input("der ="))
            print(" Le calcul est Rs - der = Cv \nLe Cap vrai (Cv) est égal à", Rs - der, "°")
        if choix1 == 3:
            Cc = float(input("Cap compas (Cc) ="))
            W = float(input("Variation (W) ="))
            print(" Le calcul est Cc + W = Cv \nLe Cap vrai (Cv) est égal à", Cc - W, "°")
        if choix1 == 4:
            Cc = float(input("Cap compas (Cc) ="))
            D = float(input("Déclinaison (D) ="))
            d = float(input("déviation (d) ="))
            print(" Le calcul est Cc + D + d = Cv \nLe Cap vrai (Cv) est égal à", Cc + D + d, "°")

    if rep == 2:
        print("\n\n/Vous cherchez le Cap Magnétique(Cm)\ ")
        print("\nVous connaissez soit :"
              "\n 1.Cap vrai (Cv) et Déclinaison (D)"
              "\n 2.Cap compas (Cc) et déviation(d)"
              "\n 3.Cap compas (Cc), la Variation (W) et la Déclinaison (D)"
              "\n 4.Cap vrai (Cv), la Variation(W) et la déviation (d) ")
        choix2 = int(input("\nVous disposez de :"))
        while choix2 < 1 or choix2 > 4:
            print("Veuillez choisir un nombre entre 1 et 4 qui correspondent aux options proposées")
            choix2 = int(input("\nVous disposez de :"))
        if choix2 == 1:
            Cv = float(input("Cap vrai (Cv) = "))
            D = float(input("Déclinaison (D) ="))
            print(" Le calcul est Cv - D = Cm \nLe Cap magnétique (Cm) est égal à", Cv - D, "°")
        if choix2 == 2:
            Cc = float(input("Cap compas (Cc) = "))
            d = float(input("déviation(d) ="))
            print(" Le calcul est Cc + d = Cm \nLe Cap magnétique (Cm) est égal à", Cc + d, "°")
        if choix2 == 3:
            Cc = float(input("Cap compas (Cc) = "))
            W = float(input("Variation (W) ="))
            D = float(input("Déclinaison (D) ="))
            print(" Le calcul est Cc + W - D = Cm \nLe Cap magnétique (Cm) est égal à", Cc + W - D, "°")
        if choix2 == 4:
            Cv = float(input("Cap vrai (Cv) = "))
            W = float(input("Variation (W) ="))
            d = float(input("déviation(d) ="))
            print(" Le calcul est Cv - (W - d) = Cm \nLe Cap magnétique (Cm) est égal à", Cv - (W - d), "°")

    if rep == 3:
        print("\n\n/Vous cherchez le Cap Compas(Cc)\ ")
        print("\nVous connaissez soit :"
              "\n 1.Cap vrai (Cv) et Variation(W)"
              "\n 2.Cap magnétique (Cm) et déviation(d)"
              "\n 3.Cap magnétique (Cc), la Variation (W) et la Déclinaison (D)"
              "\n 4.Cap vrai (Cv), la déviation (d) et la Déclinaison (D)")
        choix3= int(input("\nVous disposez de :"))
        while choix3 < 1 or choix3 > 4:
            print("Veuillez choisir un nombre entre 1 et 4 qui correspondent aux options proposées")
            choix3 = int(input("\nVous disposez de :"))
        if choix3 == 1:
            Cv = float(input("Cap vrai (Cv) = "))
            W = float(input("Variation (W) ="))
            print(" Le calcul est Cv - W = Cc \nLe Cap compas (Cc) est égal à", Cv - W, "°")
        if choix3 == 2:
            Cm = float(input("Cap magnétique = "))
            d = float(input("déviation(d) ="))
            print(" Le calcul est Cm - d = Cc \nLe Cap compas (Cc) est égal à", Cm - d, "°")
        if choix3 == 3:
            Cm = float(input("Cap magnétique = "))
            W = float(input("Variation (W) ="))
            D = float(input("Déclinaison (D) ="))
            print(" Le calcul est Cm - (W - D) = Cc \nLe Cap compas (Cc) est égal à", Cm - (W - D), "°")
        if choix3 == 4:
            Cv = float(input("Cap vrai (Cv) = "))
            d = float(input("déviation(d) ="))
            D = float(input("Déclinaison (D) ="))
            print(" Le calcul est Cv - (d + D) = Cc \nLe Cap compas (Cc) est égal à", Cv - (D + d), "°")

    if rep == 4:
        print("\n\n/Vous cherchez la Déclinaison(D)\ ")
        print("\nVous connaissez soit :"
              "\n 1.La déviation(d) et la Variation(W)"
              "\n 2.Le Cap magnétique(Cm) et le Cap vrai(Cv)"
              "\n 3.Le Cap compas(Cc),le Cap magnétique(Cm) et la la Variation (W)"
              "\n 4.Le Cap compas(Cc), le Cap vrai(Cv) et la déviation(d)"
              "\n 5.La Route surface(Rs), la dérive(der), et le Cap magnétique(Cm)")
        choix4 = int(input("\nVous disposez de :"))
        while choix4 < 1 or choix4 > 5:
            print("Veuillez choisir un nombre entre 1 et 5 qui correspondent aux options proposées")
            choix4 = int(input("\nVous disposez de :"))
        if choix4 == 1:
            d = float(input("déviation(d) = "))
            W = float(input("Variation (W) ="))
            print(" Le calcul est W - d = D \nLa Déclinaison (D) est égale à", W - d,"°")
        if choix4 == 2:
            Cm = float(input("Cap magnétique = "))
            Cv = float(input("Cap vrai (Cv) = "))
            print(" Le calcul est Cv - Cm = D \nLa Déclinaison (D) est égale à", Cv - Cm ,"°")
        if choix4 == 3:
            Cc = float(input("Cap compas (Cc) = "))
            Cm = float(input("Cap magnétique = "))
            W = float(input("Variation (W) ="))
            print(" Le calcul est Cc + W - Cm = D \nLa Déclinaison (D) est égale à", Cc + W - Cm ,"°")
        if choix4 == 4:
            Cc = float(input("Cap compas (Cc) = "))
            Cv = float(input("Cap vrai (Cv) = "))
            d = float(input("déviation(d) = "))
            print(" Le calcul est Cv - d - Cc = D \nLa Déclinaison (D) est égale à", Cv - d - Cc, "°")

        if choix4 == 5:
            Rs = float(input("Route surface (Rs) ="))
            print("Attention pour la dérive, elle est négative si le vent vient de tribord. "
                  "\n Dans ce cas de figure il faut donc mettre un - devant la valeur de la dérive. ")
            der = float(input("der ="))
            Cm = float(input("Cap magnétique = "))
            print(" Le calcul est Rs - der - Cm = D \n La Déclinaison (D) est égale à",Rs - der - Cm, "°")

    if rep == 5:
        print("\n\n/Vous cherchez la déviation(d)\ ")
        print("\nVous connaissez soit :"
              "\n 1.La Variation (W) et la Déclinaison(D)"
              "\n 2.Le Cap magnétique (Cm) et le Cap compas(Cc)"
              "\n 3.Le Cap vrai(Cv), la Déclinaison(D) et le Cap compas(Cc)"
              "\n 4.Le Cap magnétique(Cm), la Variation(W) et le Cap vrai(Cv)"
              "\n 5.La Route surface(Rs), la dérive(der),Le Cap magnétique (Cm) et la Variation(W)")
        choix5 = int(input("\nVous disposez de :"))
        while choix5 < 1 or choix5 > 5:
            print("Veuillez choisir un nombre entre 1 et 5 qui correspondent aux options proposées")
            choix5 = int(input("\nVous disposez de :"))
        if choix5 == 1:
            W = float(input("Variation (W) ="))
            D = float(input("Déclinaison (D) ="))
            print(" Le calcul est W - D = d \nLa déviation (d) est égale à", W - D, "°")
        if choix5 == 2:
            Cm = float(input("Cap magnétique = "))
            Cc = float(input("Cap compas (Cc) = "))
            print(" Le calcul est Cm - Cc = d \nLa déviation (d) est égale à", Cm - Cc, "°")
        if choix5 == 3:
            Cv = float(input("Cap vrai (Cv) = "))
            D = float(input("Déclinaison (D) ="))
            Cc = float(input("Cap compas (Cc) = "))
            print(" Le calcul est Cv - D - Cc = d \nLa déviation (d) est égale à", Cv - D - Cc, "°")
        if choix5 == 4:
            Cm = float(input("Cap magnétique = "))
            W = float(input("Variation (W) ="))
            Cv = float(input("Cap vrai (Cv) = "))
            print(" Le calcul est Cm + W - Cv = d \nLa déviation (d) est égale à", Cm + W - Cv, "°")
        if choix5 == 5:
            Rs = float(input("Route surface (Rs) ="))
            print("Attention pour la dérive, elle est négative si le vent vient de tribord. "
                  "\n Dans ce cas de figure il faut donc mettre un - devant la valeur de la dérive. ")
            der = float(input("der ="))
            Cm = float(input("Cap magnétique = "))
            W = float(input("Variation (W) ="))
            print(" Le calcul est -Rs + der + W + Cm = d \nLa déviation (d) est égale à",-Rs + der + W + Cm, "°")

    if rep == 6:
        print("\n\n/Vous cherchez la Variation (W)\ ")
        print("\nVous connaissez soit :"
              "\n 1.La Déclinaison (D) et la déviation (D)"
              "\n 2.Le Cap vrai (Cv) et le Cap compas(Cc)"
              "\n 3.La Route surface(Rs), la dérive(der) et le Cap compas(Cc)"
              "\n 4.Le Cap magnétique(Cm), le Cap compas(Cc) et la Déclinaison(D)"
              "\n 5.Le Cap vrai(Cv), le Cap compas(Cc) et la déviation(d)")
        choix6 = int(input("\nVous disposez de :"))
        while choix6 < 1 or choix6 > 5:
            print("Veuillez choisir un nombre entre 1 et 5 qui correspondent aux options proposées")
            choix6 = int(input("\nVous disposez de :"))
        if choix6 == 1:
            D = float(input("Déclinaison (D) ="))
            d = float(input("déviation(d) = "))
            print(" Le calcul est D + d = W \nLa déviation (d) est égale à", D + d , "°")
        if choix6 == 2:
            Cv = float(input("Cap vrai (Cv) = "))
            Cc = float(input("Cap compas (Cc) = "))
            print(" Le calcul est Cv - Cc = W \nLa déviation (d) est égale à",Cv - Cc, "°")
        if choix6 == 3:
            Rs = float(input("Route surface (Rs) ="))
            print("Attention pour la dérive, elle est négative si le vent vient de tribord. "
                  "\n Dans ce cas de figure il faut donc mettre un - devant la valeur de la dérive. ")
            der = float(input("der ="))
            Cc = float(input("Cap compas (Cc) = "))
            print(" Le calcul est Rs - der - Cc = W \nLa déviation (d) est égale à",Rs - der - Cc, "°")
        if choix6 == 4:
            Cm = float(input("Cap magnétique = "))
            Cc = float(input("Cap compas (Cc) = "))
            D = float(input("Déclinaison (D) ="))
            print(" Le calcul est Cm + D - Cc = W \nLa déviation (d) est égale à",Cm + D - Cc, "°")
        if choix6 == 5:
            Cv = float(input("Cap vrai (Cv) = "))
            Cc = float(input("Cap compas (Cc) = "))
            d = float(input("déviation(d) = "))
            print(" Le calcul est Cv + d - Cm = W \nLa déviation (d) est égale à",Cv + d - Cm, "°")

    if rep == 7:
        print("\n\n/Vous cherchez la Route surface(Rs)\ ")
        print("\nVous connaissez soit :"
              "\n 1.Le Cap vrai (Cv) et la dérive(der)"
              "\n 2.Le Cap compas (Cc), la variation (W) et la dérive(der)"
              "\n 3.Le Cap magnétique(m), la Déclinaison(D) et la dérive(der)")
        choix7 = int(input("\nVous disposez de :"))
        while choix7 < 1 or choix7 > 3:
            print("Veuillez choisir un nombre entre 1 et 3 qui correspondent aux options proposées")
            choix7 = int(input("\nVous disposez de :"))
        if choix7 == 1:
            Cv = float(input("Cap vrai (Cv) = "))
            print("Attention pour la dérive, elle est négative si le vent vient de tribord. "
                  "\n Dans ce cas de figure il faut donc mettre un - devant la valeur de la dérive. ")
            der = float(input("der ="))
            print(" Le calcul est Cv + der = Rs \nLa Route surface (Rs) est égale à",Cv + der, "°")
        if choix7 == 2:
            Cc = float(input("Cap compas (Cc) = "))
            W = float(input("Variation (W) ="))
            print("Attention pour la dérive, elle est négative si le vent vient de tribord. "
                  "\n Dans ce cas de figure il faut donc mettre un - devant la valeur de la dérive. ")
            der = float(input("der ="))
            print(" Le calcul est Cc + W + der = Rs \nLa Route surface (Rs) est égale à",Cc + W + der, "°")
        if choix7 == 3:
            Cm = float(input("Cap magnétique = "))
            D = float(input("Déclinaison (D) ="))
            print("Attention pour la dérive, elle est négative si le vent vient de tribord. "
                  "\n Dans ce cas de figure il faut donc mettre un - devant la valeur de la dérive. ")
            der = float(input("der ="))
            print(" Le calcul est Cm + D + der = Rs \nLa Route surface (Rs) est égale à",Cm + D + der , "°")

    if rep == 8:
        print("\n\n/Vous cherchez la Dérive(der)\ ")
        print("\nVous connaissez soit :"
              "\n 1.Le Cap vrai (Cv) et la Route surface(Rs)"
              "\n 2.Le Cap compas (Cc), la variation (W) et la Route surface(Rs)"
              "\n 3.Le Cap magnétique(m), la Déclinaison(D) et la Route surface(Rs)")
        choix8 = int(input("\nVous disposez de :"))
        while choix8 < 1 or choix8 > 3:
            print("Veuillez choisir un nombre entre 1 et 3 qui correspondent aux options proposées")
            choix8 = int(input("\nVous disposez de :"))
        if choix8 == 1:
            Cv = float(input("Cap vrai (Cv) = "))
            Rs = float(input("Route surface (Rs) ="))
            print(" Le calcul est Rs - Cv = der \nLa dérive (der) est égale à", Rs - Cv , "°")
        if choix8 == 2:
            Cc = float(input("Cap compas (Cc) = "))
            W = float(input("Variation (W) ="))
            Rs = float(input("Route surface (Rs) ="))
            print(" Le calcul est Rs - Cc - W = der \nLa dérive (der) est égale à", Rs - Cc - W , "°")
        if choix8 == 3:
            Cm = float(input("Cap magnétique = "))
            D = float(input("Déclinaison (D) ="))
            Rs = float(input("Route surface (Rs) ="))
            print(" Le calcul est Rs - Cm - D = der \nLa dérive (der) est égale à",Rs - Cm - D, "°")

    if rep == 9:
        print("\n\nVous avez le Cap Compas et la dérive (der) et d'autres donnés et vous souhaitez obtenir la route surface")
        print("\nVous connaissez soit :"
              "\n 1.Le CC + la variation (W) + der \n (affichage du cap vrai en plus)"
              "\n 2.Le CC + la déviation (d) + la Déclinaison(D) + der \n (affichage du cap vrai ET cap magnétique en plus)")
        choix9 = int(input("Vous disposez de :"))
        while choix9 < 1 or choix9 > 2:
            print("Veuillez choisir un nombre entre 1 et 2 qui correspondent aux options proposées")
            choix9 = float(input("Vous disposez de :"))
        if choix9 == 1:
            Cc= float(input("Le Cap Compas (CC) ="))
            W= float(input("La variation (W)="))
            der= float(input("La dérive ="))
            print("Le cap vrai (Cv) est égal à", Cc + W,"°\n (Cc + W = Cv")
            print("La Route surface (Rs) est",Cc + W + der, "° \n (Rs = Cv + der)")
        if choix9 == 2:
            Cc= float(input("Le Cap Compas (CC) ="))
            d = float(input("déviation(d) = "))
            D = float(input("Déclinaison (D) ="))
            print("Attention pour la dérive, elle est négative si le vent vient de tribord. "
                  "\n Dans ce cas de figure il faut donc mettre un - devant la valeur de la dérive. ")
            der = float(input("La dérive ="))
            print("Le cap magnétique s'écrit Cc + d = Cm, soit Cm=", Cc + d,
                  "° \n Le cap vrai s'écrit Cv = Cm + D, soit Cv=", Cc + d + D,
                  "° \n La variation (W) est de ", d + D, "°   (W=D+d)" )
            print("La Route surface (Rs) est", Cc + D + d + der,"°  (Rs = Cv + der)")
