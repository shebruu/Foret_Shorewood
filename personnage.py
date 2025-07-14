from abc import ABC, abstractmethod
import random

def lancer_4d6_garder_3_meilleurs():
    """
    Lance 4 dés à 6 faces et retourne la somme des 3 meilleurs résultats.
    """
    des = [random.randint(1, 6) for _ in range(4)]
    des.sort(reverse=True)  # Trier en ordre décroissant
    return sum(des[:3])  # Prendre les 3 meilleurs

def modificateur(caracteristique):
    if caracteristique < 5:
        caracteristique -=1

    elif caracteristique < 10:
        caracteristique += 0
    elif caracteristique < 15:
        caracteristique += 1
    else:
        caracteristique += 2



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



    @abstractmethod
    def frappe(self,monstre):
        pass

    def est_vivant(self):
        if self.points_vie:
            return True
        return None

