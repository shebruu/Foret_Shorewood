from abc import ABC, abstractmethod

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
        return 0
    elif caracteristique < 15:
        return 1
    else:
        return 2


class Personnage(ABC):
    """
    Classe abstraite représentant un personnage du jeu avec des caractéristiques principales et des méthodes de base.
    """

    def __init__(
        self,
        nom: str,
        x: int = 0,
        y: int = 0,
    ):
        self.nom = nom

        # Génération automatique si valeurs non fournies
        self._endurance = lancer_4d6_garder_3_meilleurs()
        self._force = lancer_4d6_garder_3_meilleurs()

        # Position sur le plateau
        self.x = x
        self.y = y

        self.est_visible = False

        self._points_vie = self._endurance + modificateur(self._endurance)

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
        self._points_vie = max(0, pv)

    @abstractmethod
    def frappe(self, cible):

        pass

    def est_vivant(self):
        return self.points_vie > 0

    def modificateur_force(self, valeur=None):
        if valeur is None:
            valeur = self.force
        return modificateur(valeur)

    def modificateur_endurance(self, valeur=None):
        if valeur is None:
            valeur = self.endurance
        return modificateur(valeur)

    def position(self) -> tuple[int, int]:
        return self.x, self.y

    def __repr__(self):
        return (
            f"<Personnage nom={self.nom} PV={self.points_vie} pos=({self.x},{self.y})>"
        )
