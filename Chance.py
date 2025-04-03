import random
import time

class Chance:
    def __init__(self, nom):
        self.nom=nom
        self.deplacement = 0
        if self.nom == "Récréation":
            deplacement = random.randint(1, 6)
            self.deplacement = deplacement
            self.texte = f"📖 Récréation ! Vous avancez de {deplacement} cases."
        elif self.nom == "Journée banalisée":
            self.texte =  "🎉 Journée banalisée ! Vous pouvez rejouer immédiatement."
        elif self.nom == "Bonne Note":
            self.texte = "💯 Bonne Note ! Vous gagnez 100€."
        elif self.nom == "Réussite scolaire":
            self.texte = "🎓 Réussite scolaire ! Vous gagnez 200€."
        elif self.nom == "Heure libre":
            deplacement = 2
            self.deplacement = deplacement
            self.texte = "📢 Heure libre ! Vous avancez de 2 cases."
        elif self.nom == "Copie double":
            self.texte = "✍️ Copie double ! Vous recevez une bourse de 50€ "
        elif self.nom == "Cours ennuyeux":
            self.texte = "⏳ Cours ennuyeux... Le joueur verra son prochain lancé divisé par 2."
        elif self.nom == "Heure de colle":
            self.texte = "🚫 Heure de colle ! Le joueur passe un tour."
        elif self.nom == "Bureau du proviseur":
            self.texte = "🏛️ Bureau du proviseur ! Le joueur paye une amende de 100€."
        elif self.nom == "Haleine du prof":
            deplacement = random.randint(1,6)
            self.deplacement = -deplacement  
            self.texte = f"💨 Haleine du prof ! Le joueur recule de {deplacement} cases."
        elif self.nom == "Devoir Surveillé":
            self.texte = "📝 Devoir Surveillé ! Le joueur est bloqué pendant 2 tours."
        elif self.nom == "Salle de Notes":
            self.texte = "💸 Sale Note ! Ton père est furax il casse ton téléphone. Le joueur perd 150€."
        elif self.nom == "Contrôle surprise":
            hasard = random.randint(1, 6)
            self.hasard = hasard
            self.texte = "Contrôle surprise ! Tu connaissais le cours ou pas ?"
        
        
        
    def appliquer_effet(self, joueur, partie):
        print(self.texte)
        if self.nom == "Récréation":
            partie.tour(joueur, self.deplacement)
        
        elif self.nom == "Journée banalisée":
            joueur.peut_rejouer = True

        elif self.nom == "Bonne Note":
            joueur.solde += 100

        elif self.nom == "Réussite scolaire":
            joueur.solde += 200

        elif self.nom == "Heure libre":
            partie.tour(joueur, self.deplacement)

        elif self.nom == "Copie double":
            joueur.solde += 50

        # Cas Malus
        elif self.nom == "Cours ennuyeux":
            joueur.lance_divise_par_2 = True

        elif self.nom == "Heure de colle":
            joueur.tours_a_attendre = 1 # A CHANGERRRRRRR !!!!!

        elif self.nom == "Bureau du proviseur":
            joueur.solde -= 100

        elif self.nom == "Haleine du prof":
            partie.deplacement(joueur, self.deplacement)

        elif self.nom == "Devoir Surveillé":
            joueur.tours_a_attendre = 2  # A CHANGERRRRRRRRRRRRRRRRRRRRRR

        elif self.nom == "Salle de Notes":
            joueur.solde -= 150

        elif self.nom == "Contrôle surprise":
            if self.hasard <= 3:
                joueur.solde -= 75
                print(f"🔄 {joueur.nom} n'a pas révisé et perd 75€ . Il a maintenant {joueur.solde}€")
            else:
                print(f"🔄  {joueur.nom} s'en sort sans encombre , il avait révisé en cachette !.")
