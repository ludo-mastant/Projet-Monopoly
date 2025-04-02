import time
import random
from plateau import Plateau
from Joueur import Joueur
from terrain import Terrain
from CaseSpeciale import CaseSpeciale

class Monopoly:
    def __init__(self, joueurs_noms):
        self.plateau = Plateau()
        self.joueurs = [Joueur(nom) for nom in joueurs_noms]
        self.tour_actuel = 0

    def choix_action(self, joueur):
        """Le joueur choisit une action : soit passer, soit acheter une propriété"""
        case_actuelle = self.plateau.cases[joueur.position]
        if isinstance(case_actuelle, Terrain) and case_actuelle.est_achetable():
            print("Y'a un prob vieux")
            joueur.acheter(case_actuelle)
        else:
            print("Faut payer vieux")

    def deplacement(self, joueur):
        """Le joueur lance le dé et avance"""
        lancer = joueur.tirer_de()
        joueur.deplacement(lancer)
        print(f"🎲 {joueur.nom} avance de {lancer} cases et arrive sur {self.plateau.cases[joueur.position % len(self.plateau.cases)]}, Nouvelle position : {joueur.position}")

    def traitement_post_deplacement(self, joueur):
        """Gestion des actions après déplacement"""
        case_actuelle = self.plateau.cases[joueur.position % len(self.plateau.cases)]
        
        if isinstance(case_actuelle, Terrain):
            if case_actuelle.est_achetable():
                self.choix_action(joueur)
            elif case_actuelle.proprio and case_actuelle.proprio != joueur:
                joueur.payer(case_actuelle)
        elif isinstance(case_actuelle, CaseSpeciale):
            case_actuelle.appliquer_effet(joueur)

    def tour(self, joueur):
        """Un tour complet d'un joueur"""
        if joueur.solde < 0:
            return  # Le joueur est en faillite

        print(f"\n🎭 C'est au tour de {joueur.nom} !")
        self.deplacement(joueur)
        self.traitement_post_deplacement(joueur)

    def joueur_faillite(self, joueur):
        """Vérifie si un joueur est en faillite"""
        return joueur.solde < 0

    def definir_gagnant(self):
        """Détermine le gagnant de la partie"""
        gagnant = max(self.joueurs, key=lambda joueur: joueur.solde)
        print(f"🏆 {gagnant.nom} remporte la partie avec {gagnant.solde}€ !")

    def jouer_partie(self):
        """Boucle principale du jeu"""
        while sum(not self.joueur_faillite(j) for j in self.joueurs) > 1:
            joueur = self.joueurs[self.tour_actuel % len(self.joueurs)]
            if not self.joueur_faillite(joueur):
                self.tour(joueur)
            self.tour_actuel += 1
        
        self.definir_gagnant()

# Lancer une partie
if __name__ == "__main__":
    j1 = input("Quelle est le nom du Joueur 1 ? " )
    j2 = input("Quelle est le nom du Joueur 2 ? ")
    noms_joueurs = [j1, j2]
    jeu = Monopoly(noms_joueurs)
    print("C'est partie pour le jeu !")
    time.sleep(3)
    jeu.jouer_partie()