import random
from direction import Direction
from heros import Heros
from monstres import Monstre
import os

TAILLE = 15


class Jeu:
    def __init__(self, heros, monstres):

        self.TAILLE_PLATEAU = TAILLE
        self.heros = heros
        self.monstres = monstres

    def afficher(self, message=""):
        os.system("cls" if os.name == "nt" else "clear")
        print("=" * 38)
        print(
            f"Héros ({self.heros.nom})  |  PV: {self.heros.points_vie}/{self.heros.endurance + self.heros.modificateur_endurance()}  |  Or: {self.heros.or_}  |  Cuir: {self.heros.cuir}"
        )
        print(
            f"Position: ({self.heros.x},{self.heros.y}) | Monstres restants: {sum(m.points_vie>0 for m in self.monstres)}"
        )
        print("=" * 38)

        grille = [
            ["." for _ in range(self.TAILLE_PLATEAU)]
            for _ in range(self.TAILLE_PLATEAU)
        ]
        grille[self.heros.x][self.heros.y] = "H"

        for m in self.monstres:
            if m.est_visible and m.points_vie > 0:
                grille[m.x][m.y] = m.symbole().upper()

        for i, ligne in enumerate(grille):
            print(" ".join(ligne))
        print("=" * 38)
        if message:
            print(message)
        print("=" * 38)

    def est_fini(self):
        return self.heros.points_vie <= 0 or all(
            m.points_vie <= 0 for m in self.monstres
        )

    def deplacer_heros(self, direction):
        mouvements = {"z": (-1, 0), "s": (1, 0), "q": (0, -1), "d": (0, 1)}
        dx, dy = mouvements.get(direction, (0, 0))
        nx, ny = self.heros.x + dx, self.heros.y + dy

        if 0 <= nx < self.TAILLE_PLATEAU and 0 <= ny < self.TAILLE_PLATEAU:
            self.heros.x, self.heros.y = nx, ny
            return self.verifier_combat()
        else:
            return "❌ Déplacement hors limites."

    def verifier_combat(self):
        for m in self.monstres:
            if (
                m.points_vie > 0
                and abs(self.heros.x - m.x) + abs(self.heros.y - m.y) == 1
            ):
                m.est_visible = True
                return self.combat(m)
        return ""

    def placer_monstres(self, nb=10):
        monstres_places = []
        essais = 0

        while len(monstres_places) < nb and essais < 550:
            x, y = random.randint(0, self.TAILLE_PLATEAU - 1), random.randint(
                0, self.TAILLE_PLATEAU - 1
            )
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
        message = (
            f"💥 Combat contre un {monstre.monstre} à ({monstre.x}, {monstre.y}) !\n"
        )
        while self.heros.points_vie > 0 and monstre.points_vie > 0:
            degats_heros = self.heros.frappe(monstre)
            message += f"Le héros inflige {degats_heros} dégâts au {monstre.monstre} (PV restant: {monstre.points_vie})\n"
            if monstre.points_vie <= 0:
                message += "✅ Monstre vaincu !\n"
                self.heros.depouiller(monstre)
                self.heros.reposer()
                break
            degats_monstre = monstre.frappe(self.heros)
            message += f"Le {monstre.monstre} inflige {degats_monstre} dégâts au héros (PV restant: {self.heros.points_vie})\n"
            if self.heros.points_vie <= 0:
                message += "💀 Le héros est mort !"
                break
        return message
