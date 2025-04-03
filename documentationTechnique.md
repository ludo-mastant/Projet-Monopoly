# Documentation du fichier `joueur.py`

## Introduction

Ce fichier contient la classe `Joueur`, qui gère les actions et l'état d'un joueur dans un jeu de Monopoly. Les actions principales incluent le tirage des dés, le déplacement sur le plateau, l'achat de terrains et le paiement de loyers.

---

## Classe `Joueur`

### Attributs

- **`nom`** (str) : Le nom du joueur.
- **`solde`** (int) : Le solde d'argent du joueur, initialisé à 2000 €.
- **`position`** (int) : La position actuelle du joueur sur le plateau, initialisée à 0.
- **`terter`** (list) : Liste des terrains que le joueur possède.

---

### Méthodes

#### `__init__(self, nom, solde=2000, position=0)`

Constructeur de la classe `Joueur`. Initialise le nom, le solde et la position du joueur.

- **Paramètres** :
  - `nom` : Le nom du joueur.
  - `solde` : Le montant d'argent du joueur (par défaut 2000 €).
  - `position` : La position du joueur sur le plateau (par défaut 0).

#### `tirer_de(self)`

Simule le tirage des dés pour le joueur (un nombre aléatoire entre 1 et 6) et affiche un message indiquant le résultat.

#### `deplacement(self, nb_cases)`

Déplace le joueur de `nb_cases` sur le plateau.

- **Paramètre** :
  - `nb_cases` : Le nombre de cases à avancer.

#### `acheter(self, terrain)`

Permet au joueur d'acheter un terrain si son solde est suffisant. Si l'achat est validé, le terrain est ajouté à la liste des terrains du joueur.

- **Paramètre** :
  - `terrain` : Un objet de type `Terrain`.

#### `payer(self, terrain, autre_joueur)`

Permet au joueur de payer le loyer d'un terrain appartenant à un autre joueur. Si le joueur n'a pas assez d'argent, il donne tout son solde à l'autre joueur.

- **Paramètres** :
  - `terrain` : Le terrain pour lequel le loyer doit être payé.
  - `autre_joueur` : L'autre joueur à qui le loyer est payé.

---

## Conclusion

Ce fichier se concentre sur la gestion des actions d'un joueur dans le cadre du jeu de Monopoly. Il permet de simuler le déplacement, l'achat de terrains et le paiement des loyers.

---

# Documentation Technique : Classe `Terrain`

## Description
La classe `Terrain` hérite de `Case` et représente un terrain de jeu dans Monopoly. Elle gère l'achat de terrain, l'ajout de maisons et d'hôtels, ainsi que le calcul du loyer.

---

## Attributs

- **cout_achat** : Dictionnaire des coûts d'achat des terrains.
- **loyer_base** : Dictionnaire des loyers de base des terrains.
- **cout_maisons** : Dictionnaire des coûts d'ajout de maisons.
- **cout_hotels** : Dictionnaire des coûts d'ajout d'hôtels.
- **nom** : Nom du terrain (hérité de `Case`).
- **salle** : Numéro de la salle.
- **proprio** : Joueur propriétaire ou `None` si libre.
- **nbr_maisons** : Nombre de maisons sur le terrain.
- **nbr_hotels** : Nombre d'hôtels sur le terrain.
- **prix** : Prix d'achat du terrain.
- **loyer** : Loyer de base.
- **cout_maison** : Coût d'une maison.
- **cout_hotel** : Coût d'un hôtel.

---

## Méthodes

### `__init__(self, nom, salle, proprio=None)`
Initialise un terrain avec un nom, un numéro de salle, et un propriétaire optionnel.

### `est_achetable(self)`
Retourne `True` si le terrain est libre.

### `ameliorer_terrain(self, joueur)`
Ajoute une maison ou un hôtel si le joueur a assez d'argent.

### `acheter_terrain(self, joueur)`
Permet à un joueur d'acheter le terrain si celui-ci est libre et que le joueur a assez d'argent.

---

## Exemple d'utilisation

```python
# Création d'un terrain T24
terrain_T24 = Terrain(nom="Happy Teeth Island", salle="T24")

# Affichage du prix d'achat
print(terrain_T24.prix)

# Tentative d'achat par un joueur
joueur = Joueur(nom="Alice", solde=400)
terrain_T24.acheter_terrain(joueur)

---



