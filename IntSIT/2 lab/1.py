"""Show menu."""
import os


def main():
    """Start the main function."""
    while True:
        key = show_menu()
        if key == 1:
            load_patterns()
        elif key == 2:
            calc_output()
        elif key == 3:
            educate()
        elif key == 4:
            set_structure()
        elif key == 5:
            break

    print('\nProgram Exit.')


def show_menu():
    """Display menu in console and requests key."""
    print('Menu:')
    print('1: Load patterns')
    print('2: Calc output')
    print('3: Educate')
    print('4: Set structure')
    print('5: Exit')
    print()
    key = int(input('Select menu item: '))
    os.system("cls")
    return key


def load_patterns():
    """Load templates from file."""
    print('Success load_patterns\n')


def calc_output():
    """Calculate neural network output."""
    print('Success calc_output\n')


def educate():
    """Training neural network."""
    print('Success educate\n')


def set_structure():
    """Change structure INS."""
    print('Success set_structure\n')


if __name__ == '__main__':
    main()
