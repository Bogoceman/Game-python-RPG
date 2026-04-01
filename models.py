characters = {
	"Guerrier": {"ATK": 15, "DEF": 10, "PV": 100},
	"Mage": {"ATK": 20, "DEF": 5, "PV": 80},
	"Archer": {"ATK": 18, "DEF": 7, "PV": 90},
	"Voleur": {"ATK": 22, "DEF": 8, "PV": 85},
	"Paladin": {"ATK": 14, "DEF": 12, "PV": 110},
	"Sorcier": {"ATK": 25, "DEF": 3, "PV": 70},
	"Chevalier": {"ATK": 17, "DEF": 15, "PV": 120},
	"Moine": {"ATK": 19, "DEF": 9, "PV": 95},
	"Berserker": {"ATK": 23, "DEF": 6, "PV": 105},
	"Chasseur": {"ATK": 16, "DEF": 11, "PV": 100},
}

monsters = {
	"Gobelin": {"ATK": 10, "DEF": 5, "PV": 50},
	"Orc": {"ATK": 20, "DEF": 8, "PV": 120},
	"Dragon": {"ATK": 35, "DEF": 20, "PV": 300},
	"Zombie": {"ATK": 12, "DEF": 6, "PV": 70},
	"Troll": {"ATK": 25, "DEF": 15, "PV": 200},
	"Spectre": {"ATK": 18, "DEF": 10, "PV": 100},
	"Golem": {"ATK": 30, "DEF": 25, "PV": 250},
	"Vampire": {"ATK": 22, "DEF": 12, "PV": 150},
	"Loup-garou": {"ATK": 28, "DEF": 18, "PV": 180},
	"Squelette": {"ATK": 15, "DEF": 7, "PV": 90},
    "Jeffrey Eipstein": {"ATK": 67, "DEF": 271, "PV": 666},
}

buffs = {
    "Dégats I": {"text": "Augmentation des dégats de 5%", "value" : 1.05, "stats": ["ATK"]},
    "Dégats II": {"text": "Augmentation des dégats de 10%", "value" : 1.1, "stats": ["ATK"]},
    "Dégats III": {"text": "Augmentation des dégats de 15%", "value" : 1.15, "stats": ["ATK"]},
    "Dégats IV": {"text": "Augmentation des dégats de 20%", "value" : 1.2, "stats": ["ATK"]},
    "Dégats V": {"text": "Augmentation des dégats de 25%", "value" : 1.25, "stats": ["ATK"]},
    "Défense I": {"text": "Augmentation de la défense de 5%", "value" : 1.05, "stats": ["DEF"]},
    "Défense II": {"text": "Augmentation de la défense de 10%", "value" : 1.1, "stats": ["DEF"]},
    "Défense III": {"text": "Augmentation de la défense de 15%", "value" : 1.15, "stats": ["DEF"]},
    "Défense IV": {"text": "Augmentation de la défense de 20%", "value" : 1.2, "stats": ["DEF"]},
    "Défense V": {"text": "Augmentation de la défense de 25%", "value" : 1.25, "stats": ["DEF"]},
    "Soins I": {"text": "Augmente les points de vie d'un personnage de 15", "value" : 15, "stats": ["PV"]},
    "Soins II": {"text":"Augmente les points de vie d'un personnage de 30", "value" : 30, "stats": ["PV"]},
    "Soins III": {"text": "Augmente les points de vie d'un personnage de 40", "value" : 40, "stats": ["PV"]},
    "Soins IV": {"text": "Augmente les points de vie d'un personnage de 50", "value" : 50, "stats": ["PV"]},
    "Soins V": {"text": "Augmente les points de vie d'un personnage de 75", "value" : 75, "stats": ["PV"]},
    "Omniscience": {"text": "Augmente toute les statisiques de 15", "value" : 15, "stats": ["PV", "ATK", "DEF"]} #changer la clée de l'aumentation de stats et créer une clée pour le text affiché

}