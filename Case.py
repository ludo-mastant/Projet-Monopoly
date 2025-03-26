class Case:
    def __init__(self, nom):
        """
        Initialise une case avec un nom.
        :param nom: Le nom de la case.
        """
        self.nom = nom

    def __str__(self):
        return self.nom
