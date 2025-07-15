from abc import ABC, abstractmethod
import random
from de import De
def lancer_4d6_garder_3_meilleurs():
    """
    Lance 4 dés à 6 faces et retourne la somme des 3 meilleurs résultats.
    """
    d6 = De(1, 6)
    des = [d6.lancer_de() for _ in range(4)]
    des.sort(reverse=True)
    return sum(des[:3])
def modificateur(caracteristique):
    if caracteristique < 5:
        return -1

    elif caracteristique < 10:
        return  0
    elif caracteristique < 15:
        return 1
    else:
        return 2



class Personnage(ABC):

    def __init__(self, endurance, force, points_vie=None):
        self._endurance =  endurance if endurance is not None else lancer_4d6_garder_3_meilleurs()
        self._force = force if force is not None else lancer_4d6_garder_3_meilleurs()
        self._points_vie= points_vie if points_vie is not None else modificateur(self._endurance)

    @property
    def endurance(self):
        return self._endurance
    @property
    def force(self):
        return self._force
    @property
    def points_vie(self):
        return self._points_vie
    @points_vie.setter
    def points_vie(self, points_vie):
        self._points_vie = points_vie

    def modificateur_force(self):
        return modificateur(self.force)

    @abstractmethod
    def frappe(self,monstre):
        pass

    def est_vivant(self):
        return self.points_vie > 0

    def calculer_points_de_vie(self):
        return self._endurance + modificateur(self._endurance)

