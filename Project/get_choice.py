def get_choice(prompt):
    choice = input(prompt).strip().lower()
    if choice == '':
        return 'yes'
    elif choice.startswith('y'):
        return 'yes'
    elif choice.startswith('n'):
        return 'no'
    else:
        return choice