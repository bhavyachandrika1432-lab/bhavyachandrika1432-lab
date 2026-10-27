dictionary = {}
while True:
    print("\n----- DICTIONARY -----")
    print("1. Add Word")
    print("2. Search for Meaning")
    print("3. Display All Words")
    print("4. Update Meaning")
    print("5. Delete Word")
    print("6. Exit")
    choice = input("Enter your choice: ")
    # 1. Add Word
    if choice == "1":
        word = input("Enter word: ").strip().lower()
        if word == "":
            print("Word cannot be empty.")
        elif word in dictionary:
            print("Word already exists.")
        else:
            meaning = input("Enter meaning: ").strip()
            if meaning == "":
                print("Meaning cannot be empty.")
            else:
                dictionary[word] = meaning
                print("Word added successfully.")
    # 2. Search for Meaning
    elif choice == "2":
        word = input("Enter word to search: ").strip().lower()
        if word in dictionary:
            print("Meaning:", dictionary[word])
        else:
            print("Word not found.")
    # 3. Display All Words
    elif choice == "3":
        if len(dictionary) == 0:
            print("Dictionary is empty.")
        else:
            print("\nAll Words and Meanings:")

            for word, meaning in dictionary.items():
                print(word, ":", meaning)
    # 4. Update Meaning
    elif choice == "4":
        word = input("Enter word to update: ").strip().lower()
        if word in dictionary:
            new_meaning = input("Enter new meaning: ").strip()

            if new_meaning == "":
                print("Meaning cannot be empty.")
            else:
                dictionary[word] = new_meaning
                print("Meaning updated successfully.")
                print("Updated meaning:", dictionary[word])
        else:
            print("Word not found.")
    # 5. Delete Word
    elif choice == "5":
        word = input("Enter word to delete: ").strip().lower()

        if word in dictionary:
            del dictionary[word]
            print("Word deleted successfully.")
        else:
            print("Word not found.")
    # 6. Exit
    elif choice == "6":
        print("Exiting Dictionary...")
        break
    # Invalid choice
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")