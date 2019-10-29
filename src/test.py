# -*- coding: utf-8 -*-

# Set the length of the tape 
# that is visable to the user
DISPLAY_TAPE_LENGTH = 20

# Set the allowed tape movements
TAPE_MOVEMENTS = {'right': 1, 'left': -1}

# For returning an empty character 
# when needed, maybe we should move 
# this to utils.py, not sure yet
EMPTY_CHARACTER = ' '

def tape_movements():
    return TAPE_MOVEMENTS.keys()

def get_next_direction(direction):
    return TAPE_MOVEMENTS[direction]
    
def empty_char():
    return EMPTY_CHARACTER
    
def display_tape_length():
    return DISPLAY_TAPE_LENGTH

def stringify(list):
    # Concatenate lists into string
    return str.join('', list)

def pipeify(string):
    return

def next_position(index, direction):
    next_index = index + get_next_direction(direction)
    return next_index

def clean_list(list):
    # Remove empty characters from a list which 
    # might have empty characters and return it
    while '' in list:
        list.remove('')
    return list

def check_list_length(list): #skips over empty space without cleaning
    count = 0
    # Return the number of occurrences
    # in a list which has no empty characters
    # First clean list with remove_empty_character
    clean = clean_list(list)
    for i in clean:
         count += 1
    return count

a = ["a","b","c","d"]
b = ["a","b","","c"]
c = 0

string = stringify(a)
print("Stringify test:")
print(string)
print("\n")

print("clean test:")
print(clean_list(b))
print("\n")

print("checklist length test:")
print(check_list_length(b))
print("\n")

print("next position:")
print(next_position(c, "right"))
print("\n")
