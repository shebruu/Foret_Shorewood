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

"""
hero1 = Heros(force=12, endurance=10, points_vie=22, type_heros="humain")
monstre1=Monstre(force=12, endurance=10, points_vie=22, monstre="loup")

print("frappe  1", hero1.frappe(monstre1))

"""

# Exemple d'utilisation et test
if __name__ == "__main__":
    # Créer un héros
    hero = Heros(force=12, endurance=10, points_vie=22, type_heros="humain")


    # Créer une cible fictive pour le test
    class CibleTest:
        def __init__(self, pv, richesse):
            self.points_vie = pv
            self.richesse = richesse


    cible1 = CibleTest(15, 50)

    print("=== Test de combat ===")
    print(f"Héros: {hero}")
    print(f"Cible: PV={cible1.points_vie}, Richesse={cible1.richesse}")

    # Test de frappe
    degatss = hero.frappe(cible1)
    print(f"Cible après frappe: PV={cible1.points_vie}")

    # Frapper jusqu'à ce que la cible soit morte
    while cible1.points_vie > 0:
        hero.frappe(cible1)

    print(f"Cible finale: PV={cible1.points_vie}")

    # Test de dépouillement
    print(f"Richesse du héros avant dépouillement: {hero.richesse}")
    hero.depouiller(cible1)
    print(f"Richesse du héros après dépouillement: {hero.richesse}")
    print(f"Richesse de la cible: {cible1.richesse}")