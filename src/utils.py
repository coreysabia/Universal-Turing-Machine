# -*- coding: utf-8 -*-
import os
# Set the length of the tape 
# that is visable to the user
DISPLAY_TAPE_LENGTH = 10
# Set the allowed tape movements
TAPE_MOVEMENTS = {'right': 1, 'left': -1}
# For returning an empty character 
EMPTY_CHARACTER = ' '

SPEED = 0.1

def get_speed():
    return SPEED

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

def tape_visualization(string):
    return '|'.join(string[i:i + 1] for i in range(0, len(string)))

def next_position(position, direction):
    next_position = position + get_next_direction(direction)
    return next_position

def clean_list(list): # !!!!!!!!!!!!!!will not clean unknown charaters from list, should add that functionality!!!!!!!!!!!1
    # Remove empty characters from a list which 
    # might have empty characters and return it
    while '' in list:
        list.remove('')
    while ' ' in list:
        list.remove(' ')
    return list

def check_list_length(list): #skips over empty space without cleaning
    #THIS needs to return the occurences of a specific character (for each character that is found)
    count = 0
    # Return the number of occurrences
    # in a list which has no empty characters
    # First clean list with remove_empty_character
    clean = clean_list(list)
    for clean in clean:
         count += 1
    return count

def count_list_members(list): # counts the occurances of each charater in a list
    #string = stringify(list)
    char_a = 0
    char_b = 0
    char_c = 0
    char_x = 0
    char_y = 0
    char_arrow = 0
    char_left_bracket = 0
    char_right_bracket = 0
    char_unknown = 0
    for i in list:
        if (i == "a"):
            char_a += 1
        elif (i == "b"):
            char_b += 1
        elif (i == "c"):
            char_c += 1
        elif (i == "X"):
            char_x += 1
        elif (i == "Y"):
            char_y += 1
        elif (i == ">"):
            char_arrow += 1
        elif (i == "["):
            char_left_bracket += 1
        elif (i == "]"):
            char_right_bracket += 1
        else:
            char_unknown += 1
    return [char_a, char_b, char_c, char_arrow, char_x, char_y, char_left_bracket, char_right_bracket, char_unknown]

def count_specific_member(list, character): #returns a specific charaters count, pass a list and a charater you want to know how many are in the list(upper or lower case)
    total_count = count_list_members(list)
    #print(total_count)
    character = character.lower()
    #print(character)
    count_character = 0
    #print(count_character)
    if (character == "a"):
        count_character = total_count[0]
    elif(character == "b"):
        count_character = total_count[1]
    elif(character == "c"):
        count_character = total_count[2]
    elif(character == "x"):
        count_character = total_count[4]
    elif(character == "y"):
        count_character = total_count[5]
    elif(character == "["):
        count_character = total_count[6]
    elif(character == "]"):
        count_character = total_count[7]
    elif(character == ">"):
        count_character = total_count[3]
    else:
        count_character = total_count[-1]
    #print(count_character)
    return count_character