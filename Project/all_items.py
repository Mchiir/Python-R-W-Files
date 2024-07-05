def all_inventories(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        print("All inventories:")
        print(content)