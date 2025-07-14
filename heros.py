from abc import ABC
from personnage import Personnage
from monstres import Monstre
import random

types_heros=["humain", "nain"]
class Heros(Personnage):
    def __init__(self,force,endurance,points_vie,type_heros):
       Personnage.__init__(self,force,endurance,points_vie)
       self._st_richesse = 0
       self._typ=type_heros

    @property
    def richesse(self):
        return self._st_richesse
    @property
    def type_heros(self):
        return self._typ

    def modificateur_force(self):
        bonus=0
        if self.force < 5:
            bonus = -1

        elif self.force < 10:
            bonus = 0
        elif self.force < 15:
            bonus = 1
        else:
            bonus = 2
        return  bonus

    def frappe(self,cible):
        rand = random.randint(1, 4)
        degats= self.modificateur_force() + rand
        if cible.points_vie>0:
               cible.points_vie -=degats
        return degats

    def depouiller(self,cible):
        if cible.points_vie<=0:
            self._st_richesse +=cible.richesse
            cible.richesse=0

if __name__ == '__main__':
    hero1 = Heros(force=12, endurance=10, points_vie=22, type_heros="humain")
    monstre1 = Monstre(force=12, endurance=10,points_vie=22, monstre="orques")

