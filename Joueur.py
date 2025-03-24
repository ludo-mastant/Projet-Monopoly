import random
from terrain import Terrain 

class Joueur:

    def __init__(self, nom, solde = 2000 , position = 0 ):
        self.nom = nom
        self.solde = solde 
        self.position = position 
        self.terter = []


    def tirer_de(self):
        tirer = random.randint(1,6)
        print (f"Le joueur {self.joueur} a tiré " , tirer , )
        #self.position += tirer
        return tirer

    def deplacement(self, nb_cases):
        
        self.position += nb_cases  #tirer

    def acheter(self, terrain):
        """
            Le joueur achete le terrain terrain
        """
        #possede = []
        achete = input(f'Voulez vous acheter le terrain {terrain.getNom()} ? (0/1)')
        if achete == 1 :
            if self.solde >= terrain.getPrix() :
                self.solde -= terrain.getPrix()
                print (f"Le joueur {self.nom} a acheté le terrain {terrain.getNom()} pour le prix de {terrain.getPrix()} € , il lui reste donc {self.solde} €")
                self.terter.append(terrain)
            else:
                print (f"Le joueur {self.nom} n'a pas assez d'argent pour acheter le terrain {terrain.getNom()} , car le prix était de {terrain.getPrix()}, et il n'avait que {self.solde} €")
        else: 
            print(f"Le joueur{self.nom} ne veut pas acheter le terrain {terrain.getNom()} puis passe son tour ")
        

    def payer(self,terrain, autre_joueur):
        """
            Le joueur paye le loyer du terrain terrain à autre_joueur

            si le terrain sur la case que l'on est a  un proprio , il faut donner en argent le prix du loyer actuel du batiment 
        """

        if self.solde < terrain.getLoyer() : # self.terter.getLoyer(Terrain)
            autre_joueur.solde += self.solde
            
            print (f"Le joueur {self.nom} n'a pas assez d'argent et donc ne peut pas payer le loyer et donc donne tout son argent a {autre_joueur}({self.solde}€)")
            self.solde = -1
        else :
            self.solde -= terrain.getLoyer()
            autre_joueur.solde += terrain.getLoyer()
            print (f"Le joueur {self.nom} a payé le loyer de {terrain.loyer} € a {self.autre_joueur}")