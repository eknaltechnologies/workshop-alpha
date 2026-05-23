def create_kingdom():
    kingdom = {
        "king": "Arthur",
        "castle": "Camelot",
        "gold": 500,
        "army": ["knight", "archer", "catapult"]
    }

    print("\n===== KINGDOM RECORDS =====")
    print(kingdom)

    return kingdom


def access_information(kingdom):
    print("\n===== ACCESSING INFORMATION =====")
    print("King:", kingdom["king"])
    print("Army:", kingdom["army"])
    print("Queen:", kingdom.get("queen"))


def update_records(kingdom):
    print("\n===== UPDATING RECORDS =====")

    kingdom["gold"] += 250
    kingdom["queen"] = "Guinevere"
    kingdom["castle"] = "New Camelot"
    kingdom["dragon"] = True

    print(kingdom)


def delete_information(kingdom):
    print("\n===== DELETING INFORMATION =====")

    if "catapult" in kingdom["army"]:
        kingdom["army"].remove("catapult")

    if "queen" in kingdom:
        del kingdom["queen"]

    removed_gold = kingdom.pop("gold")
    print("Gold Taken:", removed_gold)

    print(kingdom)


def search_kingdom(kingdom):
    print("\n===== SEARCHING KINGDOM =====")

    print("Does gold exist?", "gold" in kingdom)

    print("\nKeys:")
    for key in kingdom.keys():
        print(key)

    print("\nValues:")
    for value in kingdom.values():
        print(value)

    print("\nItems:")
    for item in kingdom.items():
        print(item)


def manage_villages(kingdom):
    print("\n===== VILLAGES =====")

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

    print("Population of v2:",
          kingdom["villages"]["v2"]["population"])

    kingdom["villages"]["v1"]["crops"].append("sugarcane")

    kingdom["villages"]["v3"]["population"] += 50

    print("\nUpdated Villages:")
    print(kingdom["villages"])


def loop_records(kingdom):
    print("\n===== LOOPING THROUGH KINGDOM =====")

    for key, value in kingdom.items():
        print(f"{key} : {value}")

    print("\n===== VILLAGE REPORT =====")

    for village, details in kingdom["villages"].items():
        population = details["population"]
        crops = ", ".join(details["crops"])

        print(
            f"Village {village} has {population} people and grows {crops}"
        )


def army_power():
    print("\n===== ARMY POWER =====")

    army_stats = {
        "knight": 50,
        "archer": 30,
        "dragon": 300
    }

    army_stats["archer"] += 10

    strongest = max(army_stats, key=army_stats.get)

    print("Strongest Unit:", strongest)

    del army_stats["knight"]

    print("Updated Army Stats:")
    print(army_stats)

    return army_stats


def kingdom_events(kingdom, army_stats):
    print("\n===== KINGDOM EVENTS =====")

    kingdom["gold"] = kingdom.get("gold", 0) + 200

    kingdom["villages"]["v1"]["population"] -= 20

    if "archer" in kingdom["army"]:
        kingdom["army"].remove("archer")

    if "dragon" in army_stats:
        army_stats["dragon"] -= 50

    kingdom["alliance"] = "Northern Empire"

    print("\nKingdom After Events:")
    print(kingdom)

    print("\nArmy Stats After Events:")
    print(army_stats)


def final_challenge(kingdom, army_stats):
    print("\n===== FINAL INTERACTIVE CHALLENGE =====")

    soldier = input("Enter new soldier name: ")
    strength = int(input("Enter soldier strength: "))

    army_stats[soldier] = strength

    print("\nArmy Stats Updated:")
    print(army_stats)

    village_name = input("\nEnter new village name: ")
    population = int(input("Enter population: "))
    crops = input(
        "Enter crops separated by commas: "
    ).split(",")

    kingdom["villages"][village_name] = {
        "population": population,
        "crops": [crop.strip() for crop in crops]
    }

    print("\nVillages After Addition:")
    print(kingdom["villages"])

    remove_village = input(
        "\nEnter village name to remove: "
    )

    if remove_village in kingdom["villages"]:
        del kingdom["villages"][remove_village]
        print("Village removed successfully.")
    else:
        print("Village not found.")

    print("\nUpdated Kingdom:")
    print(kingdom)


def main():
    kingdom = create_kingdom()

    access_information(kingdom)

    update_records(kingdom)

    delete_information(kingdom)

    search_kingdom(kingdom)

    manage_villages(kingdom)

    loop_records(kingdom)

    army_stats = army_power()

    kingdom_events(kingdom, army_stats)

    final_challenge(kingdom, army_stats)


main()