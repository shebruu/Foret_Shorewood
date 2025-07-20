from personnage import Personnage
from de import De

types_monstres = {"loup": "L", "orque": "O", "dragonnet": "D"}


class Monstre(Personnage):
    def __init__(self, monstre, x=0, y=0):
        super().__init__(nom=monstre, x=x, y=y)
        self.monstre = monstre.lower()
        # Application des bonus AVANT PV (on modifie les attributs privés !)
        if self.monstre == "orque":
            self._force += 1
        if self.monstre == "dragonnet":
            self._endurance += 1
        #  recalcule les PV max après bonus endurance
        self._points_vie = self._endurance + self.modificateur_endurance()
        # Richesses et dépecabilité selon type
        de4 = De(1, 4)
        de6 = De(1, 6)
        if self.monstre == "loup":
            self.cuir = de4.lancer_de()
            self.or_ = 0
            self.depecable = True
        elif self.monstre == "orque":
            self.cuir = 0
            self.or_ = de6.lancer_de()
            self.depecable = False
        elif self.monstre == "dragonnet":
            self.cuir = de4.lancer_de()
            self.or_ = de6.lancer_de()
            self.depecable = True
        else:
            self.cuir = 0
            self.or_ = 0
            self.depecable = False

    def symbole(self):
        return types_monstres.get(self.monstre, "?")

    def frappe(self, cible):
        de4 = De(1, 4)
        rand = de4.lancer_de()
        degats = self.modificateur_force() + rand
        cible.points_vie = max(0, cible.points_vie - degats)
        return degats

    def __str__(self):
        return (
            f"{self.monstre.capitalize()} - For: {self.force} "
            f"({self.modificateur_force():+d}), End: {self.endurance}, "
            f"PV: {self.points_vie}, Or: {self.or_}, Cuir: {self.cuir}"
        )
