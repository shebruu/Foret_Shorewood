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
    """
    Calcule le modificateur associé à une caractéristique (force ou endurance).
    """
    if caracteristique < 5:
        return -1

    elif caracteristique < 10:
        return  0
    elif caracteristique < 15:
        return 1
    else:
        return 2




class Personnage(ABC):
    def __init__(self, nom, endurance=None, force=None, points_vie=None, x=None, y=None):
        self.nom = nom

        # Génération automatique si valeurs non fournies
        self._endurance = endurance if endurance is not None else lancer_4d6_garder_3_meilleurs()
        self._force = force if force is not None else lancer_4d6_garder_3_meilleurs()

        # Calcul des points de vie si non fournis
        self._points_vie = points_vie if points_vie is not None else self.calculer_points_de_vie()

        # Position sur le plateau
        self.x = x
        self.y = y

        # Par défaut les monstres sont invisibles
        self.est_visible = False

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
    def points_vie(self, pv):
        self._points_vie =max(0, pv)

    def modificateur_force(self):
        return modificateur(self.force)
    def position(self):
        return self.x, self.y

    def est_vivant(self):
        return self.points_vie > 0


    @abstractmethod
    def frappe(self, cible):
        """
        Méthode abstraite : chaque sous-classe doit définir comment elle frappe.
        """
        pass

    def calculer_points_de_vie(self):
        return self._endurance + modificateur(self._endurance)

