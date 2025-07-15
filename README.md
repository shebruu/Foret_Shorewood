# Course automobile  en Python

Bienvenue  !  

Projet pédagogique pour apprendre la programmation orientée objet  



## ✨ Fonctionnalités principales
Permet de créer des personnages de types Héros ou Monstres
Chaque Personnage a une Endurance, Force, Points de vie. À chaque tour, 4 dés sont lancé pour déterminer la force et l endurace du personnage
- Organise la bataille entre les héros et monstres.
- Calcule les points de vies, la force, l'endurance de chaque personnage  
- Gere le dépouillage de richesse des monstres
- Menus de tests et scénarios dans `main.py`


          Personnage (classe abstraite)
               ▲            ▲
          Heros         Monstre
           ▲  ▲           ▲   ▲
        Humain Nain   Loup Orque Dragonnet



classes abstraite
Personnage (abstract)
-------------------------------
- _endurance : int
- _force : int
- _points_vie : int
- x : int
- y : int
-------------------------------
+ endurance : int (lecture seule)
+ force : int (lecture seule)
+ points_vie : int (lecture seule ou private)
+ modificateur(valeur: int) : int
+ est_mort() : bool
+ frappe(cible: Personnage) : int
+ calculer_points_de_vie() : int (optionnel si centralisé)

classes enfants 
Heros (abstract)
-------------------------------
- richesse_or : int
- richesse_cuir : int
-------------------------------
+ depouiller(monstre: Monstre)
+ restaurer_points_vie()
+ affronter(monstre: Monstre)

Humain
-------------------------------
+ bonus : force +1, endurance +1 (sans modifier les vraies valeurs)

Nain
-------------------------------
+ bonus : endurance +2 (sans modifier la valeur de base)

Monstre (abstract)
-------------------------------
- or : int
- cuir : int
- depecable : bool
-------------------------------
+ generer_ressources()


Loup
-------------------------------
+ bonus : aucun
+ depecable : True (cuir)

Orque
-------------------------------
+ bonus : force +1
+ or (1d6)

Dragonnet
-------------------------------
+ bonus : endurance +1
+ or (1d6), cuir (1d4)
+ depecable : True


| Monstre       | Bonus force | Bonus endurance | Or    | Cuir  | Dépeçable |
| ------------- | ----------- | --------------- | ----- | ----- | --------- |
| **Loup**      | 0           | 0               | ❌     | ✅ 1d4 | ✅         |
| **Orque**     | +1          | 0               | ✅ 1d6 | ❌     | ❌         |
| **Dragonnet** | 0           | +1              | ✅ 1d6 | ✅ 1d4 | ✅         |

De
-------------------------------
- _min : int
- _max : int
-------------------------------
+ min : int (lecture seule)
+ max : int (lecture seule)
+ lancer() : int



ZoneJeu
-------------------------------
- grille : List[List[str]]
- monstres : List[Monstre]
- heros : Heros
-------------------------------
+ afficher_carte()
+ placer_monstres()
+ deplacer_heros(x: int, y: int)
+ verifier_combat()
+ jeu_termine() : bool

## Démarrage

1. Clone le projet :
   ```bash
   git clone <url_du_repo>
   cd <nom_du_dossier>
2. Lance le fichier principal pour découvrir :
   python main.py

Structure : avec import absolu car pas de modle, main.py est ds le  meme dossier 
from voiture import Voiture