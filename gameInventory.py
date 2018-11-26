# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification


# Displays the inventory.


def display_inventory(inventory):
    print("Inventory:")
    # Variable to store sum (Not using here the sum() function)
    sum_value = 0
    for key, value in inventory.items():
        print(str(value) + " " + key)
        sum_value += value
    print("Total number of items: " + str(sum_value))

# Adds to the inventory dictionary a list of items from added_items.


def add_to_inventory(inventory, added_items):
    for i in added_items:
        if i in inventory:
            inventory[i] += 1
        else:
            inventory.update({i: 1})
    return inventory


# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order


def print_table(inventory, order=None):
    # The length og the longest string
    max_length = max(len(i) for i in inventory)
    print("Inventory:\n")
    print("count".rjust(7) + "item name".rjust(13))
    print("-"*(max_length + 11))

    if order == None:
        for key, value in inventory.items():
            print(str(value).rjust(7) + key.rjust(max_length + 4))
    elif order == "count,desc":
        desc_inventory = sorted(inventory, key=inventory.get, reverse=True)
        for key in desc_inventory:
            print(str(inventory[key]).rjust(7) + key.rjust(max_length + 4))
    elif order == "count,asc":
        asc_inventory = sorted(inventory, key=inventory.get)
        for key in asc_inventory:
            print(str(inventory[key]).rjust(7) + key.rjust(max_length + 4))

    print("-"*(max_length + 11))
    print("Total number of items: " + str(sum(inventory.values())))


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="test_inventory.csv"):
    read_file = open(filename, "r")
    content = read_file.read()
    list_of_content = [str(item) for item in content.split(",")]
    add_to_inventory(inventory, list_of_content)
    read_file.close()
    return inventory


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    list_to_export = []
    for key, value in inventory.items():
        list_to_export.extend([key] * value)
    list_to_export = ",".join(list_to_export)
    write_file = open(filename, "w")
    write_file.write(list_to_export)
    write_file.close()


inv = {"arrow": 12, "gold coin": 42, "rope": 1, "torch": 6, "dagger": 1}
dragon_loot = ["gold coin", "dagger", "gold coin", "gold coin", "ruby"]
inv = add_to_inventory(inv, dragon_loot)
import_inventory(inv)
print_table(inv, "count,desc")
export_inventory(inv)
