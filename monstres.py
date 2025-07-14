from abc import ABC

from personnage import Personnage

types_monstres=["loup", "orques","dragonnets"]
class Monstre(Personnage, ABC):
    def __init__(self,force,endurance,points_vie,monstre, ms_richesse):
        Personnage.__init__(force,endurance,points_vie)
        self._monstre=monstre
        self.ms_richesse=0
        self.depece=None


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
