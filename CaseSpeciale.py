import random


class CaseSpeciale:
    def __init__(self, nom, type_case):
        self.nom = nom
        self.type_case = type_case  # Peut être "bonus" ou "malus"

    def appliquer_effet(self, joueur):
        if self.nom == "Récréation":
            deplacement = random.randint(1, 6)
            print(f"📖 Récréation ! {joueur.nom} avance de {deplacement} cases.")
            joueur.position += deplacement
        
        elif self.nom == "Journée banalisée":
            print(f"🎉 Journée banalisée ! {joueur.nom} peut rejouer immédiatement.")
            joueur.peut_rejouer = True

        elif self.nom == "Bonne Note":
            print(f"💯 Bonne Note ! {joueur.nom} gagne 100€.")
            joueur.solde += 100

        elif self.nom == "Réussite scolaire":
            print(f"🎓 Réussite scolaire ! {joueur.nom} gagne 200€.")
            joueur.solde += 200

        elif self.nom == "Heure libre":
            print(f"📢 Heure libre ! {joueur.nom} avance de 2 cases.")
            joueur.position += 2

        elif self.nom == "Copie double":
            print(f"✍️ Copie double ! {joueur.nom} reçoit une bourse de 50€.")
            joueur.solde += 50

        # Cas Malus
        elif self.nom == "Cours ennuyeux":
            print(f"⏳ Cours ennuyeux... {joueur.nom} verra son prochain lancé divisé par 2.")
            joueur.lance_divise_par_2 = True

        elif self.nom == "Heure de colle":
            print(f"🚫 Heure de colle ! {joueur.nom} passe un tour.")
            joueur.tours_a_attendre = 1

        elif self.nom == "Bureau du proviseur":
            print(f"🏛️ Bureau du proviseur ! {joueur.nom} paye une amende de 100€.")
            joueur.solde -= 100

        elif self.nom == "Haleine du prof":
            recul = random.randint(1, 6)
            print(f"💨 Haleine du prof ! {joueur.nom} recule de {recul} cases.")
            joueur.position -= recul

        elif self.nom == "Devoir Surveillé":
            print(f"📝 Devoir Surveillé ! {joueur.nom} est bloqué pendant 2 tours.")
            joueur.tours_a_attendre = 2

        elif self.nom == "Salle de Notes":
            print(f"💸 Salle de Notes ! {joueur.nom} perd 150€.")
            joueur.solde -= 150

        elif self.nom == "Contrôle surprise":
            if random.randint(1, 6) <= 3:
                print(f"🔄 Contrôle surprise ! {joueur.nom} n'a pas révisé et perd 75€.")
                joueur.solde -= 75
            else:
                print(f"🔄 Contrôle surprise ! {joueur.nom} s'en sort sans encombre.")




# Création des objets CaseSpeciale (tout est de type "chance")
recreation = CaseSpeciale("Récréation", "chance")
journee_banalisee = CaseSpeciale("Journée banalisée", "chance")
bonne_note = CaseSpeciale("Bonne Note", "chance")
reussite_scolaire = CaseSpeciale("Réussite scolaire", "chance")
heure_libre = CaseSpeciale("Heure libre", "chance")
copie_double = CaseSpeciale("Copie double", "chance")

cours_ennuyeux = CaseSpeciale("Cours ennuyeux", "chance")
heure_de_colle = CaseSpeciale("Heure de colle", "chance")
bureau_du_proviseur = CaseSpeciale("Bureau du proviseur", "chance")
haleine_du_prof = CaseSpeciale("Haleine du prof", "chance")
devoir_surveille = CaseSpeciale("Devoir Surveillé", "chance")
salle_de_notes = CaseSpeciale("Salle de Notes", "chance")
controle_surprise = CaseSpeciale("Contrôle surprise", "chance")

# Liste de toutes les cases spéciales
cases_speciales = [
    recreation, journee_banalisee, bonne_note, reussite_scolaire,
    heure_libre, copie_double, cours_ennuyeux, heure_de_colle, bureau_du_proviseur,
    haleine_du_prof, devoir_surveille, salle_de_notes, controle_surprise
]

"""
# Test affichage des cases spéciales
for case in cases_speciales:
    print(f"Case : {case.nom}, Type : {case.type_case}")
"""