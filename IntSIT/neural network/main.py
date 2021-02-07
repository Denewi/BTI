"""Neural network recognizes symbols."""
from random import uniform
import numpy as np

# Constants
N_LAYER = 3  # Number layers
N_MAX_NEURON = 30  # Max number of neurons per layer (zero layer)
N_MIN_NEURON = 4  # Min number of neurons per layer (output layer)
N_TEMPLATE = 10  # Number of templates
N_SPEED = 1  # Ratio of speed of learning
E_THRESHOLD = 0.01  # Training error threshold value
N_ITERATION = 10000  # Max number of iterations in training cycle

my_patterns = [[0]*N_MAX_NEURON for i in range(N_TEMPLATE)]


def main():
    """Start the main function."""
    key = None
    while key != '5':
        key = show_menu()
        if key == '1':
            load_patterns()
        elif key == '2':
            calc_pattern()
        elif key == '3':
            educate()
        elif key == '4':
            set_struc()
        elif key != '5':
            print('Wround item!')


def show_menu():
    """Display menu in console and requests key."""
    print('\nMenu:')
    print('1: Load patterns')
    print('2: Calc output')
    print('3: Educate')
    print('4: Set structure')
    print('5: Exit')
    key = input('Select menu item: ')
    return key


def load_patterns():
    """Load templates from file."""
    with open('patterns.txt', 'r') as input_file:
        key = int(input_file.read(1))
        while key:
            for pattern_char in range(N_MAX_NEURON):
                char = input_file.read(1)
                if (not char == '\n') and (not char == ' '):
                    my_patterns[key][pattern_char] = int(char)
                    print(my_patterns)


def calc_pattern():
    """Calculate neural network output."""
    pass


def educate():
    """Training neural network."""
    pass


def set_struc():
    """Change structure INS."""
    pass


if __name__ == '__main__':
    main()
