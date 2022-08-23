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

  