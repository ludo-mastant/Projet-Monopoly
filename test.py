# Importation des classes Joueur et Terrain
from Joueur import Joueur
from terrain import Terrain
from plateau import Plateau

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


# Test de plateau
plateau = Plateau()
print(plateau.avoir_terrain(0))  # Devrait renvoyer "Case départ"
print(plateau.avoir_terrain(1))  # Devrait renvoyer "Propriété 1"
print(plateau.avoir_terrain(25)) # Devrait renvoyer "Terrain inexistant"