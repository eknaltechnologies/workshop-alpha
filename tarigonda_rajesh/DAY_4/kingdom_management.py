# 1 Creating Kingdom Records
kingdom = {"king": "Arthur", "castle": "Camelot", "gold": 500, "army": ["knight", "archer", "catapult"]}

print(f"King: {kingdom['king']}\nArmy: {kingdom['army']}")

# 2 Accessing Information
print(kingdom.get("queen"))


# 3 Updating records
kingdom["gold"] += 250
kingdom["queen"] = "Guinevere"
kingdom["castle"] = "New Camelot"
kingdom["dragon"] = True
print(f"After Update:\n{kingdom}")

# 4 Deleting Information
kingdom["army"].remove("catapult")
del kingdom["queen"]
print(f'Gold taken: {kingdom.pop("gold")}')

# 5 Searching the Kingdom

print(f"Gold exists in kingdom : {'gold' in kingdom}")
print(f"Keys: {list(kingdom.keys())}")
print(f"Values: {list(kingdom.values())}")
print(f"Items: {list(kingdom.items())}")

# 6 Villages (Nested Dictionary)

kingdom["villages"] = {
    "v1": {"population": 120, "crops": ["wheat", "barley"]},
    "v2": {"population": 80, "crops": ["rice"]},
    "v3": {"population": 200, "crops": ["wheat", "corn"]},
}

print(f"Polualtion of V2: {kingdom['villages']['v2']['population']}")
kingdom["villages"]["v1"]["crops"].append("sugarcane")
kingdom["villages"]["v3"]["population"] += 50

print(f"Updated Kindom: \n{kingdom}")

# 7 Looping Through Records
for k, v in kingdom.items():
    print(f"{k} -> {v}")

for k, v in kingdom["villages"].items():
    print(f"{k} --> {v}")
# 8 Army Power
kingdom["army_stats"] = {"knight": 50, "archer": 30, "dragon": 300}

kingdom["army_stats"]["archer"] += 10

strong_army = 0
for v in kingdom["army_stats"].values():
    if v > strong_army:
        strong_army = v


print(f"Strongest Unit: {strong_army}")
del kingdom["army_stats"]["knight"]

# 9Kingdom Events
kingdom["gold"] = 200
kingdom["villages"]["v1"]["population"] -= 20
kingdom["army"].remove("archer")
kingdom["army_stats"]["dragon"] -= 50
kingdom["alliance"] = "Northen Empire"

print(f"Gold: {kingdom['gold']}\
      \nPopulation of v1:{kingdom['villages']['v1']['population']}\
      \nDragon Health: {kingdom['army_stats']['dragon']}\
      \nAllience: {kingdom['alliance']}")

# 10 Inteactive
new_solder = input("Enter the new Soldiers: ")
strength = int(input("Enter the strength of army: "))
kingdom["army_stats"][new_solder] = strength
village = input(f"Enter the Village to remove {list(kingdom['villages'].keys())} :")

for k, v in kingdom.items():
    print(f"{k}--> {v}")
