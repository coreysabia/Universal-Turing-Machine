# -*- coding: utf-8 -*-

# Set the length of the tape 
# that is visable to the user
DISPLAY_TAPE_LENGTH = 20
# Set the allowed tape movements
TAPE_MOVEMENTS = {'right': 1, 'left': -1}
# For returning an empty character 
EMPTY_CHARACTER = ' '

def tape_movements():
    return TAPE_MOVEMENTS.keys()

def get_next_direction(direction):
    return TAPE_MOVEMENTS[direction]
    
def empty_char():
    return EMPTY_CHARACTER
    
def display_tape_length():
    return DISPLAY_TAPE_LENGTH

def print_system_clear():
    #print cli clear (as if you type cls or clear depending on os)
    os.system('clear')


def stringify(list):
    # Concatenate lists into string
    return str.join('', list)

def pipeify(string): #ignore for now
    return

def next_position(position, direction):
    next_position = position + get_next_direction(direction)
    return next_position

def clean_list(list):
    # Remove empty characters from a list which 
    # might have empty characters and return it
    while '' in list:
        list.remove('')
    return list

def check_list_length(list): #skips over empty space without cleaning
    #THIS needs to return the occurences of a specific character (for each character that is found)
    count = 0
    # Return the number of occurrences
    # in a list which has no empty characters
    # First clean list with remove_empty_character
    clean = clean_list(list)
    for i in clean:
         count += 1
    return count