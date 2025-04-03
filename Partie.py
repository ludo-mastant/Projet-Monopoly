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
        self.peut_rejouer = False

    def choix_action(self, joueur):
        """Le joueur choisit une action : soit passer, soit acheter une propriété"""
        case_actuelle = self.plateau.cases[joueur.position % len(self.plateau.cases)]
        if isinstance(case_actuelle, Terrain) and case_actuelle.est_achetable():
            print(f"Le terrain {case_actuelle.nom} est disponible à l'achat")
            joueur.acheter(case_actuelle)
        else:
            print("Aucune action possible sur cette case")

    def deplacement(self, joueur, lancer = -1):
        """Le joueur lance le dé et avance"""
        if lancer == -1 :
            lancer = joueur.tirer_de()

        # Initialiser l'attribut a_fait_tour_complet s'il n'existe pas
        if not hasattr(joueur, 'a_fait_tour_complet'):
            joueur.a_fait_tour_complet = False

        joueur.deplacement(lancer)
        print(f"🎲 {joueur.nom} avance de {lancer} cases et arrive sur {self.plateau.cases[joueur.position % len(self.plateau.cases)]}, Nouvelle position : {joueur.position}")

        # Vérifier si le joueur a fait un tour complet (passé par la case départ)
        if joueur.a_fait_tour_complet:
            joueur.solde += 200
            print(f"💰 {joueur.nom} a fait un tour complet et reçoit 200€ ! Nouveau solde : {joueur.solde}€")
            joueur.a_fait_tour_complet = False  # Réinitialiser pour le prochain tour

    def traitement_post_deplacement(self, joueur):
        """Gestion des actions après déplacement"""
        case_actuelle = self.plateau.cases[joueur.position % len(self.plateau.cases)]

        if isinstance(case_actuelle, Terrain):
            if case_actuelle.est_achetable():
                self.choix_action(joueur)
            elif case_actuelle.proprio and case_actuelle.proprio != joueur:
                joueur.payer(case_actuelle)
        elif isinstance(case_actuelle, CaseSpeciale) and case_actuelle.type_case == "chance":
            taille = len(case_actuelle.tabCartes)
            carteTiree = random.randint(0, taille - 1)  #-1 car dernier de la liste= len(list -1)
            case_actuelle.tabCartes[carteTiree].appliquer_effet(joueur, self)
        elif isinstance(case_actuelle, CaseSpeciale) and case_actuelle.type_case == "en_prison": #si on tombe sur la case d'aller en prison
            case_actuelle.aller_prison(joueur)
        elif isinstance(case_actuelle, CaseSpeciale) and case_actuelle.type_case == "visite": #si on est sur la case de visite de la prison ( et si joueur.en_prison == true)
            case_actuelle.gerer_prison(joueur)
        elif isinstance(case_actuelle, CaseSpeciale) and case_actuelle.type_case == "évenement" and case_actuelle.nom == "Réunion Parent-Prof":
            # Gestion de la case Réunion Parent-Prof
            montant = 75
            if joueur.solde < montant:
                print(f"❌ {joueur.nom} n'a pas assez d'argent pour payer la réunion parent-prof. Il donne tout ce qu'il a ({joueur.solde}€).")
                joueur.solde = -1  # Le joueur est en faillite
            else:
                joueur.solde -= montant
                print(f"📝 {joueur.nom} assiste à une réunion parent-prof et perd {montant}€. Solde restant : {joueur.solde}€")


    def afficher_menu_joueur(self, joueur):
        """Affiche le menu d'options pour le joueur au début de son tour"""
        while True:
            print(f"\n📋 Menu pour {joueur.nom} :")
            print("1. Lancer le dé et jouer son tour")
            print("2. Voir son solde")
            print("3. Voir ses propriétés")
            print("4. Améliorer ses propriétés (construire des maisons)")
            print("5. Voir le plateau")
            print("0. Quitter la partie")

            choix = input("Choisissez une option (1-5, 0 pour quitter) : ")

            if choix == "1":
                # Jouer son tour
                return True
            elif choix == "2":
                # Voir son solde
                print(f"💰 Solde de {joueur.nom} : {joueur.solde}€")
            elif choix == "3":
                # Voir ses propriétés
                self.afficher_proprietes(joueur)
            elif choix == "4":
                # Améliorer ses propriétés
                self.ameliorer_proprietes(joueur)
            elif choix == "5":
                # Voir le plateau
                self.afficher_plateau()
            elif choix == "0":
                # Quitter la partie
                if input("Êtes-vous sûr de vouloir quitter la partie ? (o/n) : ").lower() == "o":
                    print("Fin de la partie.")
                    exit()
            else:
                print("Option invalide, veuillez réessayer.")

    def afficher_proprietes(self, joueur):
        """Affiche les propriétés du joueur"""
        if not joueur.terter:
            print(f"🏠 {joueur.nom} ne possède aucune propriété.")
            return

        print(f"\n🏠 Propriétés de {joueur.nom} :")
        for i, terrain in enumerate(joueur.terter, 1):
            statut = ""
            if terrain.nbr_hotels == 1:
                statut = "🏨 Hôtel"
            elif terrain.nbr_maisons > 0:
                statut = f"🏡 Maisons: {terrain.nbr_maisons}"
            else:
                statut = "Terrain sans amélioration"

            print(f"{i}. {terrain.nom} ({terrain.salle}) - {statut}")
            print(f"   Prix d'achat: {terrain.prix}€ - Loyer actuel: {terrain.loyer}€")

    def ameliorer_proprietes(self, joueur):
        """Permet au joueur d'améliorer ses propriétés en construisant des maisons ou des hôtels"""
        if not joueur.terter:
            print(f"🏠 {joueur.nom} ne possède aucune propriété à améliorer.")
            return

        print(f"\n🏗️ Amélioration des propriétés de {joueur.nom} :")
        for i, terrain in enumerate(joueur.terter, 1):
            statut = ""
            if terrain.nbr_hotels == 1:
                statut = "🏨 Hôtel"
            else:
                statut = f"🏡 Maisons: {terrain.nbr_maisons}/4"

            if terrain.nbr_hotels == 1:
                cout = "Max atteint"
            elif terrain.nbr_maisons == 4:
                cout = f"Hôtel: {terrain.cout_hotel}€"
            else:
                cout = f"Maison: {terrain.cout_maison}€"

            print(f"{i}. {terrain.nom} - {statut} - Coût d'amélioration: {cout}")

        print("0. Retour au menu")

        choix = input("Choisissez une propriété à améliorer (0 pour retour) : ")
        if choix == "0":
            return

        try:
            index = int(choix) - 1
            if 0 <= index < len(joueur.terter):
                terrain = joueur.terter[index]
                terrain.ameliorer_terrain(joueur)
            else:
                print("Numéro de propriété invalide.")
        except ValueError:
            print("Entrée invalide, veuillez entrer un nombre.")

    def afficher_plateau(self):
        """Affiche l'état actuel du plateau"""
        print("\n🎮 État du plateau :")
        for i, case in enumerate(self.plateau.cases):
            proprietaire = ""
            if isinstance(case, Terrain) and case.proprio:
                proprietaire = f" (Propriétaire: {case.proprio.nom})"
            print(f"{i}. {case.nom}{proprietaire}")

    def tour(self, joueur, lancer = -1):
        """Un tour complet d'un joueur"""
        if joueur.solde < 0:
            return  # Le joueur est en faillite

        print(f"\n🎭 C'est au tour de {joueur.nom} !")

        # Si le joueur est en prison, on gère directement la prison
        if joueur.en_prison:
            case_prison = self.plateau.cases[9]  # La prison est à la case 9
            if isinstance(case_prison, CaseSpeciale) and case_prison.nom == "Prison":
                case_prison.gerer_prison(joueur)
                # Si le joueur est sorti de prison, on le fait jouer normalement
                if not joueur.en_prison:
                    # Afficher le menu avant de jouer
                    if self.afficher_menu_joueur(joueur):
                        self.deplacement(joueur, lancer)
                        time.sleep(3)
                        self.traitement_post_deplacement(joueur)
                        time.sleep(3)
        else:
            # Afficher le menu avant de jouer
            if self.afficher_menu_joueur(joueur):
                # Tour normal
                self.deplacement(joueur, lancer)
                time.sleep(3)
                self.traitement_post_deplacement(joueur)
                time.sleep(3)

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
            # Changement de joueur
            joueur = self.joueurs[self.tour_actuel % len(self.joueurs)]

            # Vérifier si le joueur doit attendre des tours
            if joueur.tours_a_attendre > 0:
                print(f"{joueur.nom} doit attendre encore {joueur.tours_a_attendre} tour(s)")
                joueur.tours_a_attendre -= 1
                self.tour_actuel += 1
                continue

            # si le joueur peut jouer
            if not self.joueur_faillite(joueur):
                self.tour(joueur)

                # le joueur peut rejouer
                if joueur.peut_rejouer:
                    print(f"{joueur.nom} peut rejouer immédiatement!")
                    joueur.peut_rejouer = False
                else:
                    self.tour_actuel += 1
                
                # La gestion de la prison se fait dans la méthode tour
                # Pas besoin d'incrémenter tour_actuel ici car c'est déjà fait plus haut
            else:
                self.tour_actuel += 1

        self.definir_gagnant()

# Lancer une partie
if __name__ == "__main__":
    reponse = int(input("Combien de joueurs pour votre super Partie de Monopoly School Edition  2/4 ?"))
    if reponse == 2 :
        j1 = input("Quelle est le nom du Joueur 1 ? " )
        j2 = input("Quelle est le nom du Joueur 2 ? ")
        noms_joueurs = [j1, j2]
    if reponse == 3 :
        j1 = input("Quelle est le nom du Joueur 1 ? " )
        j2 = input("Quelle est le nom du Joueur 2 ? ")
        j3 = input("Quelle est le nom du Joueur 3 ? ")
        noms_joueurs = [j1, j2,j3]
    if reponse == 4 :
        j1 = input("Quelle est le nom du Joueur 1 ? " )
        j2 = input("Quelle est le nom du Joueur 2 ? ")
        j3 = input("Quelle est le nom du Joueur 3 ? ")
        j4 = input("Quelle est le nom du Joueur 4 ? ")
        noms_joueurs = [j1, j2,j3,j4]
    jeu = Monopoly(noms_joueurs)
    print("C'est partie pour le jeu !")
    time.sleep(3)
    jeu.jouer_partie()