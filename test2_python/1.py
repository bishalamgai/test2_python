phoneDirectory = {}

while True:
    print("\nWELCOME TO THE GRANN'S PHONE DIRECTORY MENU\n")
    print("1. Add a record")
    print("2. Search a record")
    print("3. Change a record")
    print("4. Delete a record")
    print("5. Quit")
    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        name = input("\nEnter name: ")
        number = input("Enter your 10-digit phone number: ")
        phoneDirectory[name] = number
        print("\nRecord added")

    elif choice == 2:
        name = input("\nEnter name to search: ")
        if name in phoneDirectory:
            print(name + ": " + phoneDirectory[name])
        else:
            print("\nName not found in the phone directory")

    elif choice == 3:
        name = input("\nEnter name: ")
        if name in phoneDirectory:
            number = input("Enter new 10-digit phone number: ")
            phoneDirectory[name] = number
            print("\nRecord updated")
        else:
            print("\nName not found in the phone directory")

    elif choice == 4:
        name = input("\nEnter name: ")
        if name in phoneDirectory:
            del phoneDirectory[name]
            print("\nRecord deleted")
        else:
            print("\nName not found in the phone directory")

    elif choice == 5:
        break

    else:
        print("\nInvalid input. Please enter a valid choice.")
