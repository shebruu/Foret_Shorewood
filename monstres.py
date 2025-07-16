from personnage import Personnage
from de import De
from personnage import lancer_4d6_garder_3_meilleurs
import random
types_monstres = {
    "loup": "L",
    "orques": "O",
    "dragonnets": "D"
}
class Monstre(Personnage):
    def __init__(self, monstre,x,y):
        self.monstre = monstre.lower()

        endurance = endurance if endurance is not None else lancer_4d6_garder_3_meilleurs()
        force = force if force is not None else lancer_4d6_garder_3_meilleurs()

        # Bonus spécifiques AVANT super() pour que PV soit correct
        bonus_force = 1 if monstre == "orques" else 0
        bonus_endurance = 1 if monstre == "dragonnets" else 0

        endurance += bonus_endurance
        force += bonus_force
      

        self._monstre = monstre
        de4 = De(1, 4)
        de6 = De(1, 6)

        # Richesses aléatoires selon le type de monstre
        if monstre == "loup":
            self._richesse = {"or": 0, "cuir": de4.lancer_de()}
            self.depecable = True
        elif monstre == "orques":
            self._richesse = {"or": de6.lancer_de(), "cuir": 0}
            self.depecable = False
        elif monstre == "dragonnets":
            self._richesse = {
                "or": de6.lancer_de(),
                "cuir": de4.lancer_de()
            }
            self.depecable = True
        else:
            self._richesse = {"or": 0, "cuir": 0}
            self.depecable = False
    @property
    def force(self):
        return self._force

    @property
    def monstre(self):
        return self._monstre

    @monstre.setter
    def monstre(self, value):
        if value in types_monstres:
            self._monstre = value

    @property
    def richesse(self):
        return self._richesse

    @richesse.setter
    def richesse(self, value):
        self._richesse = value


    def symbole(self):
        return types_monstres.get(self.monstre, "?")

    def modificateur_force(self):
        """Bonus/malus basé sur la force réelle (avec bonus orque déjà inclus)"""
        if self.force < 5:
            return -1
        elif self.force < 10:
            return 0
        elif self.force < 15:
            return 1
        else:
            return 2

    def frappe(self, cible):
        de4 = De(1, 4)  # Dé à 4 faces
        rand = de4.lancer_de()
        degats = self.modificateur_force() + rand
        if cible.points_vie > 0:
            # ne pas avoir de pv négatif
            cible.points_vie = max(0, cible.points_vie - degats)
        return degats



    def __str__(self):
        return (f"{self._monstre.capitalize()} - For: {self.force} "
                f"({self.modificateur_force():+d}), End: {self.endurance}, "
                f"PV: {self.points_vie}, Richesse: {self._richesse}")
