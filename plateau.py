from terrain import Terrain


class Plateau :
    def __init__(self):
        # Initialisation des cases du plateau, par exemple :
        self.cases = [
            Case("départ"),
            Terrain("Happy gap-teeth city"),
            Terrain("Sunny head beach"),
            Terrain("Tagad island"),
            Terrain("Overthinking path"),
            Terrain("Hairy Bird Nest"),
            Terrain("The Youth District"),
            Terrain("Reptilian Way"),
            Terrain("Improvisation's City"),
            Terrain("The Useless Street"),
            Terrain("Perinity City"),
            Terrain("Juventus Cartel"),
            Terrain("Crazy Motel"),
            Terrain("Leaving City"),
            Terrain("The Musical Shopping-Center"),
            Terrain("The Market Bistro"),
            Terrain("The..hmmm...MeteoTower"),
            Terrain("The Autstic Boulevard"),
        ]

    def avoir_terrain(self, i):
        """
        Donne le i-ème terrain du plateau.
        """
        if 0 <= i < len(self.cases):
            return self.cases[i]
        else:
            return "Terrain inexistant"