from utils import *
from models import monsters

def systeme_de_combat(team, pseudo):
    vague = 0
    while True:
        print(f"\n================= VAGUE {get_vague() + 2} =================")
        afficher_team(team, pseudo)  # affiche l'équipe avant chaque vague
        
        # génère et affiche les monstres de la vague
        monstre = generer_monstre(monsters, vague)
        afficher_monstre([monstre], get_vague())
        
        # vérifie si l'équipe est morte
        if verifier_game_over(team, vague):
            break

        # combat avec le monstre de la vague
        tour = 1
        while monstre['PV'] > 0 and any(member['PV'] > 0 for member in team):
            print(f"\n--- TOUR {tour} ---")
            
            # Attaque de l'équipe
            attaque_gentil(team, monstre)
            
            # Affichage des PV après attaque de l'équipe
            print(f"\nÉtat après l'attaque de l'équipe :")
            print(f"{monstre['name']} - ❤️  PV: {max(0, monstre['PV'])}")
            
            # Vérifier si le monstre est mort
            if monstre['PV'] <= 0:
                print(f"\n{monstre['name']} a été vaincu !")
                break
            
            # Attaque du monstre
            attaque_mechant(monstre, team)
            
            # Affichage des PV et de l'équipe après attaque du monstre
            print(f"\nÉtat de l'équipe après l'attaque du monstre :")
            afficher_team(team, pseudo)
            
            # Vérifier si l'équipe est morte
            if not any(member['PV'] > 0 for member in team):
                print(f"\nVotre équipe est six pieds sous terre...")
                break
            
            tour += 1
            input("Appuyez sur Entrée pour continuer au prochain tour...")
        
        add_vague(1)
        input("Appuyez sur Entrée pour la prochaine vague...")
        vague = get_vague()

# système de défense  par rapport a l'attaque
def damage_reduction(atk, den):
    #si dmg < 0 alors l'attaque ne fait rien
    if atk <= den:
        return 1
    else :
        damage = atk - (100//100 + den)  # formule de réduction
        return damage

def attaque_gentil(team, monstre):
    for member in team:
        atk = member['ATK']
        den = monstre['DEF']
        damage = damage_reduction(atk, den)
        monstre['PV'] -= damage
        print(f"{member['name']} attaque {monstre['name']} et inflige {damage} dégâts !")

def attaque_mechant(monstre, team):
    victime = random.choice(team)
    atk = monstre['ATK']
    den = victime['DEF']
    damage = damage_reduction(atk, den)
    victime['PV'] -= damage
    print(f"{monstre['name']} attaque {victime['name']} et inflige {damage} dégâts !")
