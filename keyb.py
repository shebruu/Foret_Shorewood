import os
import time
import keyboard

# Plateau 10x10 (tu peux le passer à 15x15)
TAILLE = 10

# Exemple : 'M' pour monstre, '.' vide, 'O' obstacle
grille = [
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "O", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", "O", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "O", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
]

# Position initiale du monstre (ou joueur)
x, y = 0, 0


def afficher_grille():
    os.system("cls" if os.name == "nt" else "clear")
    for i in range(TAILLE):
        for j in range(TAILLE):
            if i == x and j == y:
                print("M", end=" ")  # M pour monstre (ou P pour joueur)
            else:
                print(grille[i][j], end=" ")
        print()


try:
    afficher_grille()
    while True:
        mouvement = False

        # Haut
        if keyboard.is_pressed("up"):
            if x > 0 and grille[x - 1][y] == ".":
                x -= 1
                mouvement = True
        # Bas
        if keyboard.is_pressed("down"):
            if x < TAILLE - 1 and grille[x + 1][y] == ".":
                x += 1
                mouvement = True
        # Gauche
        if keyboard.is_pressed("left"):
            if y > 0 and grille[x][y - 1] == ".":
                y -= 1
                mouvement = True
        # Droite
        if keyboard.is_pressed("right"):
            if y < TAILLE - 1 and grille[x][y + 1] == ".":
                y += 1
                mouvement = True

        if mouvement:
            afficher_grille()
            time.sleep(0.12)  # Pour éviter un déplacement trop rapide
        if keyboard.is_pressed("esc"):
            print("Arrêt demandé (ESC).")
            break
        time.sleep(0.05)
except KeyboardInterrupt:
    print("Programme arrêté proprement.")
