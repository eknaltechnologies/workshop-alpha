try:
    kingdom = {
        "king": "Arthur",
        "castle": "Camelot",
        "gold": 500,
        "army": ["knight", "archer", "catapult"]
    }
    print("Kingdom records initialized:", kingdom)

    # accessing values
    print(f"King of the kingdom: {kingdom['king']}")
    print(f"Army members: {kingdom['army']}")
    print("Queen information:", kingdom.get("queen"))

    # updating the records
    kingdom["gold"] += 250
    print("Treasury updated. Total gold:", kingdom["gold"])

    kingdom["queen"] = "Guinevere"
    kingdom["castle"] = "New Camelot"

    print("Castle updated to:", kingdom["castle"])

    kingdom["dragon"] = True
    print("Dragon added to the kingdom:", kingdom["dragon"])

    # deletion info
    kingdom["army"].remove("catapult")
    del kingdom["queen"]

    updated_gold = kingdom.pop("gold")
    print("Gold removed from treasury:", updated_gold)
    print("Current kingdom details:", kingdom)

    # searching the kingdom
    if "gold" in kingdom:
        print("Gold is still available in the kingdom")

    print("Kingdom keys:", kingdom.keys())
    print("Kingdom values:", kingdom.values())
    print("Complete kingdom records:", kingdom.items())

    # nested dictionary
    kingdom["villages"] = {
        "v1": {"population": 120, "crops": ["wheat", "barley"]},
        "v2": {"population": 80, "crops": ["rice"]},
        "v3": {"population": 200, "crops": ["wheat", "corn"]}
    }

    print("Villages added to the kingdom:", kingdom["villages"])

    kingdom["villages"]["v1"]["crops"].append("sugarcane")

    print(
        "Updated crops in village v1:",
        kingdom["villages"]["v1"]["crops"]
    )

    # looping through records
    for key, value in kingdom.items():
        print(key, ":", value)

    for village, data in kingdom["villages"].items():
        print(
            "Village",
            village,
            "has",
            data["population"],
            "people and grows",
            data["crops"]
        )

    # army power
    kingdom["army_stats"] = {
        "knight": 50,
        "archer": 30,
        "dragon": 300
    }

    print("Army strength details:", kingdom["army_stats"])

    kingdom["army_stats"]["archer"] += 10

    high_strength = max(kingdom["army_stats"].values())

    print("Highest army strength value:", high_strength)

    del kingdom["army_stats"]["knight"]

    print("Updated army statistics:", kingdom["army_stats"])

    # kingdom events
    kingdom["gold"] = 0
    kingdom["gold"] += 200
    kingdom["villages"]["v1"]["population"] -= 20

    del kingdom["army_stats"]["archer"]

    kingdom["army_stats"]["dragon"] -= 50

    kingdom["alliance"] = "Northern Empire"

    print("Final kingdom status:", kingdom)

    # Add new soldier
    new_soldier = input("Enter new soldier: ")
    strength = int(input(f"Enter strength for {new_soldier}: "))

    kingdom["army_stats"][new_soldier] = strength

    print("Updated army details:", kingdom["army_stats"])

    # Add new village
    village_name = input("Enter new village name: ")
    population = int(input("Enter population: "))
    crops = input("Enter crops (comma separated): ").split(",")

    kingdom["villages"][village_name] = {
        "population": population,
        "crops": crops
    }

    print("Updated village details:", kingdom["villages"])

    # Remove a village
    remove_village = input("Enter village to remove: ")

    if remove_village in kingdom["villages"]:
        del kingdom["villages"][remove_village]

    print("Villages after removal:", kingdom["villages"])

except KeyboardInterrupt:
    print("Program interrupted.")