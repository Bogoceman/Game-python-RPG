import time 
import sys
from pymongo import MongoClient
import random

def isValid(team):
    if len(team) >= 3:
        return False
    return True

def choix():
    while True:
        print("Que voulez vous faire ")
        print("1. Démarrer le jeu")
        print("2. afficher le tableau des scores")
        print("3. quitter le jeu")
        #on demande le choix de l'utilisateur et on vérifie que c'est un choix valide
        choix = int(input("Entrez votre choix (1, 2 ou 3) : "))
        #si le choix est 1 le jeu commence
        if choix == 1:
            print("Démarrage du jeu...")
            time.sleep(1)
            break
        #si le choix est 2 on affiche le tableau des scores
        elif choix == 2:
            print("Affichage du tableau des scores...")
            time.sleep(1)
            break
        #si le choix est 3 on quitte le jeu 
        elif choix == 3:
            print("REVIENS JOUER !!!!")
            sys.exit()
            exit()

def demander_pseudo():
    #le pseudo est demandé, on demande que se soit une chaine de caractère et pas un nombre ou autre
    pseudo = str(input("Entrez votre pseudo : "))
    return pseudo

def intro():
    pseudo = demander_pseudo()   
    input(f"Bienvenue {pseudo} dans le donjon infini.(Appuyez sur Entrée pour continuer)")
    input("Le donjon de l'infini est un piège où il n'y a pas de sortie et pas de fin.")
    input("Vous allez devoir combattre vaillamment les monstres qui se dresseront sur votre chemin avec votre équipe.")
    input("Qui sont les 3 membres de votre équipe déjà ?")
    return pseudo



#ici on affiche tous les personnages dispos et on les affiches de maniere lisible pour le joueur
def all_characters_from_db(
    uri="mongodb://localhost:27017/",
    db_name="rpg_game",
    collection_name="characters",):

    client = MongoClient(uri)
    try:
        collection = client[db_name][collection_name]
        print("Voici les personnages en base :")
        print("==================================================")
        for doc in collection.find(
            {}, {"_id": 0, "name": 1, "ATK": 1, "DEF": 1, "PV": 1}
        ).sort("name", 1):
            name = doc.get("name", "(sans nom)")
            atk = doc.get("ATK", "?")
            den = doc.get("DEF", "?")
            pv = doc.get("PV", "?")
            print(f"{name} - ATK: {atk}, DEF: {den}, PV: {pv}")
            print("--------------------------------------------------")
        print("==================================================")
    finally:
        client.close()

#cette fonction permet de sélectionner les personnages que le joueur veut dans son équipe et vérifie que les choix sont valides
def selected_characters(characters):
    team = []
    while isValid(team):
        choice = input("Entrez le nom du personnage que vous souhaitez sélectionner : ").strip()
        if choice in characters:
            if any(member["name"] == choice for member in team):
                print("Personnage déjà sélectionné. Choisis-en un autre.")
                continue
            stats = characters[choice]
            team.append({"name": choice, **stats})
            print(f"Vous avez sélectionné {choice} !")
        else:
            print("Personnage non trouvé. Veuillez réessayer.")
    print("Vous avez donc choisi :")
    for member in team:
        print(f"{member['name']} - ATK: {member['ATK']}, DEF: {member['DEF']}, PV: {member['PV']}")
    return team

def afficher_team(team, pseudo):
    print(f"\n============= ÉQUIPE DE {pseudo} =============")
    #le status servira a dire lorsqu'on aura perdu
    for member in team:
        pv = member['PV']
        statut = "💀 Mort" if pv <= 0 else f"❤️  {pv} PV"
        print(f"{member['name']: <12} | ATK: {member['ATK']: >2} | DEF: {member['DEF']: >2} | {statut}")
    print("===============================================\n")


def generer_monstre(monsters, vague=1):

    monstres_vague = []
    monster_names = list(monsters.keys())
    
    # Sélection aléatoire
    nom = random.choice(monster_names)
    stats = monsters[nom].copy()
        
    # Buff progressif selon la vague (+5% par vague)
    boost = 1 + (vague * 0.05)
        
    monstre = {
       "name": nom,
        "ATK": int(stats["ATK"] * boost),
        "DEF": int(stats["DEF"] * boost),
        "PV": int(stats["PV"] * boost)
    }
    return monstre

#buff de la team a chaques débuts de vagues après la première
"""def buff_team(team, vague):
    if vague >= 2 :
        for member in team :"""





def afficher_monstre(monstres, vague):
    """Affiche le monstre de la vague."""
    print(f"\n============= VAGUE {vague + 2} =============")
    for i, monstre in enumerate(monstres, 1):
        print(f"{i}. {monstre['name']} - ATK: {monstre['ATK']}, DEF: {monstre['DEF']},❤️  PV: {monstre['PV']}")
    print("="*40 + "\n")


def verifier_game_over(team, vague):
    """
    Vérifie si tous les membres de l'équipe sont morts.
    Affiche un game over si c'est le cas.
    Retourne True si game over, False sinon.
    """
    tous_morts = all(member['PV'] <= 0 for member in team)
    
    if tous_morts:
        print("\n" + "="*50)
        print("💀💀💀      GAME OVER      💀💀💀")
        print("="*50)
        print(f"Votre équipe a été anéantie...")
        print(f"Vous avez survécu à {vague } vague(s)")
        print("="*50 + "\n")
        return True
    
    return False

vague = -1
def afficher_score():
    score = get_vague() * 1000
    print("*******************************")
    print(f"*** Votre score est de {score} ***")
    print("*******************************")
    return score

def get_score():
    score = get_vague() * 1000
    return score


def add_vague(n):
    global vague
    vague += n

def get_vague():
    return vague


def score_register(pseudo, score):
    game_score = {"pseudo": pseudo, "score" : score}
    client = MongoClient("mongodb://localhost:27017/")
    db = client["rpg_game"]
    collectionScore = db["Score"]
    collectionScore.insert_many([{"pseudo": pseudo, "score" : score }])