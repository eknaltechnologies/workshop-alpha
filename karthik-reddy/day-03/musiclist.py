# Music List  -- create read update delete

import json

try:
    with open("music_list.json", "r") as f:
        music_list = json.load(f)
except FileNotFoundError:
    music_list = {}

<<<<<<< HEAD

print("Welcome to the Music List!")
print("1. Add Song"
    "\n2. View Songs"
    "\n3. Update Song"
    "\n4. Delete Song"
    "\n5. Exit")

user_choice = int(input("Please select an option (1-5): "))

if user_choice == 1:
    song_name = input("Enter the song name: ")
    singer_name = input("Enter the singer name: ")
    album_name = input("Enter the album name: ")

    music_list[song_name] = {
        "singer": singer_name,
        "album": album_name
    }

    print(f"Song '{song_name}' added successfully.")


elif user_choice == 2:
    if not music_list:
        print("No songs available.")
    else:
        print("Music List:")
        for song, details in music_list.items():
            print(f"{song}: Singer: {details['singer']}, Album: {details['album']}")


elif user_choice == 3:
    song_name = input("Enter the song name to update: ")

    if song_name in music_list:
        new_singer = input("Enter new singer name: ")
        new_album = input("Enter new album name: ")

        music_list[song_name] = {
            "singer": new_singer,
            "album": new_album
        }

        print(f"Song '{song_name}' updated successfully.")
    else:
        print("Song not found.")


elif user_choice == 4:
    song_name = input("Enter the song name to delete: ")

    if song_name in music_list:
        del music_list[song_name]
        print(f"Song '{song_name}' deleted successfully.")
    else:
        print("Song not found.")


elif user_choice == 5:
    print("Exiting Music List...")


json.dump(music_list, open("music_list.json", "w"), indent=4)
=======
print("Welcome to the Music List!")

print("1. Add Song" "\n2. View Songs" "\n3. Update Song" "\n4. Delete Song" "\n5. Exit")

try:
    user_choice = int(input("Please select an option (1-5): "))

    if user_choice == 1:
        song_name = input("Enter the song name: ")
        singer_name = input("Enter the singer name: ")
        album_name = input("Enter the album name: ")

        music_list[song_name] = {"singer": singer_name, "album": album_name}

        print(f"Song '{song_name}' added successfully.")

    elif user_choice == 2:
        if not music_list:
            print("No songs available.")
        else:
            print("Music List:")
            for song, details in music_list.items():
                print(f"{song}: Singer: {details['singer']}, Album: {details['album']}")

    elif user_choice == 3:
        song_name = input("Enter the song name to update: ")

        if song_name in music_list:
            new_singer = input("Enter new singer name: ")
            new_album = input("Enter new album name: ")

            music_list[song_name] = {"singer": new_singer, "album": new_album}

            print(f"Song '{song_name}' updated successfully.")
        else:
            print("Song not found.")

    elif user_choice == 4:
        song_name = input("Enter the song name to delete: ")

        if song_name in music_list:
            del music_list[song_name]
            print(f"Song '{song_name}' deleted successfully.")
        else:
            print("Song not found.")

    elif user_choice == 5:
        print("Exiting Music List...")

    else:
        print("Invalid choice.")

    with open("music_list.json", "w") as f:
        json.dump(music_list, f, indent=4)

except ValueError:
    print("Please enter numbers only.")
>>>>>>> 5dcca8c9c95548e30f6c7eb9d95c27c0d705e7ff
