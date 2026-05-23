# Python Kingdom Management – Final Dictionary Challenge

# 1. Create the Kingdom Records
kingdom = {
    "king": "Arthur",
    "castle": "Camelot",
    "gold": 500,
    "army": ["knight", "archer", "catapult"]
}

print("Initial Kingdom Dictionary:")
print(kingdom)


# 2. Accessing Information
print("\nKing Name:", kingdom["king"])

print("Army List:", kingdom["army"])

print("Queen:", kingdom.get("queen"))


# 3. Updating the Records
kingdom["gold"] += 250

kingdom["queen"] = "Guinevere"

kingdom["castle"] = "New Camelot"

kingdom["dragon"] = True

print("\nUpdated Kingdom:")
print(kingdom)


# 4. Deleting Information

# Remove "catapult" from army
kingdom["army"].remove("catapult")

# Delete queen key
del kingdom["queen"]

# Remove gold using pop()
removed_gold = kingdom.pop("gold")

print("\nRemoved Gold:", removed_gold)

print("Kingdom after deletion:")
print(kingdom)


# 5. Searching the Kingdom

# Check if gold exists
if "gold" in kingdom:
    print("\nGold exists in kingdom")
else:
    print("\nGold does not exist")

# Print keys
print("\nKeys:")
print(kingdom.keys())

# Print values
print("\nValues:")
print(kingdom.values())

# Print items
print("\nItems:")
print(kingdom.items())


# 6. Villages (Nested Dictionary)

kingdom["villages"] = {
    "v1": {
        "population": 120,
        "crops": ["wheat", "barley"]
    },

    "v2": {
        "population": 80,
        "crops": ["rice"]
    },

    "v3": {
        "population": 200,
        "crops": ["wheat", "corn"]
    }
}

# Print population of v2
print("\nPopulation of v2:")
print(kingdom["villages"]["v2"]["population"])

# Add sugarcane to v1
kingdom["villages"]["v1"]["crops"].append("sugarcane")

# Increase v3 population by 50
kingdom["villages"]["v3"]["population"] += 50

print("\nUpdated Villages:")
print(kingdom["villages"])


# 7. Looping Through Records

print("\n--- Kingdom Records ---")

for key, value in kingdom.items():
    print(key, ":", value)

print("\n--- Village Details ---")

for village, details in kingdom["villages"].items():
    print(
        f"Village {village} has "
        f"{details['population']} people and grows "
        f"{details['crops']}"
    )


# 8. Army Power (Dictionary of Stats)

army_stats = {
    "knight": 50,
    "archer": 30,
    "dragon": 300
}

# Increase archer strength
army_stats["archer"] += 10

print("\nUpdated Army Stats:")
print(army_stats)

# Find strongest unit
strongest_unit = max(army_stats, key=army_stats.get)

print("Strongest Unit:", strongest_unit)

# Remove knight
del army_stats["knight"]

print("Army Stats after removing knight:")
print(army_stats)


# 9. Kingdom Events (Simulation)

# Festival adds gold
kingdom["gold"] = 200

# Plague reduces v1 population
kingdom["villages"]["v1"]["population"] -= 20

# War removes archer
if "archer" in kingdom["army"]:
    kingdom["army"].remove("archer")

# Dragon loses strength
army_stats["dragon"] -= 50

# Alliance formed
kingdom["alliance"] = "Northern Empire"

print("\nKingdom after Events:")
print(kingdom)

print("\nArmy Stats after War:")
print(army_stats)


# 10. Final Interactive Challenge

print("\n--- Final Interactive Challenge ---")

# Add new soldier
soldier = input("Enter new soldier name: ")
strength = int(input("Enter soldier strength: "))

army_stats[soldier] = strength

print("\nUpdated Army Stats:")
print(army_stats)

# Add new village
village_name = input("\nEnter village name: ")

population = int(input("Enter population: "))

crops = input("Enter crops separated by commas: ").split(",")

kingdom["villages"][village_name] = {
    "population": population,
    "crops": crops
}

print("\nVillages after adding new village:")
print(kingdom["villages"])

# Remove village
remove_village = input("\nEnter village name to remove: ")

if remove_village in kingdom["villages"]:
    del kingdom["villages"][remove_village]
    print("Village removed successfully.")
else:
    print("Village not found.")

print("\nFinal Kingdom Data:")
print(kingdom)