import random
from terrain import Terrain 

class Joueur:

    def __init__(self, nom, solde = 2000 , position = 0 ):
        self.nom = nom
        self.solde = solde
        self.position = position
        self.terter = []
        self.en_prison = False
        self.lance_divise_par_2 = False
        self.tours_a_attendre = 0
        self.peut_rejouer = False
        self.a_fait_tour_complet = False


    def tirer_de(self):
        tirer = random.randint(1,6)
        #print (f"Le joueur {self.nom} a tiré " , tirer , )
        #self.position += tirer
        return tirer

    def deplacement(self, nb_cases):
        '''
        deplacement sert a faire bouger le joueur sur le plateau 
        @params self : objet de type Joueur
                nb_cases : int
        @return void
        '''
        if not self.lance_divise_par_2 == True:
            nouvelle_position = self.position + nb_cases
            # Si la nouvelle position dépasse la taille du plateau, c'est un tour complet
            self.a_fait_tour_complet = nouvelle_position >= 23
            self.position = int(nouvelle_position) % 23  # tirer
        else:
            nouvelle_position = (self.position + nb_cases) / 2
            # Si la nouvelle position dépasse la taille du plateau, c'est un tour complet
            self.a_fait_tour_complet = nouvelle_position >= 23
            self.position = int(nouvelle_position) % 23
            self.lance_divise_par_2 = False  # le lancé /2 est fini
    def acheter(self, terrain):
        """
            Le joueur achete le terrain terrain
        """
        #possede = []
        achete = int(input(f'{self.nom} , voulez vous acheter le terrain {terrain.nom} ? (0/1)'))
        if achete == 1 :
            if self.solde >= terrain.prix :
                self.solde -= terrain.prix
                print (f"Le joueur {self.nom} a acheté le terrain {terrain.nom} pour le prix de {terrain.prix} € , il lui reste donc {self.solde} €")
                self.terter.append(terrain)
                terrain.proprio = self
            else:
                print (f"Le joueur {self.nom} n'a pas assez d'argent pour acheter le terrain {terrain.nom} , car le prix était de {terrain.prix}€, et il n'avait que {self.solde}€")
        else: 
            print(f"Le joueur {self.nom} ne veut pas acheter le terrain {terrain.nom} puis passe son tour ")
        

    def payer(self,terrain):
        """
            Le joueur paye le loyer du terrain terrain à autre_joueur

            si le terrain sur la case que l'on est a  un proprio , il faut donner en argent le prix du loyer actuel du batiment
        """
        if terrain.proprio and terrain.proprio != self:
            loyer_a_payer = terrain.get_loyer()  # Utilise la méthode get_loyer pour calculer le loyer

            # Affiche des informations sur le terrain
            statut = ""
            if terrain.nbr_hotels == 1:
                statut = "avec un hôtel"
            elif terrain.nbr_maisons > 0:
                statut = f"avec {terrain.nbr_maisons} maison(s)"
            else:
                statut = "sans construction"

            print(f"💸 {self.nom} doit payer un loyer pour {terrain.nom} {statut}")

            if self.solde < loyer_a_payer:
                terrain.proprio.solde += self.solde
                print(f"❌ {self.nom} n'a pas assez d'argent pour payer le loyer de {loyer_a_payer}€ et donne tout son argent ({self.solde}€) à {terrain.proprio.nom}")
                self.solde = -1
            else:
                self.solde -= loyer_a_payer
                terrain.proprio.solde += loyer_a_payer
                print(f"✅ {self.nom} a payé un loyer de {loyer_a_payer}€ à {terrain.proprio.nom}. Solde restant : {self.solde}€")
