try:
    kingdom = {
        "king": "Arthur",
        "castle": "Camelot",
        "gold": 500,
        "army": ["knight", "archer", "catapult"],
    }

    print(kingdom)

    # accessing values

    print(f"King: {kingdom['king']}")
    print(f"Army: {kingdom['army']}")
    print("The queen is:", kingdom.get("queen"))

    print("---------- updating values ------------")

    # updating records

    kingdom["gold"] += 250

    print("Updated Gold:", kingdom["gold"])

    kingdom["queen"] = "Guinevere"

    kingdom["castle"] = "New Camelot"

    print("Updated Castle:", kingdom["castle"])

    kingdom["dragon"] = True

    print("Dragon Added:", kingdom["dragon"])

    print("---------- deleting values ------------")

    kingdom["army"].remove("catapult")

    del kingdom["queen"]

    removed_gold = kingdom.pop("gold")

    print("Removed Gold:", removed_gold)

    print("Updated Kingdom:", kingdom)

    print("---------- searching values ------------")

    print("Does gold exist?", "gold" in kingdom)

    print("Keys:", kingdom.keys())

    print("Values:", kingdom.values())

    print("Items:", kingdom.items())

    print("---------- nested dictionary ------------")

    kingdom["villages"] = {
        "v1": {"population": 120, "crops": ["wheat", "barley"]},
        "v2": {"population": 80, "crops": ["rice"]},
        "v3": {"population": 200, "crops": ["wheat", "corn"]},
    }

    print("Villages:", kingdom["villages"])

    kingdom["villages"]["v1"]["crops"].append("sugarcane")

    kingdom["villages"]["v3"]["population"] += 50

    print("Updated v1 crops:", kingdom["villages"]["v1"]["crops"])

    print("---------- looping record ------------")

    for key, value in kingdom.items():
        print(key, ":", value)

    for village, info in kingdom["villages"].items():
        print(
            "Village",
            village,
            "has",
            info["population"],
            "people and grows",
            info["crops"],
        )

    print("---------- army stats -----------")

    kingdom["army_stats"] = {"knight": 50, "archer": 30, "dragon": 300}

    print("Army Stats:", kingdom["army_stats"])

    kingdom["army_stats"]["archer"] += 10

    strongest = max(kingdom["army_stats"], key=kingdom["army_stats"].get)

    print("Strongest Unit:", strongest)

    del kingdom["army_stats"]["knight"]

    print("Updated Army Stats:", kingdom["army_stats"])

    print("---------- kingdom events ------------")

    kingdom["gold"] = 200

    kingdom["villages"]["v1"]["population"] -= 20

    if "archer" in kingdom["army_stats"]:
        del kingdom["army_stats"]["archer"]

    kingdom["army_stats"]["dragon"] -= 50

    kingdom["alliance"] = "Northern Empire"

    print("Updated Kingdom:", kingdom)

    print("---------- adding soliders ------------")

    soldier = input("Enter new soldier: ")

    strength = int(input("Enter strength: "))

    kingdom["army_stats"][soldier] = strength

    print("Updated Army Stats:", kingdom["army_stats"])

    print("---------- adding villages ------------")

    village = input("Enter village name: ")

    population = int(input("Enter population: "))

    crops = input("Enter crop name: ").split(",")

    kingdom["villages"][village] = {"population": population, "crops": crops}

    print("Updated Villages:", kingdom["villages"])

    print("---------- removing villages ------------")

    remove_village = input("Enter village to remove: ")

    if remove_village in kingdom["villages"]:
        del kingdom["villages"][remove_village]

        print(remove_village, "removed")

    else:
        print("Village not found")

    print("Final Kingdom:", kingdom)


except KeyboardInterrupt:
    print("\nProgram stopped by user")
