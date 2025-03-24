from Joueur import Joueur

class Terrain :

    cout_achat = {
        'T11': 60,          #TOSONI ET ARACIL
        'T24 BIS': 100,     #AUDIER
        'T22': 140,         #PALISSE
        'T21': 180,         #FASCENTE ET MERLO
        'A104': 220,        #ABDELAZIZ
        'T10': 300,         #MEUNIER
        'T24': 350,         #VATANT ET JANUEL
    }

    loyer = {
        'T11': 40,
        'T24 BIS': 80,
        'T22': 120,
        'T21': 160,
        'A104': 200,
        'T10': 280,
        'T24': 330,
    }

    cout_maisons = {
        'T11': 100,
        'T24 BIS': 100,
        'T22': 150,
        'T21': 150,
        'A104': 200,
        'T10': 300,
        'T24': 350,
    }

    cout_hotels = {
        'T11': 500,
        'T24 BIS': 500,
        'T22': 700,
        'T21': 700,
        'A104': 900,
        'T10': 950,
        'T24': 1000,
    }

    def __init__(self, nom, salle, nbr_maison, nbr_hotel, proprio=None) :
        self._nom = nom
        self._salle = salle
        self._nbr_maison = nbr_maison
        self._nbr_hotel = nbr_hotel
        self._proprio = proprio
    
    """Méthodes est_achetable"""
    
    def est_achetable(self):

        """Un terrain est achetable si il n'y a pas de proprio"""

        if self._proprio == True :
            print("Le terrain",self._proprio,"n'est pas achetable")
        else :
            print("Le terrain",self._proprio,"est achetable")
        return 
    
    """Méthodes ameliorer_terrain"""

    def ameliorer_terrain(self):
        
        """Améliore le terrain (rajoute des maisons ou des hôtels)."""
        
        if self.nb_hotels == 1:
            print(self.nom,  "a déjà un hôtel. Impossible d'améliorer davantage.")
            return
        
        if self.nb_maisons < 4:
            if Joueur.solde >= self.cout_maisons:
                self._nb_maisons += 1
                Joueur.solde -= self.cout_maisons
                print("Une maison a été ajoutée sur", self._nom)
            else:
                print("Le joueur n'a pas assez d'argent pour ajouter une maison.")
        elif self._nb_maisons == 4:
            if Joueur.solde >= self.cout_hotels:
                self._nb_hotels += 1
                self._nb_maisons = 0  # 4 maisons deviennent un hôtel
                Joueur.solde -= self.cout_hotels
                print("Un hôtel a été ajouté sur", self._nom)
            else:
                print("Le joueur n'a pas assez d'argent pour ajouter un hôtel.")
    
    """Accesseur de la classe terrain"""

    def getLoyer(self):
        return self.loyer
    
    def getNom(self):
        return self._nom
    
    def getPrix(self):
        return self.cout_achat
    