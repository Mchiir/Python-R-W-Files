def check_existance(lines, item, file_path):
    item_exists = False
    for line in lines:
        if item.strip() == line.strip():
            item_exists = True
            break
    
    if item_exists:
        print("The item already exists!")
    elif item:
        with open(file_path, 'a') as file:
            file.write('\n' + item)
        print("Item added successfully\nItem added: {}".format(item))
    else:
        print("No item entered.")