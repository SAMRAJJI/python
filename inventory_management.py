inventory = {}

def add():
    item = input("Enter the item name to add: ")
    copies = int(input("Enter the quantity: "))
    if item in inventory:
        inventory[item] += copies
    else:
        inventory[item] = copies
    print("Item added successfully.\n", inventory)

def update():
    item = input("Enter the item name to be updated: ")
    if item in inventory:
        copies = int(input("Enter the new quantity: "))
        inventory[item] += copies
        print("Given item is updated successfully.\n", inventory)
    else:
        print("This item does not exist.")

def remove():
    item = input("Enter the item name to be removed: ")
    if item in inventory:
        del inventory[item]
        print("Given item is removed successfully.\n", inventory)
    else:
        print("This item does not exist.")

def display():
    print("The items in the inventory so for:\n", inventory)

def exiting():
    print("Exiting Inventory Management.")
print("INVENTORY MANAGEMENT")
while True:
    choice = int(input("\n1. Add\n2. Update\n3. Remove\n4. Display\n5. Exit\nEnter your choice number: "))
    if choice == 1:
        add()
    elif choice == 2:
        update()
    elif choice == 3:
        remove()
    elif choice == 4:
        display()
    elif choice == 5:
        exiting()
        break
    else:
        print("Invalid choice.")
        Print("The inventory at last:\n", inventory)
