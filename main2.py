from utils import *
from models import *
from game import *


# Récuperer un personnage 
def get_character_by_name(name):
    client = MongoClient("mongodb://localhost:27017/")
    try:
        collection = client["rpg_game"]["characters"]
        character = collection.find_one({"name": name})
        return character
    finally:
        client.close()



guerrier = get_character_by_name("Guerrier")
print(guerrier["_id"])