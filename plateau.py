from Case import Case
class Plateau :
    def __init__(self):
        # Initialisation des cases du plateau, par exemple :
        self.cases = [
            Case("nomcase"),
            Case(""),
            Case(""),
            Case(""),
            Case(""),
            Case(""),
        ]

    def avoir_terrain(self, i):
        """
        Donne le i-ème terrain du plateau.
        """
        if 0 <= i < len(self.cases):
            return self.cases[i]
        else:
            return "Terrain inexistant"