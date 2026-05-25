def create_university():

    university = {
        "name": "Tech University",
        "principal": "Dr. Johnson",
        "funds": 100000,
        "departments": ["CSE", "ECE", "MECH"]
    }

    print("\n===== UNIVERSITY DETAILS =====")
    print(university)

    return university


def view_information(university):

    print("\n===== VIEW DETAILS =====")

    print("University:", university["name"])
    print("Departments:", university["departments"])
    print("Vice Principal:", university.get("vice_principal"))


def update_information(university):

    print("\n===== UPDATING DETAILS =====")

    university["funds"] += 50000
    university["vice_principal"] = "Dr. Smith"
    university["name"] = "Global Tech University"
    university["hostel"] = True

    print(university)


def remove_information(university):

    print("\n===== REMOVING DETAILS =====")

    if "MECH" in university["departments"]:
        university["departments"].remove("MECH")

    if "vice_principal" in university:
        del university["vice_principal"]

    removed_funds = university.pop("funds")

    print("Funds Removed:", removed_funds)

    print(university)


def search_records(university):

    print("\n===== SEARCH RECORDS =====")

    print("Funds Available:", "funds" in university)

    print("\nKeys")
    for key in university.keys():
        print(key)

    print("\nValues")
    for value in university.values():
        print(value)

    print("\nItems")
    for item in university.items():
        print(item)


def student_details(university):

    print("\n===== STUDENT DETAILS =====")

    university["students"] = {
        "student1": {
            "marks": 85,
            "subjects": ["Python", "ML"]
        },
        "student2": {
            "marks": 78,
            "subjects": ["Java"]
        },
        "student3": {
            "marks": 92,
            "subjects": ["AI", "DBMS"]
        }
    }

    print(
        "Student2 Marks:",
        university["students"]["student2"]["marks"]
    )

    university["students"]["student1"]["subjects"].append("DSA")

    university["students"]["student3"]["marks"] += 5

    print("\nUpdated Student Records")
    print(university["students"])


def report(university):

    print("\n===== UNIVERSITY REPORT =====")

    for key, value in university.items():
        print(f"{key} : {value}")

    print("\n===== STUDENT REPORT =====")

    for student, details in university["students"].items():

        marks = details["marks"]
        subjects = ", ".join(details["subjects"])

        print(
            f"{student} scored {marks} and studies {subjects}"
        )


def faculty_data():

    print("\n===== FACULTY DATA =====")

    faculty = {
        "Professor": 15,
        "Assistant Professor": 25,
        "Lab Staff": 10
    }

    faculty["Assistant Professor"] += 5

    highest = max(faculty, key=faculty.get)

    print("Highest Count:", highest)

    del faculty["Lab Staff"]

    print("\nUpdated Faculty Data")
    print(faculty)

    return faculty


def university_events(university, faculty):

    print("\n===== UNIVERSITY EVENTS =====")

    university["funds"] = university.get("funds", 0) + 20000

    university["students"]["student1"]["marks"] += 10

    if "ECE" in university["departments"]:
        university["departments"].remove("ECE")

    if "Professor" in faculty:
        faculty["Professor"] += 2

    university["partner_college"] = "National Institute"

    print("\nUpdated University")
    print(university)

    print("\nUpdated Faculty")
    print(faculty)


def final_activity(university, faculty):

    print("\n===== FINAL ACTIVITY =====")

    role = input("Enter faculty role: ")
    count = int(input("Enter count: "))

    faculty[role] = count

    print("\nFaculty Updated")
    print(faculty)

    student = input("\nEnter student name: ")
    marks = int(input("Enter marks: "))
    subjects = input(
        "Enter subjects separated by commas: "
    ).split(",")

    university["students"][student] = {
        "marks": marks,
        "subjects": [s.strip() for s in subjects]
    }

    print("\nStudents Updated")
    print(university["students"])

    remove_student = input(
        "\nEnter student name to remove: "
    )

    if remove_student in university["students"]:
        del university["students"][remove_student]
        print("Student removed")
    else:
        print("Student not found")

    print("\nFinal University Data")
    print(university)


def main():

    college = create_university()

    view_information(college)

    update_information(college)

    remove_information(college)

    search_records(college)

    student_details(college)

    report(college)

    faculty = faculty_data()

    university_events(college, faculty)

    final_activity(college, faculty)


main()