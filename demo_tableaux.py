import os
import time
import keyboard

# Créer un tableau de (grille) 10x10 cases
# Chaque élément contient :
# - '.' pour une case vide
# - 'O' pour un obstacle (infranchissable)
# - 'P' pour le personnage 

grille = [
	['.','.','.','.','.','.','.','.','.','.'],
	['.','.','.','.','.','.','.','.','.','.'],
	['.','.','.','.','.','.','.','O','.','.'],
	['.','.','.','.','.','.','.','.','.','.'],
	['.','.','.','.','.','.','.','.','.','.'],
	['.','.','O','.','.','.','.','.','.','.'],
	['.','.','.','.','.','.','.','.','.','.'],
	['.','.','.','.','.','.','.','O','.','.'],
	['.','.','.','.','.','.','.','.','.','.'],
	['.','.','.','.','.','.','.','.','.','.']
]

# position initiale du joueur (en haut gauche)
x, y = 0,0

def afficher_grille():
	"""
	Rafraichit l'affichage de la grille dans la console
	Affiche :
	- 'P' pour la position du joueur
	- 'O' pour les obstacles
	- '.' pour les cases
	"""

	# Efface la console
	os.system('cls' if os.name == 'nt' else 'clear')

	# Parcours des lignes et colonnes pour afficher chaque cases
	for i in range(10):
		for j in range(10):
			# On affiche 'P' si c'est la position du joueur
			if i == x and j == y:
				print('p', end=" ")
			# Sinon on affiche le contenus réel de la case
			else:
				print(grille[i][j], end=" ")
		print() # retour a la ligne a la fin de chaque ligne de la matrice

try:
    afficher_grille()
    
    while True:
        # On utilise comme flag => savopir si un déplacement a été effectué
        mouvement = False
        
        # Détection des touches directionnels avec 'keybord.is_pressed'
        
        # Haut => Déplacement vers le haut (X diminue)
        if keyboard.is_pressed('up'):
            if x > 0 and grille[x-1][y] == '.': # Vérifie qu'on ne sort pas de la grille et qu'il n'y ai pas d'obstacle
                x -= 1
                mouvement = True
        # Bas => Déplacement vers le bas (X augmente)
        if keyboard.is_pressed('down'):
            if x < 9 and grille[x+1][y] == '.':
                x += 1
                mouvement = True
        
        # Gauche => Déplacement vers la gauche (y diminue)
        if keyboard.is_pressed('left'):
            if y > 0 and grille[x][y-1] == '.':
                y -= 1
                mouvement = True
                
        # Droite => Déplacement vers la droite (y augmente)
        if keyboard.is_pressed('right'):
            if y < 9 and grille[x][y+1] == ".":
                y += 1
                mouvement = True
        
        #Si le joueur s'est déplacé, on rafraichit l'affichage de la grille
        if mouvement:
            afficher_grille()
            time.sleep(0.1) # Petite pause pour éviter un déplacement trop rapide
except KeyboardInterrupt:
    # Permet d'arreter proprement le programme avec CTRL+C sans message d'erreur
    print("Programme arreté proprement")