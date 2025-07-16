from abc import ABC
from personnage import Personnage
from de import De
import random

types_heros=["humain", "nain"]

class Heros(Personnage):
    def __init__(self, type_heros,x=0,y=0):
       super().__init__(nom=type_heros, x=x, y=y)
       self._richesse_or = 0
       self._richesse_cuir = 0

       self._typ=type_heros
       self.est_visible = True


    @property
    def richesse_or(self):
        return self._richesse_or

    @property
    def richesse_cuir(self):
        return self._richesse_cuir
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

    def frappe(self, cible: "Monstre"):
        de4 = De(1, 4)
        rand=de4.lancer_de()

        dommages = self.modificateur_force() + rand
        if cible.points_vie > 0:
            cible.points_vie = max(0, cible.points_vie - dommages)
         
        return dommages



    def depouiller(self, cible: "Monstre"):
        if cible.points_vie > 0:
            print("Impossible de dépouiller un monstre encore vivant !")
            return

        # Accès via le dictionnaire 'richesse'
        self._richesse_or += cible.richesse.get("or", 0)
        self._richesse_cuir += cible.richesse.get("cuir",0)
        cible.richesse["or"] = 0
        cible.richesse["cuir"] = 0

    def restaurer_points_vie(self):
        self._points_vie = self.calculer_points_de_vie()
    def __str__(self):
        return f"{self.type_heros.capitalize()} - For: {self.force}, End: {self.endurance}, PV: {self.points_vie}, Or: {self.richesse_or}, Cuir: {self.richesse_cuir}"



"""
if __name__ == '__main__':
    from monstres import Monstre  # décalé ici pour éviter la boucle

    hero1 = Heros(force=12, endurance=10, points_vie=22, type_heros="humain")
    monstre1 = Monstre(force=12, endurance=10, points_vie=22, monstre="orques")

    print("=== Test de combat ===")
    print(f"Héros : {hero1}")
    print(f"Cible : PV = {monstre1.points_vie}, Or = {monstre1.richesse['or']}, Cuir = {monstre1.richesse['cuir']}")

    # Combat
    while monstre1.points_vie > 0:
        degats = hero1.frappe(monstre1)
        print(f"Frappe : {degats} dégâts, PV cible = {monstre1.points_vie}")

    print(f"\nCible finale : PV = {monstre1.points_vie}")

    # Test de dépouillement
    print(f"\nRichesse du héros avant : Or = {hero1.richesse_or}, Cuir = {hero1.richesse_cuir}")
    hero1.depouiller(monstre1)
    print(f"Richesse du héros après : Or = {hero1.richesse_or}, Cuir = {hero1.richesse_cuir}")
    print(f"Richesse restante cible : Or = {monstre1.richesse['or']}, Cuir = {monstre1.richesse['cuir']}")
"""