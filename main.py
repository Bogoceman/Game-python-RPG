from utils import *
from models import *
from game import *

#sélection de si on veut jouernt ou afficher les scores ou quitter le jeu
choix()
#introduction du jeu avec le pseudo qui est stocké dans la variable pseudo pour pouvoir l'utiliser plus tard dans le jeu
pseudo = intro()
#affichage de tous les personnages disponibles en base de données
all_characters_from_db()
#création de l'equipe de 3 personnages
team = selected_characters(characters)
#pseudo affiché avec l'équipe
statut = afficher_team(team, pseudo)

# Exemple : génération de monstres pour les vagues
monstre = generer_monstre(monsters, vague)

while True :
    systeme_de_combat(team, pseudo)
    break
#affichage du score final par palier de 1000
afficher_score()