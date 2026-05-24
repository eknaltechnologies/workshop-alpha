print("============PYTHON KINGDOM MANAGEMENT - ROYAL DATA KEEPER SCRIPT===========")
kingdom={
     "king": "Arthur",  
     "castle": "Camelot", 
     "gold": 500, 
     "army": ["knight", "archer", "catapult"]
        }
print(f"Kingdom records:{kingdom}")
#Accesing information
print(f"King:{kingdom['king']}")
print(f"army:{kingdom['army']}")
#fetch queen
fetch_queen=kingdom.get("queen")
print(f"safely fetching 'queen':{fetch_queen}")

#Update records
kingdom["gold"] = kingdom["gold"] + 250
kingdom.update({
    "queen": "Guinevere",
    "castle": "New Camelot",
    "dragon": True
})
print(f"Updated Records: {kingdom}\n")

#delete records
removed_unit = kingdom["army"].pop(2)
print(f"The {removed_unit} removed from the army")
del kingdom['queen']
gold_taken = kingdom.pop("gold")
print(f"Gold taken from treasury: {gold_taken}")
print(f"Records after deletions: {kingdom}\n")

#searching the kingdom
print(f"Does the 'gold' exists?:{'gold' in kingdom}")
print("\n--- KEYS ONLY ---")
print(list(kingdom.keys()))

print("\n--- VALUES ONLY ---")
print(list(kingdom.values()))

print("\n--- ITEMS (PAIRS) ---")
print(list(kingdom.items()))

#Villages (Nested dic)
kingdom.update({
    "villages": {
        "v1": {"population": 120, "crops": ["wheat", "barley"]},
        "v2": {"population": 80, "crops": ["rice"]},
        "v3": {"population": 200, "crops": ["wheat", "corn"]}
    }
})
v2_population = kingdom.get("villages").get("v2").get("population")

print(v2_population)
kingdom.get("villages").get("v1").get("crops").append("sugarcane")
print(kingdom["villages"]["v1"]["crops"])

v3_population = kingdom["villages"]["v3"]["population"]
new_population = v3_population + 50
kingdom["villages"]["v3"]["population"] = new_population

print(f"V3 population is increased to: {kingdom['villages']['v3']['population']}\n")
#Looping through records
for key, value in kingdom.items():
    print(f"{key}: {value}\n")
for village_id, village_info in kingdom["villages"].items():
    people = village_info["population"]
    crops = village_info["crops"]
    print(f"Village {village_id} has {people} people and grows {crops}\n")
#  Army Power (Dictionary of Stats)   
army_stats = {
    "knight": 50,
    "archer": 30,
    "dragon": 300
}    
army_stats["archer"] = army_stats["archer"] + 10
print(f"Updated Army Stats: {army_stats}")
strongest_unit = max(army_stats, key=army_stats.get)
highest_value = army_stats[strongest_unit]
print(f"The strongest unit is {strongest_unit} with a strength of {highest_value}.\n")
#delete knight
del army_stats["knight"]
print(f"Updated army stats after removal: {army_stats}")

#kingdom events
if "gold" in kingdom:
    kingdom["gold"] = kingdom["gold"] + 200
else:
    kingdom["gold"] = 200
kingdom["villages"]["v1"]["population"] = kingdom["villages"]["v1"]["population"] - 20
del army_stats["archer"]
army_stats["dragon"] = army_stats["dragon"] - 50

kingdom["alliance"] = "Northern Empire"
print("\nUpdated Kingdom:", kingdom)
print("\nUpdated Army Stats:", army_stats)
print("--- Action 1: Add a New Soldier ---")
soldier_name = input("Enter the name of the new soldier type: ")
soldier_strength = int(input(f"Enter the strength value for {soldier_name}: "))
army_stats[soldier_name] = soldier_strength

# Print updated status
print("Updated Army Stats:", army_stats)
print("-" * 40)
print("\n--- Action 2: Add a New Village ---")
new_village_id = input("Enter the new village ID : ")
new_pop = int(input(f"Enter the population for {new_village_id}: "))
print("\n--- Action 2: Add a New Village ---")
new_village_id = input("Enter the new village ID : ")
new_pop = int(input(f"Enter the population for {new_village_id}: "))
crops_input = input(f"Enter crops for {new_village_id} (separated by commas): ")
new_crops_list = crops_input.split(",")
kingdom["villages"][new_village_id] = {
    "population": new_pop,
    "crops": new_crops_list
}
print("Updated Kingdom Villages:", kingdom["villages"])
print("-" * 40)
print("\n--- Action 3: Remove a Village ---")
village_to_remove = input("Enter the ID of the village you want to remove: ")
if village_to_remove in kingdom["villages"]:
    del kingdom["villages"][village_to_remove]
    print(f"Successfully removed {village_to_remove}.")
else:
    print(f"Error: {village_to_remove} was not found in the kingdom.")

print("\nFinal Updated Kingdom:")
print(kingdom)