import random
from Case import Case
import time
from Joueur import Joueur

from Chance import Chance 

class CaseSpeciale(Case):
    def __init__(self, nom, type_case):
        super().__init__(nom)
        self.type_case = type_case  # Peut être "bonus" ou "malus"
        if self.type_case == "chance" :

            # Création des objets CaseSpeciale (tout est de type "chance")
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

            # Liste de toutes les cases spéciales
            self.tabCartes = [
                recreation, journee_banalisee, bonne_note, reussite_scolaire,
                heure_libre, copie_double, cours_ennuyeux, heure_de_colle, bureau_du_proviseur,
                haleine_du_prof, devoir_surveille, salle_de_notes, controle_surprise
            ]

    
    def aller_prison(self, joueur):
        """Envoie le joueur en prison"""
        if self.nom == "En Prison":
            print(f"🚔 {joueur.nom} s'est fait choper en train de tricher et va en heure de colle !")
            joueur.position = 9  # La prison est sur la case 9
            joueur.en_prison = True  # Il est maintenant en prison
            # Initialiser le compteur de tours en prison
            joueur.tours_en_prison = 0

    """
    def est_en_prison(self, joueur):
        #Vérifie si le joueur est en prison
        return joueur.en_prison
    """
    
    def gerer_prison(self, joueur):
        """Gère le cas où un joueur est en prison et doit faire un 6 pour sortir ou payer pour sortir"""
        if self.nom == "Prison":
            if joueur.en_prison:
                print(f"⏳ {joueur.nom} est en prison.")

                # Compter le nombre de tours en prison
                if not hasattr(joueur, 'tours_en_prison'):
                    joueur.tours_en_prison = 1
                else:
                    joueur.tours_en_prison += 1

                # Après 3 tours, le joueur est libéré automatiquement
                if joueur.tours_en_prison >= 3:
                    print(f"🕒 {joueur.nom} a passé 3 tours en prison et est libéré automatiquement !")
                    joueur.en_prison = False
                    joueur.tours_en_prison = 0
                    return

                # Options pour sortir de prison
                print(f"Options pour {joueur.nom} :")
                print("1. Lancer le dé et espérer faire un 6")
                print("2. Payer 50€ pour sortir immédiatement")

                choix = input("Choisissez une option (1/2) : ")

                if choix == "2" and joueur.solde >= 50:
                    # Payer pour sortir
                    joueur.solde -= 50
                    print(f"💰 {joueur.nom} paie 50€ et sort de prison ! Solde restant : {joueur.solde}€")
                    joueur.en_prison = False
                    joueur.tours_en_prison = 0
                else:
                    # Lancer le dé
                    lancer_de = random.randint(1, 6)  # Simule le lancé de dé
                    print(f"🎲 {joueur.nom} a lancé un {lancer_de}.")

                    if lancer_de == 6:
                        print(f"✅ {joueur.nom} a fait un 6 et peut sortir de prison !")
                        joueur.en_prison = False
                        joueur.tours_en_prison = 0
                    else:
                        print(f"❌ {joueur.nom} reste en prison.")
            else:
                print("🏛️ Visite guidée gratuite de la prison")



"""
# Test affichage des cases spéciales
for case in cases_speciales:
    print(f"Case : {case.nom}, Type : {case.type_case}")
"""