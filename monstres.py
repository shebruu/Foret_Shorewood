

from personnage import Personnage
from heros import Heros
import random
types_monstres=["loup", "orques","dragonnets"]



class Monstre(Personnage):
    def __init__(self,force,endurance,points_vie,monstre):
        Personnage.__init__(self, force, endurance, points_vie)
        self._monstre=monstre
        self.ms_richesse=0
        self.depece=None


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

    @property
    def force(self):
        return self._force


    @property
    def monstre(self):
        return self._monstre

    @monstre.setter
    def monstre(self,value):
        if value in types_monstres:
            self._monstre=value


    @property
    def ms_richesse(self):
        return self.ms_richesse

    @ms_richesse.setter
    def ms_richesse(self,value):
        self.ms_richesse=value
    def __str__(self):
        return f"{self._monstre.capitalize()} - For: {self._force} ({self.modificateur_force():+d}), End: {self.endurance}, PV: {self.points_vie}, Richesse: {self.ms_richesse}"
