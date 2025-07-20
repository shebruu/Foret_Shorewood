from personnage import Personnage
from de import De


class Heros(Personnage):
    def __init__(self, type_heros, x=0, y=0):
        super().__init__(nom=type_heros, x=x, y=y)
        self.or_ = 0
        self.cuir = 0
        self.nom = type_heros
        # Application des bonus de type
        if type_heros.lower() == "humain":
            self._force += 1
            self._endurance += 1
        elif type_heros.lower() == "nain":
            self._endurance += 2
        # Mise à jour des PV max après bonus
        self._points_vie = self._endurance + self.modificateur_endurance()
        self.est_visible = True

    def reposer(self):
        # Restaure les PV max
        self._points_vie = self._endurance + self.modificateur_endurance()

    def depouiller(self, cible):
        # Cible est  mort
        if cible.points_vie > 0:
            print("Impossible de dépouiller un monstre encore vivant !")
            return
        self.or_ += getattr(cible, "or_", 0)
        self.cuir += getattr(cible, "cuir", 0)
        # Vider le butin du monstre
        if hasattr(cible, "or_"):
            cible.or_ = 0
        if hasattr(cible, "cuir"):
            cible.cuir = 0

    def frappe(self, cible):
        de4 = De(1, 4)
        rand = de4.lancer_de()
        dommages = rand + self.modificateur_force()
        cible.points_vie = max(0, cible.points_vie - dommages)
        return dommages

    def __str__(self):
        return (
            f"{self.nom.capitalize()} - For: {self.force}, End: {self.endurance}, "
            f"PV: {self.points_vie}, Or: {self.or_}, Cuir: {self.cuir}"
        )
