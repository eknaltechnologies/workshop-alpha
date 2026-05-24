import json

try:
    with open("music_list.json", "r") as f:
        music_list = json.load(f)
except FileNotFoundError:
    music_list = {}

while True:
    print("Welcome to the Music List! \n1. Add Song\n2. View Songs\n3. Update Song\n4. Delete Song\n5. Search a Song\n6. Exit")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    user_choice = int(input("Please select an option (1-6): "))

    #Add a Song
    if user_choice == 1:
        song_name = input("Enter the song name: ")
        singer_name = input("Enter the singer name: ")
        album_name = input("Enter the album name: ")

        music_list[song_name] = {
            "singer": singer_name,
            "album": album_name
        }
        print(f"Song '{song_name}' added successfully.")

    #View all songs
    elif user_choice == 2:
        if not music_list:
            print("No songs available.")
        else:
            print("Music List:")
            for song, details in music_list.items():
                print(f"{song}-> Singer : {details['singer']} | Album : {details['album']}")

    #Update a Song
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

    #Delete a Song
    elif user_choice == 4:
        song_name = input("Enter the song name to delete: ")

        if song_name in music_list:
            del music_list[song_name]
            print(f"Song '{song_name}' deleted successfully.")
        else:
            print("Song not found.")

    #Search for a Song 
    elif user_choice==5:
        song_name=input('Enter song name to search: ').lower()

        found=False
        for song,details in music_list.items():
            if song_name in song.lower():
                print(f"{song}-> Singer: {details['singer']} | Album:{details['album']}")
                found=True
        if not found:
            print("No Songs found......")
    
    #Exit 
    elif user_choice ==6:
        print("Exiting Music List...")
        break
    else:
        print('Invalid choice.')

    
    json.dump(music_list, open("music_list.json", "w"), indent=4)
