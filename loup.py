
from monstres import Monstre
from de import De


class Loup(Monstre):
    def symbole(self):
        return "L"

    def richesse(self):
        return {"or": 0, "cuir": De(1, 4).lancer_de()}

    @property
    def depecable(self):
        return True