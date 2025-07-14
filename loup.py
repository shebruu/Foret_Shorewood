from monstres import  Monstre
import random
class Loup(Monstre):
    def __init__(self, force=None, endurance=None):
        force = force or random.randint(8, 12)
        endurance = endurance or random.randint(6, 10)
        points_vie = force + endurance - 2
        super().__init__(force, endurance, points_vie, "loup")
