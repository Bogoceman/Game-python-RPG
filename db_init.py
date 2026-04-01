from pymongo import MongoClient
from models import *

client = MongoClient("mongodb://localhost:27017/")
db = client["rpg_game"]
collectionMonsters = db["monsters"]
collectionCharacters = db["characters"]
collectionBuffs = db["buffs"]


collectionCharacters.insert_many([{"name": name, **stats} for name, stats in characters.items()])
collectionMonsters.insert_many([{"name": name, **stats} for name, stats in monsters.items()])
collectionBuffs.insert_many([{"name": name, **stats } for name, stats in buffs.items()])