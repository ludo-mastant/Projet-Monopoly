"""test Interface graphique"""

import tkinter as tk
from tkinter import messagebox
from plateau import Plateau  # Assurez-vous que le fichier plateau.py est dans le même répertoire

class MonopolyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Monopoly - Créer une Partie")
        self.root.geometry("600x600")  # Augmenter la taille pour inclure le plateau
        
        # Liste des joueurs
        self.joueurs = []
        
        # Initialisation du plateau
        self.plateau = Plateau()
        
        self.create_widgets()
    
    def create_widgets(self):
        # Titre
        title_label = tk.Label(self.root, text="Bienvenue dans Monopoly school edition!", font=("Arial", 16))
        title_label.pack(pady=20)
        
        # Nombre de joueurs
        self.num_joueurs_label = tk.Label(self.root, text="Nombre de joueurs (2 à 4) :")
        self.num_joueurs_label.pack()
        
        self.num_joueurs_var = tk.IntVar()
        self.num_joueurs_var.set(2)  # Valeur par défaut
        self.num_joueurs_spinbox = tk.Spinbox(self.root, from_=2, to=4, textvariable=self.num_joueurs_var)
        self.num_joueurs_spinbox.pack(pady=10)
        
        # Liste des joueurs
        self.players_frame = tk.Frame(self.root)
        self.players_frame.pack(pady=10)
        
        self.add_player_widgets()
        
        # Bouton pour démarrer la partie
        start_button = tk.Button(self.root, text="Démarrer la Partie", command=self.start_game)
        start_button.pack(pady=20)
    
    def add_player_widgets(self):
        """Ajoute des champs de saisie pour les joueurs"""
        for widget in self.players_frame.winfo_children():
            widget.destroy()  # On détruit les widgets existants (si on veut ajouter ou modifier)
        
        num_joueurs = self.num_joueurs_var.get()
        
        # Création des champs pour les noms des joueurs
        self.joueurs_entries = []
        for i in range(num_joueurs):
            player_label = tk.Label(self.players_frame, text=f"Nom du Joueur {i+1}:")
            player_label.grid(row=i, column=0, pady=5)
            player_entry = tk.Entry(self.players_frame)
            player_entry.grid(row=i, column=1, pady=5)
            self.joueurs_entries.append(player_entry)
    
    def start_game(self):
        """Démarre la partie et vérifie les noms des joueurs"""
        self.joueurs = []
        for entry in self.joueurs_entries:
            player_name = entry.get().strip()
            if player_name == "":
                messagebox.showerror("Erreur", "Veuillez entrer un nom pour chaque joueur.")
                return
            self.joueurs.append(player_name)

        if len(self.joueurs) < 2:
            messagebox.showerror("Erreur", "Il doit y avoir au moins 2 joueurs pour commencer la partie.")
            return

        # Lancer la partie ici (tu peux appeler une méthode du jeu pour commencer)
        self.launch_monopoly_game()

    def launch_monopoly_game(self):
        """Lance la partie de Monopoly avec les joueurs"""
        print(f"Les joueurs sont : {', '.join(self.joueurs)}")

        # Créer une nouvelle fenêtre pour le plateau de jeu
        game_window = tk.Toplevel(self.root)
        game_window.title("Plateau de Monopoly")
        game_window.geometry("800x800")

        # Afficher le plateau
        self.display_plateau(game_window)

    def display_plateau(self, window):
        """Affiche le plateau de jeu dans la fenêtre donnée"""
        plateau_frame = tk.Frame(window)
        plateau_frame.pack(expand=True, fill='both')

        # Exemple d'affichage des cases du plateau
        for i in range(10):  # Supposons que vous ayez 10 cases pour simplifier
            case_label = tk.Label(plateau_frame, text=f"Case {i+1}", borderwidth=1, relief="solid", width=20, height=3)
            case_label.grid(row=i//5, column=i%5, padx=5, pady=5)




"""def callback():
    if askyesno('Titre 1', 'Êtes-vous sûr de vouloir faire ça?'):
        showwarning('Titre 2', 'Tant pis...')
    else:
        showinfo('Titre 3', 'Vous avez peur!')
        showerror("Titre 4", "Aha")

Button(text='Action', command=callback).pack()

fenetre.mainloop()
"""

# Code principal pour lancer l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = MonopolyApp(root)
    root.mainloop()