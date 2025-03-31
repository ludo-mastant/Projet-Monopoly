from Case import Case

class Terrain(Case):
    # Coût d'achat en fonction du numéro de salle
    cout_achat = {
        'T11': 60, 'T24 BIS': 100, 'T22': 140, 'T21': 180, 
        'A104': 220, 'T10': 300, 'T24': 350
    }

    # Loyer de base en fonction du numéro de salle
    loyer_base = {
        'T11': 40, 'T24 BIS': 80, 'T22': 120, 'T21': 160, 
        'A104': 200, 'T10': 280, 'T24': 330
    }

    # Coût pour ajouter une maison/hôtel
    cout_maisons = {
        'T11': 100, 'T24 BIS': 100, 'T22': 150, 'T21': 150, 
        'A104': 200, 'T10': 300, 'T24': 350
    }

    cout_hotels = {
        'T11': 500, 'T24 BIS': 500, 'T22': 700, 'T21': 700, 
        'A104': 900, 'T10': 950, 'T24': 1000
    }

    def __init__(self, nom, salle, proprio=None):
        """Initialisation du terrain"""
        super().__init__(nom)
        self.salle = salle  # Numéro de salle 
        self.proprio = proprio  #
        self.nbr_maisons = 0
        self.nbr_hotels = 0

        # Récupération des valeurs selon la salle
        self.prix = Terrain.cout_achat.get(salle, 0)
        self.loyer = Terrain.loyer_base.get(salle, 0)
        self.cout_maison = Terrain.cout_maisons.get(salle, 0)
        self.cout_hotel = Terrain.cout_hotels.get(salle, 0)

    def est_achetable(self):
        """Retourne True si le terrain n’a pas de propriétaire"""
        return self.proprio is None

    def ameliorer_terrain(self, joueur):
        """
        Améliore le terrain :
        - Ajoute une maison si possible
        - Transforme 4 maisons en 1 hôtel si possible
        """
        if self.nbr_hotels == 1:
            print(f"Le terrain {self.nom} a déjà un hôtel. Impossible d'améliorer davantage.")
            return

        if self.nbr_maisons < 4:
            if joueur.solde >= self.cout_maison:
                joueur.solde -= self.cout_maison
                self.nbr_maisons += 1
                print(f"🏡 Maison ajoutée sur {self.nom}. Solde restant : {joueur.solde}€")
            else:
                print(f"{joueur.nom} n'a pas assez d'argent pour ajouter une maison sur {self.nom}.")
        elif self.nbr_maisons == 4:
            if joueur.solde >= self.cout_hotel:
                joueur.solde -= self.cout_hotel
                self.nbr_maisons = 0  # On enlève les maisons
                self.nbr_hotels = 1  # On ajoute un hôtel
                print(f"🏨 Hôtel ajouté sur {self.nom}. Solde restant : {joueur.solde}€")
            else:
                print(f"{joueur.nom} n'a pas assez d'argent pour ajouter un hôtel sur {self.nom}.")

    def acheter_terrain(self, joueur):
        """Permet à un joueur d'acheter un terrain s'il est libre et a assez d'argent"""
        if self.est_achetable():
            if joueur.solde >= self.prix:
                joueur.solde -= self.prix
                self.proprio = joueur
                print(f"{joueur.nom} a acheté {self.nom} ({self.salle}) pour {self.prix}€. Solde restant : {joueur.solde}€")
            else:
                print(f"{joueur.nom} n'a pas assez d'argent pour acheter {self.nom} !")
        else:
            print(f"{self.nom} appartient déjà à {self.proprio.nom} !")

    """def get_loyer(self):
        #Retourne le loyer à payer en fonction du nombre de maisons/hôtels
        if self.nbr_hotels == 1:
            return self.loyer * 10  # Loyer multiplié avec un hôtel
        return self.loyer * (1 + self.nbr_maisons * 0.5)  # Loyer augmente avec les maisons
    """


   # Créer un terrain appelé "Happy Teeth Island" dans la salle T24
#happy_teeth_island = Terrain(nom="Happy Teeth Island", salle="T24")

"""
# Affichage des détails du terrain
print(f"Nom du terrain : {happy_teeth_island.nom}")
print(f"Numéro de salle : {happy_teeth_island.salle}")
print(f"Prix d'achat : {happy_teeth_island.prix}€")
print(f"Loyer de base : {happy_teeth_island.loyer}€")
print(f"Coût de la maison : {happy_teeth_island.cout_maison}€")
print(f"Coût de l'hôtel : {happy_teeth_island.cout_hotel}€")
"""
    