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
        self.dé_1 = randint(6, self.nb_face)
        self.dé_2 = randint(6, self.nb_face)
        return [self.dé_1, self.dé_2]

    def comparer_des(self, d):
        if (self.dé_1 + self.dé_2) >= (d.dé_1 + d.dé_2):
            print("\n\tLa somme de votre Dés est superieur ou égale à celle de l'odinateur\n")
        else:
            print("\n\tLa somme de votre Dés est inférieur à celle de l'odinateur\n")

    # afficher les informations de la classe
    def info(self):
        return [self.nb_face,self.dé_1,self.dé_2]

# Menu utilisateur 
def menu():

    # Premier menu
    conditiont1 = False
    while not conditiont1:
        nombre_face = int(input("Entrer le nombre de faces voulu : "))
        if not 6 <= nombre_face <= 24:
            print("Vous devez choisir un nombre de faces entre 6 et 24")
        else:
            conditiont1 = True

    conditiont2 = False
    while not conditiont2:
        valeur_de1 = int(input("Entrer le nombre de l'état initial de premier dés : "))
        if not 0 <= valeur_de1 <= nombre_face:
            print(f"Vous devez choisir un nombre entre 0 et {nombre_face}")
        else:
            conditiont2 = True

    conditiont3 = False
    while not conditiont3:
        valeur_de2 = int(input("Entrer le nombre de l'état initial de deuxième dés : "))
        if not 0 <= valeur_de2 <= nombre_face:
            print(f"Vous devez choisir un nombre entre 0 et {nombre_face}")
        else:
            conditiont3 = True
    
    # Utiliser les données introduits par l'utilisateur pour instancier la classe
    d = Dés(nombre_face, valeur_de1, valeur_de2)

    # Instancier la classe par défaut
    d1 = Dés(nombre_face)

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