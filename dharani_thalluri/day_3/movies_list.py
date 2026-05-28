# Movie List System
import json

try:
    with open("movie_list.json", "r") as f:
        movie_list = json.load(f)
except FileNotFoundError:
    movie_list = {"movies": {}}

while True:
    print(
        "===== Movie List System ====="
        "\n 1. Add Movie"
        "\n 2. View Movies"
        "\n 3. Update Movie"
        "\n 4. Delete Movie"
        "\n 5. Search Movie"
        "\n 6. Highest Rated Movie"
        "\n 7. Genre Wise Movies"
        "\n 8. Total Movies"
        "\n 9. Exit"
    )

    user_choice = int(input("Enter your choice (1-9): "))

    # ADD MOVIE
    if user_choice == 1:
        movie_name = input("Enter movie name: ")
        genre = input("Enter genre: ")
        rating = float(input("Enter movie rating: "))
        year = int(input("Enter release year: "))

        movie_list["movies"][movie_name] = {
            "genre": genre,
            "rating": rating,
            "year": year,
        }

        print(f"Movie '{movie_name}' added successfully!")

    # VIEW MOVIES
    elif user_choice == 2:
        if not movie_list["movies"]:
            print("No movies found.")

        else:
            print("\nMovie List:")

            for name, details in movie_list["movies"].items():
                print(f"Movie Name : {name}")
                print(f"Genre      : {details['genre']}")
                print(f"Rating     : {details['rating']}")
                print(f"Year       : {details['year']}")
                print("--------------------------")

    # UPDATE MOVIE
    elif user_choice == 3:
        movie_name = input("Enter movie name to update: ")

        if movie_name in movie_list["movies"]:
            new_genre = input("Enter new genre: ")
            new_rating = float(input("Enter new rating: "))
            new_year = int(input("Enter new release year: "))

            movie_list["movies"][movie_name]["genre"] = new_genre
            movie_list["movies"][movie_name]["rating"] = new_rating
            movie_list["movies"][movie_name]["year"] = new_year

            print("Movie updated successfully!")

        else:
            print("Movie not found.")

    # DELETE MOVIE
    elif user_choice == 4:
        movie_name = input("Enter movie name to delete: ")

        if movie_name in movie_list["movies"]:
            del movie_list["movies"][movie_name]

            print("Movie deleted successfully!")

        else:
            print("Movie not found.")

    # SEARCH MOVIE
    elif user_choice == 5:
        movie_name = input("Enter movie name to search: ")

        if movie_name in movie_list["movies"]:
            details = movie_list["movies"][movie_name]

            print("\nMovie Found:")
            print(f"Genre  : {details['genre']}")
            print(f"Rating : {details['rating']}")
            print(f"Year   : {details['year']}")

        else:
            print("Movie not found.")

    # HIGHEST RATED MOVIE
    elif user_choice == 6:
        if not movie_list["movies"]:
            print("No movies found.")

        else:
            highest_movie = None
            highest_rating = 0

            for name, details in movie_list["movies"].items():
                if details["rating"] > highest_rating:
                    highest_rating = details["rating"]
                    highest_movie = name

            print("\nHighest Rated Movie:")
            print(f"{highest_movie} - Rating: {highest_rating}")

    # GENRE WISE MOVIES
    elif user_choice == 7:
        genre_name = input("Enter genre to search: ")

        found = False

        print(f"\nMovies in Genre '{genre_name}':")

        for name, details in movie_list["movies"].items():
            if details["genre"].lower() == genre_name.lower():
                print(f"{name} ({details['year']}) - Rating: {details['rating']}")

                found = True

        if not found:
            print("No movies found in this genre.")

    # TOTAL MOVIES
    elif user_choice == 8:
        total_movies = len(movie_list["movies"])

        print(f"Total Movies = {total_movies}")

    # EXIT
    elif user_choice == 9:
        with open("movie_list.json", "w") as f:
            json.dump(movie_list, f, indent=4)

        print("Movie data saved successfully!")
        print("Exiting Movie List System...")

        break

    else:
        print("Invalid choice. Please try again.")

    # Save data after every operation
    with open("movie_list.json", "w") as f:
        json.dump(movie_list, f, indent=4)
