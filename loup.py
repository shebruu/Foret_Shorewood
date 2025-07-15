
from monstres import Monstre
from de import De


class Loup(Monstre):
    def __init__(self, endurance, force, points_vie):
        super().__init__(endurance, force, points_vie, monstre="loup")
        d4 = De(1, 4)
        # Ici, le loup ne donne que du cuir, pas d'or
        self._richesse = {"or": 0, "cuir": d4.lancer_de()}
        self.depecable = True  # plus lisible que "depece"

    def modificateur_force(self):
        # Si tu veux surcharger, sinon utilise celui de Monstre
        return super().modificateur_force()
