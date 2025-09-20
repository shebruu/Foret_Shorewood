# Course automobile  en Python

Bienvenue  !  


Projet pédagogique qui simule une bataille entre **héros** et **monstres** à l’aide de classes, de dés et de règles simples.

## Fonctionnalités principales
- Création de personnages de type **Héros** ou **Monstre**  
- Gestion de l’**endurance**, de la **force** et des **points de vie**  
- Système de **dés** pour calculer les actions de combat  
- Organisation des batailles entre héros et monstres  
- Gestion du **dépouillage des monstres** (or, cuir)  
- Menus de tests et scénarios prêts à l’emploi dans `main.py`  

---

## Classes principales
- **Personnage (abstraite)** : définit endurance, force et points de vie  
- **Héros** (Humain, Nain) : peuvent restaurer leurs points de vie et dépouiller les monstres  
- **Monstres** (Loup, Orque, Dragonnet) : possèdent des bonus spécifiques et des ressources  
- **ZoneJeu** : gère la carte, le placement des monstres et les combats  



          Personnage (classe abstraite)
               ▲            ▲
          Heros         Monstre
           ▲  ▲           ▲   ▲
        Humain Nain   Loup Orque Dragonnet


### Personnage (abstraite)  
Classe de base : définit endurance, force, points de vie, combat et état de mort.  

### Héros (abstraite)  
Peut dépouiller les monstres, restaurer ses points de vie et affronter un adversaire.  
- **Humain** : bonus +1 en force et endurance.  
- **Nain** : bonus +2 en endurance.  

### Monstres (abstraite)  
Possèdent des ressources (or, cuir) et parfois dépouillables.  
- **Loup** : donne du cuir.  
- **Orque** : bonus +1 en force, donne de l’or.  
- **Dragonnet** : bonus +1 en endurance, donne or et cuir.  

### Système de Dés 
Classe utilitaire pour gérer des tirages aléatoires dans un intervalle (min/max).  

### ZoneJeu  
Représente la grille de jeu :  
- placement des héros et monstres,  
- déplacements,  
- vérification des combats,  
- fin de partie.  


