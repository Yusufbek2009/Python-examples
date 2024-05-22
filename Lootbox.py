import random as r
import time as t

# Updates will be soon ;)

# Items
items = ["Golden Hand", "Fortune Cube", "Infenal Gun",
    "Cookie Jar", "Pearl of Galaxy", "Shadow Sword",
    "Dragon's Scream", "True Darkness", "Diamond Egg",
    "Living Legend", "Slime Bucket", "Master Key"]

# Rarities
rarity = {
    "Golden Hand": "Common",
    "Fortune Cube": "Epic",
    "Infenal Gun": "Rare",
    "Cookie Jar": "Common",
    "Pearl of Galaxy": "Legendary",
    "Shadow Sword": "Epic",
    "Dragon's Scream": "Rare",
    "True Darkness": "Legendary",
    "Diamond Egg": "Rare",
    "Living Legend": "Epic",
    "Slime Bucket": "Common",
    "Master Key": "Epic"
}

ch = r.choice(items)
rrt = rarity[ch]

print("One Moment...")
t.sleep(3)
print()
print("======================")
print(f"You got {ch} which is {rrt} item.")
print("Have a good day!")
print("Closing after 5 seconds.")
print("======================")
t.sleep(5)
