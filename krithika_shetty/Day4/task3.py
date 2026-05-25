def show_section(title):
    print(f"\n===== {title} =====")


def show_data(title, data):
    print(f"\n{title}:")
    print(data)


def create_kingdom():
    kingdom = {"king": "Arthur", "castle": "Camelot", "gold": 500, "army": ["knight", "archer", "catapult"]}

    show_section("KINGDOM RECORDS")
    print(kingdom)
    return kingdom


def access_information(kingdom):
    show_section("ACCESSING INFORMATION")

    details = {"King": kingdom["king"], "Army": kingdom["army"], "Queen": kingdom.get("queen")}

    for key, value in details.items():
        print(f"{key}: {value}")


def update_records(kingdom):
    show_section("UPDATING RECORDS")

    kingdom["gold"] += 250
    kingdom["queen"] = "Guinevere"
    kingdom["castle"] = "New Camelot"
    kingdom["dragon"] = True

    print(kingdom)


def delete_information(kingdom):
    show_section("DELETING INFORMATION")

    kingdom["army"] = [soldier for soldier in kingdom["army"] if soldier != "catapult"]

    kingdom.pop("queen", None)

    removed_gold = kingdom.pop("gold", 0)

    print("Gold Taken:", removed_gold)
    print(kingdom)


def search_kingdom(kingdom):
    show_section("SEARCHING KINGDOM")

    print("Does gold exist?", "gold" in kingdom)

    for title, data in {"Keys": kingdom.keys(), "Values": kingdom.values(), "Items": kingdom.items()}.items():
        print(f"\n{title}:")
        for item in data:
            print(item)


def manage_villages(kingdom):
    show_section("VILLAGES")

    kingdom["villages"] = {
        "v1": {"population": 120, "crops": ["wheat", "barley"]},
        "v2": {"population": 80, "crops": ["rice"]},
        "v3": {"population": 200, "crops": ["wheat", "corn"]},
    }

    print("Population of v2:", kingdom["villages"]["v2"]["population"])

    kingdom["villages"]["v1"]["crops"].append("sugarcane")
    kingdom["villages"]["v3"]["population"] += 50

    show_data("Updated Villages", kingdom["villages"])


def loop_records(kingdom):
    show_section("LOOPING THROUGH KINGDOM")

    for key, value in kingdom.items():
        print(f"{key} : {value}")

    show_section("VILLAGE REPORT")

    for village, details in kingdom["villages"].items():
        print(f"Village {village} has " f"{details['population']} people and grows " f"{', '.join(details['crops'])}")


def army_power():
    show_section("ARMY POWER")

    army_stats = {"knight": 50, "archer": 30, "dragon": 300}

    army_stats["archer"] += 10

    strongest = max(army_stats, key=army_stats.get)

    print("Strongest Unit:", strongest)

    army_stats.pop("knight")

    show_data("Updated Army Stats", army_stats)

    return army_stats


def kingdom_events(kingdom, army_stats):
    show_section("KINGDOM EVENTS")

    kingdom["gold"] = kingdom.get("gold", 0) + 200

    kingdom["villages"]["v1"]["population"] -= 20

    if "archer" in kingdom["army"]:
        kingdom["army"].remove("archer")

    if "dragon" in army_stats:
        army_stats["dragon"] -= 50

    kingdom["alliance"] = "Northern Empire"

    show_data("Kingdom After Events", kingdom)
    show_data("Army Stats After Events", army_stats)


def final_challenge(kingdom, army_stats):
    show_section("FINAL INTERACTIVE CHALLENGE")

    soldier = input("Enter new soldier name: ")
    strength = int(input("Enter soldier strength: "))

    army_stats[soldier] = strength

    show_data("Army Stats Updated", army_stats)

    village_name = input("\nEnter new village name: ")
    population = int(input("Enter population: "))

    crops = input("Enter crops separated by commas: ").split(",")

    kingdom["villages"][village_name] = {"population": population, "crops": [crop.strip() for crop in crops]}

    show_data("Villages After Addition", kingdom["villages"])

    remove_village = input("\nEnter village name to remove: ")

    if remove_village in kingdom["villages"]:
        del kingdom["villages"][remove_village]
        print("Village removed successfully.")
    else:
        print("Village not found.")

    show_data("Updated Kingdom", kingdom)


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
