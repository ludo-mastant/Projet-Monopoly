import random
from Case import Case  # Importation de la classe Case, probablement pour gérer les cases du jeu
import time
from Joueur import Joueur  # Importation de la classe Joueur, probablement pour gérer les actions des joueurs

from Chance import Chance  # Importation de la classe Chance, utilisée pour gérer les cartes Chance du jeu

class CaseSpeciale(Case):
    def __init__(self, nom, type_case):
        super().__init__(nom)  # Appel du constructeur de la classe parent Case pour initialiser le nom de la case
        self.type_case = type_case  # Attribue le type de la case (bonus, malus ou chance)

        # Si la case est de type "chance", on crée toutes les cartes Chance possibles
        if self.type_case == "chance":
            # Création des différentes cartes Chance avec des descriptions spécifiques
            recreation = Chance("Récréation")
            journee_banalisee = Chance("Journée banalisée")
            bonne_note = Chance("Bonne Note")
            reussite_scolaire = Chance("Réussite scolaire")
            heure_libre = Chance("Heure libre")
            copie_double = Chance("Copie double")

            cours_ennuyeux = Chance("Cours ennuyeux")
            heure_de_colle = Chance("Heure de colle")
            bureau_du_proviseur = Chance("Bureau du proviseur")
            haleine_du_prof = Chance("Haleine du prof")
            devoir_surveille = Chance("Devoir Surveillé")
            salle_de_notes = Chance("Salle de Notes")
            controle_surprise = Chance("Contrôle surprise")

            # Liste de toutes les cartes Chance qui peuvent être tirées
            self.tabCartes = [
                recreation, journee_banalisee, bonne_note, reussite_scolaire,
                heure_libre, copie_double, cours_ennuyeux, heure_de_colle, bureau_du_proviseur,
                haleine_du_prof, devoir_surveille, salle_de_notes, controle_surprise
            ]

    # Méthode pour gérer l'envoi en prison du joueur (case spécifique "En Prison")
    def aller_prison(self, joueur):
        """Envoie le joueur en prison"""
        if self.nom == "En Prison":
            print(f"🚔 {joueur.nom} s'est fait choper en train de tricher et va en heure de colle !")
            joueur.position = 9  # La prison est définie sur la case numéro 9
            joueur.en_prison = True  # Le joueur est désormais en prison
            # Initialisation du compteur de tours en prison
            joueur.tours_en_prison = 0

    """
    # Méthode pour vérifier si un joueur est en prison (commentée car non utilisée ici)
    def est_en_prison(self, joueur):
        # Vérifie si le joueur est en prison
        return joueur.en_prison
    """
    
    # Méthode pour gérer la sortie de prison (case "Prison")
    def gerer_prison(self, joueur):
        """Gère le cas où un joueur est en prison et doit faire un 6 pour sortir ou payer pour sortir"""
        if self.nom == "Prison":
            if joueur.en_prison:  # Si le joueur est en prison
                print(f"⏳ {joueur.nom} est en prison.")

                # On vérifie le nombre de tours passés en prison
                if not hasattr(joueur, 'tours_en_prison'):
                    joueur.tours_en_prison = 1  # Si c'est le premier tour, on l'initialise à 1
                else:
                    joueur.tours_en_prison += 1  # Sinon, on incrémente le nombre de tours

                # Après 3 tours en prison, le joueur est libéré automatiquement
                if joueur.tours_en_prison >= 3:
                    print(f"🕒 {joueur.nom} a passé 3 tours en prison et est libéré automatiquement !")
                    joueur.en_prison = False  # Le joueur n'est plus en prison
                    joueur.tours_en_prison = 0  # Réinitialisation du compteur de tours
                    return

                # Propose deux options au joueur pour sortir de prison
                print(f"Options pour {joueur.nom} :")
                print("1. Lancer le dé et espérer faire un 6")
                print("2. Payer 50€ pour sortir immédiatement")

                choix = input("Choisissez une option (1/2) : ")

                if choix == "2" and joueur.solde >= 50:
                    # Si le joueur choisit de payer et a assez d'argent, il sort de prison
                    joueur.solde -= 50  # Déduction de l'argent du joueur
                    print(f"💰 {joueur.nom} paie 50€ et sort de prison ! Solde restant : {joueur.solde}€")
                    joueur.en_prison = False  # Le joueur n'est plus en prison
                    joueur.tours_en_prison = 0  # Réinitialisation du compteur de tours
                else:
                    # Sinon, on lance le dé pour essayer de sortir
                    lancer_de = random.randint(1, 6)  # Simulation du lancé de dé
                    print(f"🎲 {joueur.nom} a lancé un {lancer_de}.")

                    if lancer_de == 6:
                        print(f"✅ {joueur.nom} a fait un 6 et peut sortir de prison !")
                        joueur.en_prison = False  # Le joueur sort de prison
                        joueur.tours_en_prison = 0  # Réinitialisation du compteur de tours
                    else:
                        print(f"❌ {joueur.nom} reste en prison.")  # Si le joueur ne fait pas 6, il reste en prison
            else:
                # Si le joueur n'est pas en prison, il peut visiter la prison sans conséquence
                print("🏛️ Visite guidée gratuite de la prison")



"""
# Test affichage des cases spéciales
for case in cases_speciales:
    print(f"Case : {case.nom}, Type : {case.type_case}")
"""
