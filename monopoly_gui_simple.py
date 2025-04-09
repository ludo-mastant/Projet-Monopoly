"""
Monopoly - Version Graphique Simplifiée
Interface graphique simple pour le jeu Monopoly utilisant Tkinter
"""

import tkinter as tk
from tkinter import messagebox, simpledialog
import random

from Partie import Monopoly
from Joueur import Joueur
from terrain import Terrain
from CaseSpeciale import CaseSpeciale

class MonopolyGUISimple:
    def __init__(self, root):
        self.root = root
        self.root.title("Monopoly - Version Simple")
        self.root.geometry("1000x600")
        
        # Variables du jeu
        self.jeu = None
        self.joueurs = []
        self.joueur_actuel_index = 0
        
        # Création de l'écran d'accueil
        self.creer_ecran_accueil()
    
    def creer_ecran_accueil(self):
        """Crée l'écran d'accueil pour configurer la partie"""
        # Suppression des widgets existants
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Frame principale
        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        # Titre
        titre_label = tk.Label(main_frame, text="MONOPOLY - VERSION SIMPLE", font=("Arial", 16, "bold"))
        titre_label.pack(pady=20)
        
        # Nombre de joueurs
        nb_joueurs_frame = tk.Frame(main_frame)
        nb_joueurs_frame.pack(pady=10)
        
        nb_joueurs_label = tk.Label(nb_joueurs_frame, text="Nombre de joueurs:", font=("Arial", 12))
        nb_joueurs_label.pack(side="left", padx=10)
        
        self.nb_joueurs_var = tk.IntVar(value=2)
        nb_joueurs_spinbox = tk.Spinbox(nb_joueurs_frame, from_=2, to=4, 
                                       textvariable=self.nb_joueurs_var, width=5, 
                                       font=("Arial", 12), command=self.actualiser_champs_joueurs)
        nb_joueurs_spinbox.pack(side="left")
        
        # Frame pour les noms des joueurs
        self.joueurs_frame = tk.Frame(main_frame)
        self.joueurs_frame.pack(pady=15, fill="x")
        
        # Initialisation des champs pour les joueurs
        self.actualiser_champs_joueurs()
        
        # Bouton pour démarrer la partie
        demarrer_btn = tk.Button(main_frame, text="Démarrer la partie", 
                                font=("Arial", 12), command=self.demarrer_partie)
        demarrer_btn.pack(pady=20)
    
    def actualiser_champs_joueurs(self):
        """Met à jour les champs de saisie des noms des joueurs"""
        # Suppression des widgets existants
        for widget in self.joueurs_frame.winfo_children():
            widget.destroy()
        
        # Création des champs pour les noms des joueurs
        self.joueurs_entries = []
        nb_joueurs = self.nb_joueurs_var.get()
        
        for i in range(nb_joueurs):
            joueur_frame = tk.Frame(self.joueurs_frame)
            joueur_frame.pack(fill="x", pady=5)
            
            joueur_label = tk.Label(joueur_frame, text=f"Joueur {i+1}:", font=("Arial", 12))
            joueur_label.pack(side="left", padx=10)
            
            joueur_entry = tk.Entry(joueur_frame, font=("Arial", 12), width=20)
            joueur_entry.insert(0, f"Joueur {i+1}")
            joueur_entry.pack(side="left", padx=10)
            
            self.joueurs_entries.append(joueur_entry)
    
    def demarrer_partie(self):
        """Démarre la partie de Monopoly"""
        # Récupération des noms des joueurs
        noms_joueurs = []
        for entry in self.joueurs_entries:
            nom = entry.get().strip()
            if not nom:
                messagebox.showerror("Erreur", "Veuillez entrer un nom pour chaque joueur.")
                return
            noms_joueurs.append(nom)
        
        # Initialisation du jeu
        self.jeu = Monopoly(noms_joueurs)
        self.joueurs = self.jeu.joueurs
        self.joueur_actuel_index = 0
        
        # Création de l'interface de jeu
        self.creer_interface_jeu()
    
    def creer_interface_jeu(self):
        """Crée l'interface principale du jeu"""
        # Suppression des widgets existants
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Frame principale avec deux colonnes
        main_frame = tk.Frame(self.root)
        main_frame.pack(expand=True, fill="both")
        
        # Colonne gauche (plateau et informations)
        gauche_frame = tk.Frame(main_frame)
        gauche_frame.pack(side="left", expand=True, fill="both", padx=10, pady=10)
        
        # Plateau simplifié (liste des cases)
        plateau_frame = tk.LabelFrame(gauche_frame, text="Plateau de jeu")
        plateau_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Création d'une liste des cases
        self.cases_listbox = tk.Listbox(plateau_frame, font=("Arial", 10), height=15)
        self.cases_listbox.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Remplissage de la liste des cases
        for i, case in enumerate(self.jeu.plateau.cases):
            proprio = ""
            if isinstance(case, Terrain) and case.proprio:
                proprio = f" (Propriétaire: {case.proprio.nom})"
            self.cases_listbox.insert(tk.END, f"{i}. {case.nom}{proprio}")
        
        # Colonne droite (informations et contrôles)
        droite_frame = tk.Frame(main_frame)
        droite_frame.pack(side="right", fill="both", padx=10, pady=10, expand=True)
        
        # Informations sur le joueur actuel
        info_frame = tk.LabelFrame(droite_frame, text="Informations du joueur")
        info_frame.pack(fill="x", padx=5, pady=5)
        
        self.joueur_actuel_label = tk.Label(info_frame, text="", font=("Arial", 12))
        self.joueur_actuel_label.pack(anchor="w", padx=10, pady=5)
        
        self.joueur_solde_label = tk.Label(info_frame, text="", font=("Arial", 12))
        self.joueur_solde_label.pack(anchor="w", padx=10, pady=5)
        
        self.joueur_position_label = tk.Label(info_frame, text="", font=("Arial", 12))
        self.joueur_position_label.pack(anchor="w", padx=10, pady=5)
        
        # Propriétés du joueur
        proprietes_frame = tk.LabelFrame(droite_frame, text="Mes propriétés")
        proprietes_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.proprietes_listbox = tk.Listbox(proprietes_frame, font=("Arial", 10))
        self.proprietes_listbox.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Contrôles
        controles_frame = tk.LabelFrame(droite_frame, text="Actions")
        controles_frame.pack(fill="x", padx=5, pady=5)
        
        self.lancer_de_btn = tk.Button(controles_frame, text="Lancer le dé", 
                                     font=("Arial", 12), command=self.lancer_de)
        self.lancer_de_btn.pack(fill="x", padx=5, pady=5)
        
        self.acheter_btn = tk.Button(controles_frame, text="Acheter la propriété", 
                                    font=("Arial", 12), command=self.acheter_propriete)
        self.acheter_btn.pack(fill="x", padx=5, pady=5)
        self.acheter_btn.config(state="disabled")
        
        self.ameliorer_btn = tk.Button(controles_frame, text="Améliorer une propriété", 
                                      font=("Arial", 12), command=self.ameliorer_propriete)
        self.ameliorer_btn.pack(fill="x", padx=5, pady=5)
        
        self.fin_tour_btn = tk.Button(controles_frame, text="Fin du tour", 
                                     font=("Arial", 12), command=self.fin_tour)
        self.fin_tour_btn.pack(fill="x", padx=5, pady=5)
        self.fin_tour_btn.config(state="disabled")
        
        # Historique
        historique_frame = tk.LabelFrame(droite_frame, text="Historique")
        historique_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.historique_text = tk.Text(historique_frame, height=8, width=30, font=("Arial", 10))
        self.historique_text.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Mise à jour de l'interface
        self.mettre_a_jour_interface()
    
    def mettre_a_jour_interface(self):
        """Met à jour l'interface avec les informations actuelles"""
        joueur_actuel = self.joueurs[self.joueur_actuel_index]
        
        # Mise à jour des informations du joueur
        self.joueur_actuel_label.config(text=f"Tour de: {joueur_actuel.nom}")
        self.joueur_solde_label.config(text=f"Solde: {joueur_actuel.solde}€")
        
        case_actuelle = self.jeu.plateau.cases[joueur_actuel.position % len(self.jeu.plateau.cases)]
        self.joueur_position_label.config(text=f"Position: {joueur_actuel.position} - {case_actuelle.nom}")
        
        # Mise en évidence de la position du joueur dans la liste des cases
        self.cases_listbox.selection_clear(0, tk.END)
        self.cases_listbox.selection_set(joueur_actuel.position % len(self.jeu.plateau.cases))
        self.cases_listbox.see(joueur_actuel.position % len(self.jeu.plateau.cases))
        
        # Mise à jour des propriétés
        self.proprietes_listbox.delete(0, tk.END)
        
        if not joueur_actuel.terter:
            self.proprietes_listbox.insert(tk.END, "Aucune propriété")
        else:
            for terrain in joueur_actuel.terter:
                if terrain.nbr_hotels == 1:
                    statut = "avec hôtel"
                elif terrain.nbr_maisons > 0:
                    statut = f"avec {terrain.nbr_maisons} maison(s)"
                else:
                    statut = "sans construction"
                
                self.proprietes_listbox.insert(tk.END, f"{terrain.nom} ({terrain.salle}) - {statut}")
        
        # Activation/désactivation des boutons
        self.lancer_de_btn.config(state="normal")
        self.fin_tour_btn.config(state="disabled")
        
        # Vérification si le joueur peut acheter la propriété actuelle
        if (isinstance(case_actuelle, Terrain) and case_actuelle.est_achetable() and 
            joueur_actuel.solde >= case_actuelle.prix):
            self.acheter_btn.config(state="normal")
        else:
            self.acheter_btn.config(state="disabled")
        
        # Vérification si le joueur a des propriétés à améliorer
        if joueur_actuel.terter:
            self.ameliorer_btn.config(state="normal")
        else:
            self.ameliorer_btn.config(state="disabled")
        
        # Mise à jour de la liste des cases (pour les propriétaires)
        self.cases_listbox.delete(0, tk.END)
        for i, case in enumerate(self.jeu.plateau.cases):
            proprio = ""
            if isinstance(case, Terrain) and case.proprio:
                proprio = f" (Propriétaire: {case.proprio.nom})"
            
            # Marquer la position du joueur actuel
            if i == joueur_actuel.position % len(self.jeu.plateau.cases):
                self.cases_listbox.insert(tk.END, f">>> {i}. {case.nom}{proprio} <<<")
            else:
                self.cases_listbox.insert(tk.END, f"{i}. {case.nom}{proprio}")
    
    def lancer_de(self):
        """Gère le lancer de dé et le déplacement du joueur"""
        joueur_actuel = self.joueurs[self.joueur_actuel_index]
        
        # Lancer le dé
        lancer = joueur_actuel.tirer_de()
        
        # Afficher le résultat
        self.ajouter_historique(f"{joueur_actuel.nom} lance le dé: {lancer}")
        
        # Ancienne position pour l'animation
        ancienne_position = joueur_actuel.position
        
        # Déplacement du joueur
        self.jeu.deplacement(joueur_actuel, lancer)
        
        # Traitement post-déplacement
        self.traitement_post_deplacement(joueur_actuel)
        
        # Mise à jour de l'interface
        self.mettre_a_jour_interface()
        
        # Désactiver le bouton de lancer et activer le bouton de fin de tour
        self.lancer_de_btn.config(state="disabled")
        self.fin_tour_btn.config(state="normal")
    
    def traitement_post_deplacement(self, joueur):
        """Gère les actions après le déplacement du joueur"""
        case_actuelle = self.jeu.plateau.cases[joueur.position % len(self.jeu.plateau.cases)]
        
        # Vérification du type de case
        if isinstance(case_actuelle, Terrain):
            if case_actuelle.est_achetable():
                # Le terrain est disponible à l'achat
                self.ajouter_historique(f"Le terrain {case_actuelle.nom} est disponible à l'achat pour {case_actuelle.prix}€")
                self.acheter_btn.config(state="normal" if joueur.solde >= case_actuelle.prix else "disabled")
            elif case_actuelle.proprio and case_actuelle.proprio != joueur:
                # Le joueur doit payer un loyer
                loyer = case_actuelle.get_loyer()
                self.ajouter_historique(f"{joueur.nom} doit payer un loyer de {loyer}€ à {case_actuelle.proprio.nom}")
                
                # Paiement automatique
                if joueur.solde < loyer:
                    case_actuelle.proprio.solde += joueur.solde
                    self.ajouter_historique(f"{joueur.nom} n'a pas assez d'argent et donne tout son solde ({joueur.solde}€)")
                    joueur.solde = -1
                else:
                    joueur.solde -= loyer
                    case_actuelle.proprio.solde += loyer
                    self.ajouter_historique(f"{joueur.nom} a payé {loyer}€ à {case_actuelle.proprio.nom}")
                
                # Mise à jour de l'interface
                self.mettre_a_jour_interface()
        
        elif isinstance(case_actuelle, CaseSpeciale):
            if case_actuelle.type_case == "chance":
                # Tirage d'une carte chance
                self.tirer_carte_chance(joueur)
            elif case_actuelle.type_case == "en_prison":
                # Le joueur va en prison
                self.ajouter_historique(f"{joueur.nom} va en prison!")
                case_actuelle.aller_prison(joueur)
                self.mettre_a_jour_interface()
            elif case_actuelle.type_case == "visite" and joueur.en_prison:
                # Le joueur est en prison
                self.gerer_prison(joueur)
            elif case_actuelle.type_case == "évenement" and case_actuelle.nom == "Réunion Parent-Prof":
                # Réunion parent-prof
                montant = 75
                if joueur.solde < montant:
                    self.ajouter_historique(f"{joueur.nom} n'a pas assez d'argent pour la réunion parent-prof")
                    joueur.solde = -1
                else:
                    joueur.solde -= montant
                    self.ajouter_historique(f"{joueur.nom} perd {montant}€ pour la réunion parent-prof")
    
    def tirer_carte_chance(self, joueur):
        """Gère le tirage d'une carte chance"""
        case_actuelle = self.jeu.plateau.cases[joueur.position % len(self.jeu.plateau.cases)]

        if isinstance(case_actuelle, CaseSpeciale) and case_actuelle.type_case == "chance":
            # Tirage aléatoire d'une carte
            taille = len(case_actuelle.tabCartes)
            carte_index = random.randint(0, taille - 1)
            carte = case_actuelle.tabCartes[carte_index]

            # Affichage de la carte
            messagebox.showinfo("Carte Chance", f"{carte.nom}\n\n{carte.texte}")

            # Application de l'effet
            self.ajouter_historique(f"Carte chance: {carte.nom}")

            # Appliquer l'effet de la carte
            if carte.nom == "Bonne Note":
                joueur.solde += 100
                self.ajouter_historique(f"{joueur.nom} gagne 100€")
            elif carte.nom == "Réussite scolaire":
                joueur.solde += 200
                self.ajouter_historique(f"{joueur.nom} gagne 200€")
            elif carte.nom == "Journée banalisée":
                joueur.peut_rejouer = True
                self.ajouter_historique(f"{joueur.nom} pourra rejouer après ce tour")
            elif carte.nom == "Copie double":
                joueur.solde += 50
                self.ajouter_historique(f"{joueur.nom} gagne 50€")
            elif carte.nom == "Bureau du proviseur":
                joueur.solde -= 100
                self.ajouter_historique(f"{joueur.nom} perd 100€")
            elif carte.nom == "Salle de Notes":
                joueur.solde -= 150
                self.ajouter_historique(f"{joueur.nom} perd 150€")
            elif carte.nom == "Heure de colle":
                joueur.tours_a_attendre = 1
                self.ajouter_historique(f"{joueur.nom} passe un tour")
            elif carte.nom == "Devoir Surveillé":
                joueur.tours_a_attendre = 2
                self.ajouter_historique(f"{joueur.nom} passe deux tours")
            elif carte.nom == "Contrôle surprise":
                hasard = random.randint(1, 6)
                if hasard <= 3:
                    joueur.solde -= 75
                    self.ajouter_historique(f"{joueur.nom} perd 75€")
                else:
                    self.ajouter_historique(f"{joueur.nom} s'en sort sans encombre")

            # Mise à jour de l'interface
            self.mettre_a_jour_interface()
    
    def gerer_prison(self, joueur):
        """Gère le cas où un joueur est en prison"""
        if joueur.en_prison:
            self.ajouter_historique(f"{joueur.nom} est en prison")
            
            # Compter le nombre de tours en prison
            if not hasattr(joueur, 'tours_en_prison'):
                joueur.tours_en_prison = 1
            else:
                joueur.tours_en_prison += 1
            
            # Après 3 tours, le joueur est libéré automatiquement
            if joueur.tours_en_prison >= 3:
                self.ajouter_historique(f"{joueur.nom} est libéré après 3 tours en prison")
                joueur.en_prison = False
                joueur.tours_en_prison = 0
                return
            
            # Options pour sortir de prison
            choix = messagebox.askyesno("Prison", 
                                       f"{joueur.nom} est en prison.\n\nVoulez-vous payer 50€ pour sortir?\n(Non = lancer le dé)")
            
            if choix and joueur.solde >= 50:
                # Payer pour sortir
                joueur.solde -= 50
                self.ajouter_historique(f"{joueur.nom} paie 50€ et sort de prison")
                joueur.en_prison = False
                joueur.tours_en_prison = 0
            else:
                # Lancer le dé
                lancer = random.randint(1, 6)
                self.ajouter_historique(f"{joueur.nom} lance un {lancer} pour sortir de prison")
                
                if lancer == 6:
                    self.ajouter_historique(f"{joueur.nom} sort de prison!")
                    joueur.en_prison = False
                    joueur.tours_en_prison = 0
                else:
                    self.ajouter_historique(f"{joueur.nom} reste en prison")
    
    def acheter_propriete(self):
        """Gère l'achat d'une propriété"""
        joueur_actuel = self.joueurs[self.joueur_actuel_index]
        case_actuelle = self.jeu.plateau.cases[joueur_actuel.position % len(self.jeu.plateau.cases)]
        
        if isinstance(case_actuelle, Terrain) and case_actuelle.est_achetable():
            # Confirmation d'achat
            reponse = messagebox.askyesno("Achat de propriété", 
                                         f"Voulez-vous acheter {case_actuelle.nom} pour {case_actuelle.prix}€?")
            
            if reponse:
                # Achat de la propriété
                if joueur_actuel.solde >= case_actuelle.prix:
                    joueur_actuel.solde -= case_actuelle.prix
                    joueur_actuel.terter.append(case_actuelle)
                    case_actuelle.proprio = joueur_actuel
                    
                    self.ajouter_historique(f"{joueur_actuel.nom} achète {case_actuelle.nom} pour {case_actuelle.prix}€")
                    self.acheter_btn.config(state="disabled")
                    
                    # Mise à jour de l'interface
                    self.mettre_a_jour_interface()
                else:
                    messagebox.showerror("Erreur", "Vous n'avez pas assez d'argent!")
    
    def ameliorer_propriete(self):
        """Gère l'amélioration d'une propriété"""
        joueur_actuel = self.joueurs[self.joueur_actuel_index]
        
        if not joueur_actuel.terter:
            messagebox.showinfo("Information", "Vous ne possédez aucune propriété à améliorer.")
            return
        
        # Création d'une liste des propriétés à améliorer
        proprietes = []
        for terrain in joueur_actuel.terter:
            if terrain.nbr_hotels == 1:
                statut = "Hôtel (max atteint)"
                peut_ameliorer = False
            elif terrain.nbr_maisons == 4:
                statut = f"4 maisons - Hôtel: {terrain.cout_hotel}€"
                peut_ameliorer = joueur_actuel.solde >= terrain.cout_hotel
            else:
                statut = f"{terrain.nbr_maisons} maisons - Maison: {terrain.cout_maison}€"
                peut_ameliorer = joueur_actuel.solde >= terrain.cout_maison
            
            if peut_ameliorer:
                proprietes.append((terrain, statut))
        
        if not proprietes:
            messagebox.showinfo("Information", "Vous n'avez pas assez d'argent pour améliorer vos propriétés.")
            return
        
        # Création d'une liste pour l'utilisateur
        options = [f"{terrain.nom} - {statut}" for terrain, statut in proprietes]
        
        # Demande à l'utilisateur de choisir une propriété
        choix = simpledialog.askstring("Améliorer une propriété", 
                                      "Choisissez une propriété à améliorer (numéro):\n\n" + 
                                      "\n".join([f"{i+1}. {opt}" for i, opt in enumerate(options)]))
        
        if choix and choix.isdigit():
            index = int(choix) - 1
            if 0 <= index < len(proprietes):
                terrain, _ = proprietes[index]
                
                # Amélioration du terrain
                terrain.ameliorer_terrain(joueur_actuel)
                
                self.ajouter_historique(f"{joueur_actuel.nom} améliore {terrain.nom}")
                
                # Mise à jour de l'interface
                self.mettre_a_jour_interface()
            else:
                messagebox.showerror("Erreur", "Numéro invalide.")
    
    def fin_tour(self):
        """Termine le tour du joueur actuel et passe au joueur suivant"""
        joueur_actuel = self.joueurs[self.joueur_actuel_index]

        # Vérification de la faillite
        if joueur_actuel.solde < 0:
            self.ajouter_historique(f"{joueur_actuel.nom} est en faillite et quitte la partie")

            # Vérifier s'il reste plus d'un joueur
            joueurs_actifs = [j for j in self.joueurs if j.solde >= 0]
            if len(joueurs_actifs) <= 1:
                self.fin_partie()
                return

        # Vérifier si le joueur a le droit de rejouer
        if joueur_actuel.peut_rejouer:
            self.ajouter_historique(f"{joueur_actuel.nom} a le droit de rejouer!")
            joueur_actuel.peut_rejouer = False  # Réinitialiser pour le prochain tour
        else:
            # Passage au joueur suivant
            self.joueur_actuel_index = (self.joueur_actuel_index + 1) % len(self.joueurs)

        # Vérification si le joueur suivant doit attendre des tours
        joueur_suivant = self.joueurs[self.joueur_actuel_index]

        while joueur_suivant.solde < 0 or joueur_suivant.tours_a_attendre > 0:
            if joueur_suivant.solde < 0:
                # Le joueur est en faillite, on passe au suivant
                self.joueur_actuel_index = (self.joueur_actuel_index + 1) % len(self.joueurs)
                joueur_suivant = self.joueurs[self.joueur_actuel_index]
            elif joueur_suivant.tours_a_attendre > 0:
                # Le joueur doit attendre des tours
                self.ajouter_historique(f"{joueur_suivant.nom} doit attendre encore {joueur_suivant.tours_a_attendre} tour(s)")
                joueur_suivant.tours_a_attendre -= 1
                self.joueur_actuel_index = (self.joueur_actuel_index + 1) % len(self.joueurs)
                joueur_suivant = self.joueurs[self.joueur_actuel_index]

        # Mise à jour de l'interface
        self.mettre_a_jour_interface()
    
    def fin_partie(self):
        """Gère la fin de la partie"""
        # Détermination du gagnant
        joueurs_actifs = [j for j in self.joueurs if j.solde >= 0]
        
        if joueurs_actifs:
            gagnant = max(joueurs_actifs, key=lambda j: j.solde)
            
            # Affichage du gagnant
            messagebox.showinfo("Fin de la partie", 
                               f"{gagnant.nom} remporte la partie avec {gagnant.solde}€!")
            
            # Demande pour recommencer
            if messagebox.askyesno("Nouvelle partie", "Voulez-vous commencer une nouvelle partie?"):
                self.creer_ecran_accueil()
            else:
                self.root.quit()
    
    def ajouter_historique(self, message):
        """Ajoute un message à l'historique"""
        self.historique_text.insert(tk.END, f"{message}\n")
        self.historique_text.see(tk.END)
        
        # Mise à jour de l'interface
        self.root.update()

# Lancement de l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = MonopolyGUISimple(root)
    root.mainloop()