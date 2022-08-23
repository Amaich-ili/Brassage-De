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

    def comparer_des(self, d1):
        if (self.dé_1 + self.dé_2) > (d1.dé_1 + d1.dé_2):
            return True
        else:
            return False

    def info(self):
        return [self.nb_face,self.dé_1,self.dé_2]