print("Shopping List")

shopping_list = []

while True:
    print("\nPlease select the action number you want to do:")
    print("1) Add to list")
    print("2) Add many at once")
    print("3) Remove from list")
    print("4) Show the list")
    print("5) Exit from the app")

    action_str = input("Your choice (1-5): ").strip()
    if not action_str.isdigit():
        print("Please enter a number between 1-5.")
        continue

    action = int(action_str)

    if action == 1:
        while True:
            item = input("Please enter your item: ").strip()
            if not item:
                print("Empty item is not allowed.")
                continue
            if item in shopping_list:
                print("Item already exists, try another one.")
                continue
            shopping_list.append(item)
            print("Item added successfully.")
            break
        continue

    elif action == 2:
        count_str = input("How many items to add: ").strip()
        if not (count_str.isdigit() and int(count_str) > 0):
            print("Please enter a positive number.")
            continue
        count = int(count_str)

        for _ in range(count):
            item = input("Please enter your item: ").strip()
            if item and item not in shopping_list:
                shopping_list.append(item)
                print(item, "added successfully.")
            else:
                print("Empty or duplicate item, skipped.")
        continue

    elif action == 3:
        if not shopping_list:
            print("List is empty, nothing to remove.")
            continue
        item = input("Enter the item to remove: ").strip()
        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "removed successfully.")
        else:
            print("Item not found.")
        continue

    elif action == 4:
        if shopping_list:
            print("Your list:", ", ".join(shopping_list))
        else:
            print("Your list is empty.")
        continue

    elif action == 5:
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose between 1-5.")
        continue