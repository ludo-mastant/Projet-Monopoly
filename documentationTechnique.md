# Documentation du fichier `joueur.py`

## Introduction

Ce fichier contient la classe `Joueur`, qui gère les actions et l'état d'un joueur dans un jeu de Monopoly. Les actions principales incluent le tirage des dés, le déplacement sur le plateau, l'achat de terrains et le paiement de loyers.

## Classe `Joueur`

### Attributs

- **`nom`** (str) : Le nom du joueur.
- **`solde`** (int) : Le solde d'argent du joueur, initialisé à 2000 €.
- **`position`** (int) : La position actuelle du joueur sur le plateau, initialisée à 0.
- **`terter`** (list) : Liste des terrains que le joueur possède.

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

## Conclusion

Ce fichier se concentre sur la gestion des actions d'un joueur dans le cadre du jeu de Monopoly. Il permet de simuler le déplacement, l'achat de terrains et le paiement des loyers.
```