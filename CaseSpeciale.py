import random
from Case import Case
import time 

class CaseSpeciale(Case):
    def __init__(self, nom, type_case):
        super().__init__(nom)
        self.type_case = type_case  # Peut être "bonus" ou "malus"

    def appliquer_effet(self, joueur):
        if self.type_case == "chance" :
            if self.nom == "Récréation":
                deplacement = random.randint(1, 6)
                print(f"📖 Récréation ! {joueur.nom} avance de {deplacement} cases.")
                joueur.position += deplacement
            
            elif self.nom == "Journée banalisée":
                print(f"🎉 Journée banalisée ! {joueur.nom} peut rejouer immédiatement.")
                joueur.peut_rejouer = True

            elif self.nom == "Bonne Note":
                joueur.solde += 100
                print(f"💯 Bonne Note ! {joueur.nom} gagne 100€. Il a maintenant {joueur.solde} €")

            elif self.nom == "Réussite scolaire":
                print(f"🎓 Réussite scolaire ! {joueur.nom} gagne 200€.")
                joueur.solde += 200

            elif self.nom == "Heure libre":
                print(f"📢 Heure libre ! {joueur.nom} avance de 2 cases.")
                joueur.position += 2

            elif self.nom == "Copie double":
                joueur.solde += 50
                print(f"✍️ Copie double ! {joueur.nom} reçoit une bourse de 50€. Il a maintenant {joueur.solde}€")

            # Cas Malus
            elif self.nom == "Cours ennuyeux":
                print(f"⏳ Cours ennuyeux... {joueur.nom} verra son prochain lancé divisé par 2.")
                joueur.lance_divise_par_2 = True

            elif self.nom == "Heure de colle":
                print(f"🚫 Heure de colle ! {joueur.nom} passe un tour.")
                joueur.tours_a_attendre = 1

            elif self.nom == "Bureau du proviseur":
                joueur.solde -= 100
                print(f"🏛️ Bureau du proviseur ! {joueur.nom} paye une amende de 100€.Il a maintenant {joueur.solde}€")

            elif self.nom == "Haleine du prof":
                recul = random.randint(1, 6)
                print(f"💨 Haleine du prof ! {joueur.nom} recule de {recul} cases.")
                joueur.position -= recul

            elif self.nom == "Devoir Surveillé":
                print(f"📝 Devoir Surveillé ! {joueur.nom} est bloqué pendant 2 tours.")
                joueur.tours_a_attendre = 2

            elif self.nom == "Salle de Notes":
                print(f"💸 Sale Note ! Ton père est furax il casse ton téléphone. {joueur.nom} perd 150€. Il a maintenant {joueur.solde}€")
                joueur.solde -= 150

            elif self.nom == "Contrôle surprise":
                print ("Contrôle surprise ! Tu connaissais le cours ou pas ?")
                time.sleep(3)
                if random.randint(1, 6) <= 3:
                    joueur.solde -= 75
                    print(f"🔄 {joueur.nom} n'a pas révisé et perd 75€ . Il a maintenant {joueur.solde}€")
                else:
                    print(f"🔄  {joueur.nom} s'en sort sans encombre , il avait révisé en cachette !.")
        elif self.type_case == "départ" :
            joueur.solde += 200
            print(f"🏁 {joueur.nom} a fini un tour et gagne 200 € . Il a maintenant {joueur.solde}€")
        elif self.type_case == "évenement" :
            joueur.solde -= 50 
            print (f"👩‍🏫  {joueur.nom} doit payer 50€ pour impressionner les profs et éviter des remarques négatives. Il a maintenant {joueur.solde}€")


        
"""
    def nb_tour (self,joueur) :
        nb_tour = 0 
        if joueur.position == 0 :
            joueur.solde += 200
            nb_tour +=1 
"""




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