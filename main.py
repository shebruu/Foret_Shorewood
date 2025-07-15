from personnage import Personnage
from heros import Heros
from monstres import Monstre

if __name__ == '__main__':
    hero1 = Heros(force=12, endurance=10, points_vie=22, type_heros="humain")
    monstre1 = Monstre(force=12, endurance=10,points_vie=22, monstre="orques")

    print("frappe  1", hero1.frappe(monstre1))
