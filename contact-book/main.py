print("Contact Book")

people = []

while True:
    print("1: Add contact")
    print("2: Remove contact")
    print("3: Show all")
    print("4: Exit")
    action = input("Please select the action you want to perform: ")

    if action not in ["1", "2", "3", "4"]:
        print("Please choose between 1-4!")
        continue
    else:
        if action == "1":
            while True:
                name = input("Name: ").strip()
                phone_str = input("Phone: ").strip()
                email = input("Email: ").strip()

                if not phone_str.isdigit():
                    print("Please enter a numerical phone number!")
                    continue
                else:
                    phone = int(phone_str)

                    person = {
                        "name": name,
                        "phone": phone,
                        "email": email
                    }

                    people.append(person)

                    print("Person added successfully.")
                    break
        if action == "2":
            if len(people) == 0:
                print("List is empty.")
                continue
            else:
                name = input("Please enter the name you want to remove: ").strip()

                found = False

                for p in people:
                    if p["name"].lower() == name.lower():
                        print("Contact found: ", p["name"])
                        people.remove(p)
                        print("Contact removed successfully.")

                        found = True
                        break

                if not found:
                    print("There is no such contact!")
                    continue
        if action == "3":
            for p in people:
                print("-----")
                print("Name: ", p["name"])
                print("Phone: ", p["phone"])
                print("Email: ", p["email"])
                print("-----")

            continue

        if action == "4":
            print("Goodbye!")
            break