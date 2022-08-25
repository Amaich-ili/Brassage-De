"""
Iliass Amaich

Programme qui permet de brasser et de comparer les Dés 
"""

from random import randint

class Dés:
    def __init__(self, nb_face = 24, dé_1 = 0, dé_2 = 0):
        self.nb_face = nb_face
        self.dé_1 = dé_1
        self.dé_2 = dé_2

    def brasser_des(self):
        self.dé_1 = randint(6, 24)
        self.dé_2 = randint(6, 24)
        return [self.dé_1, self.dé_2]

    def comparer_des(self, d):
        if (self.dé_1 + self.dé_2) >= (d.dé_1 + d.dé_2):
            print("La somme de votre Dés est superieur à celle de l'odinateur")
        else:
            print("La somme de votre Dés est inférieur à celle de l'odinateur")

    # afficher les informations de la classe
    def info(self):
        return [self.nb_face,self.dé_1,self.dé_2]

# Menu utilisateur 
def menu():

    # Premier menu
    cdt1 = False
    while not cdt1:
        cmd_1 = int(input("Entrer le nombre de faces voulu : "))
        if not 6 <= cmd_1 <= 24:
            print("Vous devez choisir un nombre de faces entre 6 et 24")
        else:
            cdt1 = True

    cdt2 = False
    while not cdt2:
        cmd_2 = int(input("Entrer le nombre de l'état initial de premier dés : "))
        if not 0 <= cmd_2 <= cmd_1:
            print(f"Vous devez choisir un nombre entre 0 et {cmd_1}")
        else:
            cdt2 = True

    cdt3 = False
    while not cdt3:
        cmd_3 = int(input("Entrer le nombre de l'état initial de deuxième dés : "))
        if not 0 <= cmd_3 <= cmd_1:
            print(f"Vous devez choisir un nombre entre 0 et {cmd_1}")
        else:
            cdt3 = True

    # Utiliser les données introduits par l'utilisateur pour instancier la classe
    d = Dés(cmd_1, cmd_2, cmd_3)

    # Instancier la classe par défaut
    d1 = Dés()

    print(
        f"\nInstance 1 de la classe Dés :\n\tLe nombre de faces est : {d.info()[0]} \n\tle numero sur le Dé 1 est : {d.info()[1]} \n\tet lnumero sur le Dé 2 est : {d.info()[2]}\n")
    print(
        f"Instance 2 de la classe Dés :\n\tLe nombre de faces est : {d1.info()[0]} \n\tle numero sur le Dé 1 est : {d1.info()[1]} \n\tet lnumero sur le Dé 2 est : {d1.info()[2]}\n")
    
    # Deuxieme menu
    condition = False
    while not condition:
        menu = int(input("1. Brasser les dés \n2. Comparer les dés \n3. Sortir \nEntrer votre choix : "))
        if menu == 1:
            print(f"le numero sur le Dé 1 est : {d.brasser_des()[0]} , et le numero sur le Dé 2 est : {d.brasser_des()[1]}")
            print(f"le numero sur le  Dé 1 est : {d1.brasser_des()[0]} , et le 1numero sur le Dé 2 est : {d1.brasser_des()[1]}")
        elif menu == 2:
            d.comparer_des(d1)
        elif menu == 3:
            print("Bonne journée !")
            print("\n FIN DE PROGRAMME")
            condition = True
        else:
            print(" Vous devez saisir un numero entre 1 et 3 ")
menu()