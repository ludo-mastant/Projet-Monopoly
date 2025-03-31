from terrain import Terrain
from CaseSpeciale import CaseSpeciale

class Plateau :
    def __init__(self):
        # Initialisation des cases du plateau, par exemple :
        self.cases = [
            CaseSpeciale("Départ","départ"), 
            Terrain("Sunny head beach","T11"),
            Terrain("The Autistic Boulevard","T11"),
            Terrain("Overthinking path","T11"),
            Terrain("Hairy Bird Nest","T24 BIS"),
            CaseSpeciale("Chance","chance"),  
            Terrain("Reptilian Way","T22"),
            Terrain("Perinity City","T22"), 
            Terrain("The Market Bistro","T22"),
            CaseSpeciale("Prison","visite"),
            Terrain("The..hmmm...MeteoTower","T21"),
            Terrain("Tagad island","T21"),                                                      #Tableau Enfin rangé dans l'ordre 
            Terrain("The Musical Shopping-Center","A104"),
            Terrain("Improvisation's City","A104"),
            CaseSpeciale("Chance","chance"),
            Terrain("The Useless Street","T10"),
            Terrain("Juventus Cartel","T10"),
            Terrain("Crazy City","T10"),
            CaseSpeciale("Réunion Parent-Prof","évenement"),
            Terrain("The Youth District","T24"),        
            Terrain("Sleepover'z Motel","T24"),
            CaseSpeciale("En Prison","prison"),            
            Terrain("Happy gap-teeth city","T24")
        ]

    def avoir_terrain(self, i):
        """
        Donne le i-ème terrain du plateau.
        """
        if 0 <= i < len(self.cases):
            return self.cases[i]
        else:
            return "Terrain inexistant"