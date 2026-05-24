
# Setting up a nested dictionary for the kingdom
kingdom = {
    "king": "Arthur",
    "castle": "New Camelot",
    "army": ["knight", "archer"],
    "dragon": True,
    "villages": {
        "v1": {"population": 120, "crops": ["wheat", "barley"]},
        "v2": {"population": 80, "crops": ["rice"]},
        "v3": {"population": 200, "crops": ["wheat", "corn"]}
    }
}

# Setting up  flat dictionary for the army combat strength numbers
army_stats = {
    "knight": 50,
    "archer": 30,
    "dragon": 300
}

#  villages -> v1 -> crops, and append sugarcane to the list
kingdom["villages"]["v1"]["crops"].append("sugarcane")

# Read v3's current population (200), add 50, and save 250 back to that slot
kingdom["villages"]["v3"]["population"] = kingdom["villages"]["v3"]["population"] + 50

print("--- Kingdom Key-Value Pairs ---")
for key, value in kingdom.items():
    print(f"{key}: {value}")

print("\n--- Village Reports ---")
# check "villages" section to pull out information for sentences
for village_id, village_info in kingdom["villages"].items():
    people = village_info["population"]
    crops = ", ".join(village_info["crops"]) # Cleans list brackets up with commas
    print(f"Village {village_id} has {people} people and grows {crops}")

# Find the unit with the highest value in army_stats (key looks at numbers, not names)
strongest_unit = max(army_stats, key=army_stats.get)
highest_value = army_stats[strongest_unit]
print(f"\n[INFO] Strongest unit initially: {strongest_unit} ({highest_value})")

# Event 1: Festival adds 200 gold. (Creates the "gold" drawer since it's missing)
if "gold" in kingdom:
    kingdom["gold"] = kingdom["gold"] + 200
else:
    kingdom["gold"] = 200

# Event 2: Plague strikes v1. Subtract 20 from their population count
kingdom["villages"]["v1"]["population"] = kingdom["villages"]["v1"]["population"] - 20

# Event 3: War removes archers from army stats and reduced dragon strength by 50
if "archer" in army_stats:
    del army_stats["archer"]
army_stats["dragon"] = army_stats["dragon"] - 50

# Event 4: Alliance creates a brand new root level drawer with text inside
kingdom["alliance"] = "Northern Empire"

print("\n System updates complete. Scenario events processed!")
print("-" * 50)


#  Add a New Soldier type
print("\n--- Action 1: Add a New Soldier ---")
soldier_name = input("Enter the name of the new soldier type : ")
soldier_strength = int(input(f"Enter the strength value for {soldier_name}: "))

# Add the user's choices into the army stats dictionary
army_stats[soldier_name] = soldier_strength
print("Updated Army Stats:", army_stats)
print("-" * 40)


# Action 2: Add a New Village layout
print("\n--- Action 2: Add a New Village ---")
new_village_id = input("Enter the new village ID : ")
new_pop = int(input(f"Enter the population for {new_village_id}: "))
crops_input = input(f"Enter crops for :{new_village_id} ")

# Split text input wherever commas sit, and trim accidental blank spaces
new_crops_list = [crop.strip() for crop in crops_input.split(",")]

# Put the whole package into a brand new village drawer inside kingdom
kingdom["villages"][new_village_id] = {
    "population": new_pop,
    "crops": new_crops_list
}
print("Updated Kingdom Villages:", kingdom["villages"])
print("-" * 40)


# Action 3: Remove an Existing Village safely
print("\n--- Action 3: Remove a Village ---")
village_remove = input("Enter the ID of the village you want to remove : ")

# Check if it exists before deleting to guarantee the script won't crash
if village_remove in kingdom["villages"]:
    del kingdom["villages"][village_remove]
    print(f"Successfully removed {village_remove}.")
else:
    print(f"Error: {village_remove} was not found in the kingdom.")


print("\n==========================================")
print("FINAL UPDATED KINGDOM DATA RECORD")
print("==========================================")
print(kingdom)