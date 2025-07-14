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

classes abstraite
Personnages (Endurance, Force)
@abstractMethod
+calculerpointsdevie(endurance_modificateur)
+frappe(Force_modificateur)
+estmort()

classes enfants 
Héros :Humain, nain
+depouiller (monstre,richesse)
+reposer()
+restaurer_points_vie()
+affronter_monstres(monstre)

Monstres : Loup, Orque, Dragonnet
(depece,force,endurance,richesse)

Dés (min,max)
+lance_de()



## Démarrage

1. Clone le projet :
   ```bash
   git clone <url_du_repo>
   cd <nom_du_dossier>
2. Lance le fichier principal pour découvrir :
   python main.py

Structure : avec import absolu car pas de modle, main.py est ds le  meme dossier 
from voiture import Voiture