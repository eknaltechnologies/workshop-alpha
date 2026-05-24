import json

try:
    with open("library.json", "r") as f:
        library = json.load(f)
except FileNotFoundError:
    library = {"books": {}, "members": {}, "issued_books": {}}

print("Welcome to the Library Management System")
print("1. Add book" "\n2. View library" "\n3. Update book" "\n4. Delete book" "\n5. Issue book" "\n6. View issued books" "\n7. Exit")

user_choice = int(input("Please select an option (1-7): "))

# 1. Add book
if user_choice == 1:
    book_name = input("Enter the book name: ")
    book_author = input("Enter the book author: ")
    book_price = float(input("Enter the book price: "))

    library["books"][book_name] = {"author": book_author, "price": book_price}
    print(f"Book '{book_name}' added successfully.")

# 2. View library
elif user_choice == 2:
    if not library["books"]:
        print("No books available.")
    else:
        print("Books list:")
        for name, details in library["books"].items():
            print(f"{name} — Author: {details['author']}, Price: {details['price']}")

# 3. Update book
elif user_choice == 3:
    book_name = input("Enter the book name to update: ")
    if book_name in library["books"]:
        new_author = input("Enter new author name: ")
        new_price = float(input("Enter new price: "))
        library["books"][book_name]["author"] = new_author  # variable, not string
        library["books"][book_name]["price"] = new_price
        print(f"Book '{book_name}' updated successfully.")
    else:
        print("Book not found.")

# 4. Delete book
elif user_choice == 4:
    book_name = input("Enter the book name to delete: ")
    if book_name in library["books"]:
        del library["books"][book_name]
        print(f"Book '{book_name}' deleted successfully.")
    else:
        print("Book not found.")

# 5. Issue book
elif user_choice == 5:
    student_name = input("Enter student name: ")
    issued_book = input("Enter book name to issue: ")
    if issued_book in library["books"]:
        library["issued_books"][student_name] = issued_book
        print(f"Book '{issued_book}' issued to {student_name}.")
    else:
        print("Book not available.")

# 6. View issued books
elif user_choice == 6:
    if not library["issued_books"]:
        print("No books issued.")
    else:
        print("Issued Books:")
        for student, book in library["issued_books"].items():
            print(f"{student} -> {book}")

# 7. Exit
elif user_choice == 7:
    print("Thank you for using the Library Management System!")

else:
    print("Invalid option.")

# Save to file
with open("library.json", "w") as f:
    json.dump(library, f, indent=4)
