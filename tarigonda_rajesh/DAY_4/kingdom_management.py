# 1 Creating Kingdom Records

kingdom = {
    "king": "Arthur",
    "castle": "Camelot",
    "gold": 500,
    "army": ["knight", "archer", "catapult"],
}


print(f"King: {kingdom['king']}\nArmy: {kingdom['army']}")

# 2 Accessing Information
print(kingdom.get("queen"))

# 3 Updating Records
kingdom["gold"] += 250
kingdom["queen"] = "Guinevere"
kingdom["castle"] = "New Camelot"
kingdom["dragon"] = True
print(f"After Update:\n{kingdom}")

# 4 Deleting Information
kingdom["army"].remove("catapult")

del kingdom["queen"]
print(f"Gold taken: {kingdom.pop('gold')}")

# 5 Searching the Kingdom

print(f"Gold exists in kingdom: {'gold' in kingdom}")

print(f"Keys: {list(kingdom.keys())}")
print(f"Values: {list(kingdom.values())}")
print(f"Items: {list(kingdom.items())}")

# 6 Villages (Nested Dictionary)

kingdom["villages"] = {
    "v1": {
        "population": 120,
        "crops": ["wheat", "barley"],
    },
    "v2": {
        "population": 80,
        "crops": ["rice"],
    },
    "v3": {
        "population": 200,
        "crops": ["wheat", "corn"],
    },
}

print(f"Population of V2: " f"{kingdom['villages']['v2']['population']}")

kingdom["villages"]["v1"]["crops"].append("sugarcane")
kingdom["villages"]["v3"]["population"] += 50

print(f"Updated Kingdom:\n{kingdom}")

# 7 Looping Through Records

for key, value in kingdom.items():
    print(f"{key} -> {value}")

for key, value in kingdom["villages"].items():
    print(f"{key} --> {value}")

# 8 Army Power

kingdom["army_stats"] = {
    "knight": 50,
    "archer": 30,
    "dragon": 300,
}

kingdom["army_stats"]["archer"] += 10

strong_army = 0

for value in kingdom["army_stats"].values():
    if value > strong_army:
        strong_army = value

print(f"Strongest Unit: {strong_army}")

del kingdom["army_stats"]["knight"]

# 9 Kingdom Events

kingdom["gold"] = 200
kingdom["villages"]["v1"]["population"] -= 20

kingdom["army"].remove("archer")

kingdom["army_stats"]["dragon"] -= 50

kingdom["alliance"] = "Northern Empire"

print(
    f"Gold: {kingdom['gold']}\n"
    f"Population of v1: "
    f"{kingdom['villages']['v1']['population']}\n"
    f"Dragon Health: "
    f"{kingdom['army_stats']['dragon']}\n"
    f"Alliance: {kingdom['alliance']}"
)

# 10 Interactive

new_soldier = input("Enter the new soldier: ")

strength = int(input("Enter the strength of army: "))

kingdom["army_stats"][new_soldier] = strength

village = input(f"Enter the village to remove " f"{list(kingdom['villages'].keys())}: ")

for key, value in kingdom.items():
    print(f"{key} --> {value}")
