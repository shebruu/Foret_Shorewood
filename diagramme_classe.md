+-----------------------------+
|        Personnage           | <<abstract>>
+-----------------------------+
| - nom : str                 |      |
| - x : int                   |
| - y : int                   |
| - est_visible : bool        |
+-----------------------------+
| + __init__(...)             |
| + endurance |
| + force  |
| + points_vie |
| + points_vie      |
| + modificateur_force() : int|
| + position() : (int, int)   |
| + est_vivant() : bool       |
| + frappe(cible) : None      | (abstract)
  + creer_aleatoire () : 
+-----------------------------+
+-------------------+                                                                       
          ^
          |   hérite de personnage
          |
+-------------------+
|      Heros        |
+-------------------+
| - _richesse_or    |
| - _richesse_cuir  |
| - _type_heros     |
| - est_visible     |
+-------------------+
| + __init__(...)            
  + richesse_or  |
| + richesse_cuir|
| + type_heros  |
| + modificateur_force()     |                       
| + frappe(cible)            |
| + depouiller(cible)        |
| + restaurer_points_vie()   |
| + __str__()                |
+-------------------+

           ^  hérite de personnage 
           |
+----------------------+
|       Monstre        |
+----------------------+
| - _monstre: str      |
| - _richesse: dict    |
| - depecable: bool    |
+----------------------+
| + __init__(...)     
| + monstre: str       |
| + force: int         |
| + richesse: dict     |
| + symbole(): str     |
| + modificateur_force(): int |
| + frappe(cible): int |
| + __str__(): str     |
 |
+----------------------+
