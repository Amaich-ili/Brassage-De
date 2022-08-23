# Iliass Amaich
from random import randint


class Dés:
    def __init__(self, nb_face = 24, dé_1 = 0, dé_2 = 0):
        self.nb_face = nb_face
        self.dé_1 = dé_1
        self.dé_2 = dé_2

    def brasser_des(self):
        self.dé_1 = randint(1, self.nb_face)
        self.dé_2 = randint(1, self.nb_face)
        return [self.dé_1, self.dé_2]

    def comparer_des(self, d):
        if (self.dé_1 + self.dé_2) > (d.dé_1 + d.dé_2):
            return True
        else:
            return False

    def info(self):
        return [self.nb_face,self.dé_1,self.dé_2]

# Demander à l'utilisateur de saisir les attributs de la classe(nombre de faces,l'état initial de premier dés,l'état initial de deuxième dés )
cdt1 = False
while not cdt1:
    cmd_1 = int(input("Entrer le nombre de faces voulu : "))
    if not 6 <= cmd_1 <= 24 :
        print("Vous devez choisir un nombre de faces entre 6 et 24")
    else:
        cdt1 = True

cmd_2 = int(input("Entrer le nombre de l'état initial de premier dés : "))
cmd_3 = int(input("Entrer le nombre de l'état initial de deuxième dés : "))

# Utiliser les données introduits pour instancier la classe
d = Dés(cmd_1, cmd_2, cmd_3)
d1 = Dés()

print(f"Instance 1 de la classe Dés :\nLe nombre de faces est : {d.info()[0]} \nle numero de Dé 1 est : {d.info()[1]} \net lnumero de Dé 2 est : {d.info()[2]}\n")
print(f"Instance 2 de la classe Dés :\nLe nombre de faces est : {d1.info()[0]} \nle numero de Dé 1 est : {d1.info()[1]} \net lnumero de Dé 2 est : {d1.info()[2]}\n")