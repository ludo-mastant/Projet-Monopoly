from plateau import Plateau

# test 1 :

plateau = Plateau()
print(plateau.avoir_terrain(0))  # Devrait renvoyer "Case départ"
print(plateau.avoir_terrain(1))  # Devrait renvoyer "Propriété 1"
print(plateau.avoir_terrain(25)) # Devrait renvoyer "Terrain inexistant"