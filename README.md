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



## Démarrage

1. Clone le projet :
   ```bash
   git clone <url_du_repo>
   cd <nom_du_dossier>
2. Lance le fichier principal pour découvrir :
   python main.py

3. 
Déplace-toi avec les flèches.

Quand tu passes à côté d’un monstre, un combat commence automatiquement et le message du combat s’affiche (PV enlevés, victoire, défaite...).
  ( Le héros frappe le monstre, Le monstre frappe le héros, Cela continue (plusieurs tours d’affilée) jusqu’à ce que l’un des deux meure.), Si le héros gagne : il gagne or et/ou cuir, ses PV sont restaurés, et il peut continuer d’explorer.

Si le héros perd : la partie est finie (“💀 Tu es mort.”).

Le plateau ne montre les monstres que quand ils sont “révélés” (combat commencé).

Si tu ne croises pas de monstre : rien ne se passe ! (C’est normal... mais tu peux mettre le héros ailleurs pour tester.)