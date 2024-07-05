import all_items
import existance
import get_choice

file_path = "F:/ALL/ThinkCyber/Python/Crucial_codes/io/inventory.txt"

def add_items():
    # Display all inventories
    all_items.all_inventories(file_path)

    choice = get_choice.get_choice("Do you want to add inventories (yes/no): ")
    while choice == 'yes':
        item = input("Enter the item: ").strip()
        
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Check if the item already exists
        existance.check_existance(lines, item, file_path)

        choice = get_choice.get_choice("Do you want to add another item? (yes/no): ")

    print("Program ended.")

add_items()