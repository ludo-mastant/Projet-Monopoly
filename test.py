"""

# Importation des classes Joueur et Terrain
from plateau import Plateau
from Joueur import Joueur
from terrain import Terrain

# Création de deux joueurs
joueur1 = Joueur(nom="Alice", solde=2000, position=0)
joueur2 = Joueur(nom="Bob", solde=1500, position=0)

# Création d'un terrain
terrain1 = Terrain(nom="Happy Teeth Island", salle="T24", proprio=None)

# Test de la méthode tirer_de pour le joueur 1
de_1 = joueur1.tirer_de()
print(f"Joueur {joueur1.nom} a tiré un {de_1}")

# Test du déplacement du joueur 1
joueur1.deplacement(de_1)
print(f"Joueur {joueur1.nom} est maintenant à la position {joueur1.position}")

# Test de l'achat du terrain
joueur1.acheter(terrain1)

# Le joueur 2 va essayer d'acheter le même terrain (pour tester la condition d'achat)
joueur2.acheter(terrain1)

# Test du paiement du loyer par le joueur 1 au joueur 2
terrain1.proprio = joueur2  # Le terrain a été acheté par joueur2
joueur1.payer(terrain1)  # Joueur 1 doit payer le loyer à joueur 2

# Test de l'ajout de maison sur le terrain 1 (par le propriétaire)
terrain1.ameliorer_terrain(joueur2)

# Test de l'ajout d'un hôtel sur le terrain 1 (par le propriétaire)
terrain1.ameliorer_terrain(joueur2)
terrain1.ameliorer_terrain(joueur2)
terrain1.ameliorer_terrain(joueur2)
terrain1.ameliorer_terrain(joueur2)  # Doit avoir maintenant 4 maisons
terrain1.ameliorer_terrain(joueur2)  # Doit transformer les maisons en un hôtel

# Affichage des résultats
print(f"Le solde de {joueur1.nom} est maintenant {joueur1.solde}€")
print(f"Le solde de {joueur2.nom} est maintenant {joueur2.solde}€")
print(f"Le terrain {terrain1.nom} a {terrain1.nbr_maisons} maison(s) et {terrain1.nbr_hotels} hôtel(s).")



plateau = Plateau()
print(plateau.avoir_terrain(0))  # Devrait renvoyer "Case départ"
print(plateau.avoir_terrain(1))  # Devrait renvoyer "Propriété 1"
print(plateau.avoir_terrain(25)) # Devrait renvoyer "Terrain inexistant"

"""

from Joueur import Joueur
from terrain import Terrain
from CaseSpeciale import CaseSpeciale
import random

# Création des joueurs
j1=str(input("Quel est le nom du Joueur 1 ?"))
j2=str(input("Quel est le nom du Joueur 2 ?"))
joueur1 = Joueur(j1)
joueur2 = Joueur(j2)

# Création de quelques terrains
terrain1 = Terrain("Happy Teeth Island", "T24")
terrain2 = Terrain("Salle A104", "A104")

# Création des cases spéciales
recreation = CaseSpeciale("Récréation", "chance")
journee_banalisee = CaseSpeciale("Journée banalisée", "chance")
bonne_note = CaseSpeciale("Bonne Note", "chance")
reussite_scolaire = CaseSpeciale("Réussite scolaire", "chance")
heure_libre = CaseSpeciale("Heure libre", "chance")
copie_double = CaseSpeciale("Copie double", "chance")

cours_ennuyeux = CaseSpeciale("Cours ennuyeux", "chance")
heure_de_colle = CaseSpeciale("Heure de colle", "chance")
bureau_du_proviseur = CaseSpeciale("Bureau du proviseur", "chance")
haleine_du_prof = CaseSpeciale("Haleine du prof", "chance")
devoir_surveille = CaseSpeciale("Devoir Surveillé", "chance")
salle_de_notes = CaseSpeciale("Salle de Notes", "chance")
controle_surprise = CaseSpeciale("Contrôle surprise", "chance")

# Liste de toutes les cases spéciales
cases_speciales = [
    recreation, journee_banalisee, bonne_note, reussite_scolaire,
    heure_libre, copie_double, cours_ennuyeux, heure_de_colle, bureau_du_proviseur,
    haleine_du_prof, devoir_surveille, salle_de_notes, controle_surprise
]

# Test affichage des cases spéciales
print("\n--- TEST AFFICHAGE DES CASES SPECIALES ---")
for case in cases_speciales:
    print(f"Case : {case.nom}, Type : {case.type_case}")

# Test achat d'un terrain par un joueur
print("\n--- TEST ACHAT TERRAIN ---")
joueur1.acheter(terrain1)

# Test si un joueur tombe sur une case spéciale
case_tiree = random.choice(cases_speciales)
print(f"\n--- TEST CASE SPECIALE ({case_tiree.nom}) ---")
case_tiree.appliquer_effet(joueur1)

# Test paiement du loyer si un joueur atterrit sur un terrain possédé
print("\n--- TEST PAIEMENT LOYER ---")
terrain1.proprio = joueur2  # Bob devient propriétaire du terrain
joueur1.payer(terrain1)

