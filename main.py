from direction import Direction
from heros import Heros
from monstres import Monstre
from plateau_jeu import Jeu

import traceback

try:
    monstres = plateau.placer_monstres()
except Exception as e:
    print("Une erreur est survenue :")
    traceback.print_exc()

if __name__ == "__main__":
    # Création du héros et du plateau
    heros = Heros(type_heros="humain", x=7, y=7)
    plateau = Jeu(heros, [])
    monstres = plateau.placer_monstres()
    plateau.monstres = monstres

    # Boucle principale
    while not plateau.est_fini():
        plateau.afficher()
        direction = input(
            "Déplace-toi (z: haut, s: bas, q: gauche, d: droite) : "
        ).lower()
        plateau.deplacer_heros(direction)

    if heros.points_vie <= 0:
        print("💀 Tu es mort.")
    else:
        print("🏆 Tous les monstres sont vaincus !")
