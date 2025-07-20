import os
import time
import keyboard

from heros import Heros
from monstres import Monstre
from plateau_jeu import Jeu


def effacer_console():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    # Héros au centre du plateau 15x15
    heros = Heros(type_heros="humain", x=7, y=7)
    jeu = Jeu(heros, [])
    jeu.monstres = jeu.placer_monstres(10)

    # Correspondance touches/flèches → directions classiques 'z', 's', 'q', 'd'
    directions = {"up": "z", "down": "s", "left": "q", "right": "d"}

    effacer_console()
    jeu.afficher()
    try:
        while not jeu.est_fini():
            mouvement = False
            for key, dir_lettre in directions.items():
                if keyboard.is_pressed(key):
                    jeu.deplacer_heros(dir_lettre)
                    effacer_console()
                    jeu.afficher()
                    mouvement = True
                    time.sleep(0.18)
                    break
            if keyboard.is_pressed("esc"):
                print("Arrêt du jeu demandé (ESC).")
                break
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("Programme arrêté proprement.")

    if heros.points_vie <= 0:
        print("💀 Tu es mort.")
    else:
        print("🏆 Tous les monstres sont vaincus !")


if __name__ == "__main__":
    main()
