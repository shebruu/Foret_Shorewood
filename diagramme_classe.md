+-----------------------------+
|        Personnage           | <<abstract>>
+-----------------------------+
| + Force        |     
  + Endurance :int
  + pv : int
| - x : int                   |
| - y : int                   |
+-----------------------------+
| + __init__(...)             |
| + frappe(cible) : None      | (abstract)
| + est_vivant() : bool       |
| + modificateur_force(int) : int|

| + endurance | getter :int
| + force  | getter : int
| + points_vie | getter, setter :int
| + position() : (int, int)   
|
  + creer_aleatoire () : 
+-----------------------------+
+-------------------+                                                                       
          ^
          |   hérite de Personnage et referénce  le De
          |
+-------------------+
|      Heros        |
+-------------------+
| + cuir     |
  + or
  + nom: string
     |
+-------------------+
| + __init__(...)            
  + reposer()|
| + depouiller(cible)        |

| + modificateur_force()     |                       
| + frappe(cible)            |
| + __str__()         
+-------------------+

           ^  hérite de Personnage 
           |
+----------------------+
|       Monstre        |
+----------------------+
 + Or: int
+----------------------+
| + __init__(...)     
|  

| + frappe(cible): int |
| + __str__(): str     |
 |
+----------------------+

+----------------------+
|       Jeu        |
+----------------------+
+ grille[15][15]
+ personnages: list(personnage)
+----------------------+
| + __init__(...)     
| + combat  |
| + deplacer_heros: bool      |
| + afficher_matrice: str   |

| + est_fini: int   |
| + verifier_combat(): str     |
| + placer_monstres(): int |
| + espaces_libre: int |
| + detecter_monstres|
 |
+----------------------+

Humain        hérite de Heros 

+----------------------+

Nain       hérite de Heros
+----------------------+


+----------------------+
|      Loup        |   hérite de Monstre 
+----------------------+
+cuir : 
+----------------------+
 |+ 0/4
+----------------------+

+----------------------+
|      dragonnet        |
+----------------------+
+cuir 
+or
+----------------------+
| +  0/4
| +  0/6
+----------------------+
+----------------------+
|     orque         |
+----------------------+
+or
+----------------------+ 
|+ 0/6




statique 
+----------------------+
|      De        |
+----------------------+
+min :int
+max : int|
+----------------------+
| + __init__(...)     
|+ lancer_de (min,max)
 |
+----------------------+