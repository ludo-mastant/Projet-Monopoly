import random
from Terrain import Terrain 

class Joueur:

    def __init__(self, nom, solde = 2000 , position = 0 , terrain):
        self.nom = nom
        self.solde = solde 
        self.position = position 
        self.terter = terrain


    def tirer_de(self):
        tirer = random.randint(1,6)
        print (f"Le joueur {self.joueur} a tiré ")

    def deplacement(self, nb_cases):
        
        self.position += nb_cases

    def acheter(self, terrain):
        """
            Le joueur achete le terrain terrain
        """
        achete = input(f'Voulez vous acheter le terrain {self.terter.getNom()} ? (0/1)')
        if achete == 1 :
            if self.solde >= self.terter.getPrix() :
                self.solde -= self.terter.getPrix()
                print (f"Le joueur {self.nom} a acheté le terrain {self.terter.getNom()} pour le prix de {self.terter.getPrix()} € , il lui reste donc {self.solde} €")
            else:
                print (f"Le joueur {self.nom} n'a pas assez d'argent pour acheter le terrain {self.terter.getNom()} , car le prix était de {self.terter.getPrix()}, et il n'avait que {self.solde} €")
        else: 
            print(f"Le joueur{self.nom} ne veut pas acheter le terrain {self.terter.getNom()} puis passe son tour ")
        

    def payer(self, terrain, autre_joueur):
        """
            Le joueur paye le loyer du terrain terrain à autre_joueur
        """