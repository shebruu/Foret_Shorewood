import random
from direction import Direction
from heros import Heros
from monstres import Monstre

TAILLE = 15
class Jeu:
    def __init__(self,heros,monstres):
     
        self.TAILLE_PLATEAU = TAILLE
        self.TAILLE_PLATEAU = TAILLE
        self.heros = heros
        self.monstres = monstres


    def afficher(self):
        print(f"\n📍 Héros en position : ({self.heros.x}, {self.heros.y})")
        if not (0 <= self.heros.x < self.TAILLE_PLATEAU and 0 <= self.heros.y < self.TAILLE_PLATEAU):
            raise ValueError("Le héros est en dehors des limites du plateau.")

        grille = [["." for _ in range(self.TAILLE_PLATEAU)] for _ in range(self.TAILLE_PLATEAU)]
        grille[self.heros.x][self.heros.y] = "H"

        for m in self.monstres:
            if m.est_visible and m.points_vie > 0:
                if 0 <= m.x < self.TAILLE_PLATEAU and 0 <= m.y < self.TAILLE_PLATEAU:
                    grille[m.x][m.y] = m.symbole()

        print("\n--- Plateau ---")
        for ligne in grille:
            print(" ".join(ligne))

    def est_fini(self):
        return self.heros.points_vie <= 0 or all(m.points_vie <= 0 for m in self.monstres)

    def deplacer_heros(self, direction):
        mouvements = {"z": (-1, 0), "s": (1, 0), "q": (0, -1), "d": (0, 1)}
        dx, dy = mouvements.get(direction, (0, 0))
        nx, ny = self.heros.x + dx, self.heros.y + dy

        if 0 <= nx < self.TAILLE_PLATEAU and 0 <= ny < self.TAILLE_PLATEAU:
            self.heros.x, self.heros.y = nx, ny
            self.verifier_combat()
        else:
            print("❌ Déplacement hors limites.")

    def verifier_combat(self):
        for m in self.monstres:
            if m.points_vie > 0:
                if abs(self.heros.x - m.x) + abs(self.heros.y - m.y) == 1:
                    m.est_visible = True
                    print(f"💥 Combat avec un {m.monstre} !")
                    while m.points_vie > 0 and self.heros.points_vie > 0:
                        degats = self.heros.frappe(m)
                        print(f"Héros frappe : -{degats} PV à {m.monstre}")
                        if m.points_vie > 0:
                            degats = m.frappe(self.heros)
                            print(f"{m.monstre} frappe : -{degats} PV au héros")
                    if self.heros.points_vie <= 0:
                        print("💀 Le héros est mort.")
                    elif m.points_vie <= 0:
                        print(f"✅ {m.monstre} vaincu !")

    def placer_monstres(self,nb=10):
        monstres_places = []
        essais = 0

        while len(monstres_places) < nb and essais < 550:
            x, y = random.randint(0, self.TAILLE_PLATEAU-1), random.randint(0, self.TAILLE_PLATEAU-1)
            if self.espace_libre(x, y, monstres_places):
                monstre_type = random.choice(["loup", "orques", "dragonnets"])
                m = Monstre(monstre=monstre_type, x=x, y=y)
                monstres_places.append(m)
            essais += 1
        return monstres_places

    def espace_libre(self, x, y, liste):
        for m in liste:
            if abs(m.x - x) < 2 and abs(m.y - y) < 2:
                return False
        if (x, y) == (self.heros.x, self.heros.y):
            return False
        return True
    def detecter_monstres(self):
        for monstre in self.monstres:
            if abs(monstre.x - self.heros.x) + abs(monstre.y - self.heros.y) == 1:
                monstre.est_visible = True
                self.combat(monstre)

    def combat(self, monstre):
        print(f"💥 Combat contre un {monstre.nom} à ({monstre.x}, {monstre.y}) !")
        # Exemple de système de combat simple
        monstre.vie = 0
        self.heros.vie -= 10
        if monstre.vie <= 0:
            print(f"✅ {monstre.nom} vaincu !")
        if self.heros.vie <= 0:
            print("💀 Le héros est mort.")