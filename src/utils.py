# -*- coding: utf-8 -*-
import os
from platform import system
# Set the length of the tape 
# that is visable to the user
DISPLAY_TAPE_LENGTH = 10
# Set the allowed tape movements
TAPE_MOVEMENTS = {'right': 1, 'left': -1}
# For returning an empty character 
EMPTY_CHARACTER = ' '

# tape movement keys
def tape_movements():
    return TAPE_MOVEMENTS.keys()

# .lowercase() whaterver the direction is to work with our tape_movements keys
def get_next_direction(direction):
    return TAPE_MOVEMENTS[direction]

# takes current position and calls next direction function to get next position
def next_position(position, direction):
    next_position = position + get_next_direction(direction)
    return next_position

# allows for empty character    
def empty_char():
    return EMPTY_CHARACTER

# returns tape length data field for render  
def display_tape_length():
    return DISPLAY_TAPE_LENGTH

# takes a list as input and returns a string
def stringify(list):
    # Concatenate lists into string
    return str.join('', list)

def tape_visualization(string):
    return ' '.join(string[i:i + 1] for i in range(0, len(string)))

# removes spaces and blanks from list
# will not clean unknown charaters from list
def clean_list(list, end_char, pos1, pos2):
    # Remove empty characters from a list which 
    # might have empty characters and return it
    #list = list((len(self.tape) + 1 ))
    #while end_char in list:
    #list.remove(end_char)
    #list.pop()
    #list.pop(0)
    
    while '' in list:
        list.remove('')
    while ' ' in list:
        list.remove(' ')
    while end_char in list:
        list.remove(end_char)
        
    #list.pop() =
    #ΔΔ0ΔΔΔΔΔ
    #nothing =
    #ΔΔ0ΔΔΔΔΔΔ
    #list.pop(0) =
    #Δ0ΔΔΔΔΔΔ

    if pos1 == 1:
        tape_minus_first = clean_first(list)
        list = tape_minus_first
    if pos2 == 1:
        tape_minus_ends = clean_last(tape_minus_first)
        list = tape_minus_ends

    return list

def clean_first(list):
    list.pop(0)
    return list

def clean_last(list):
    list.pop()
    return list

# returns the length of the given list
def check_list_length(list, end_char):
    #THIS needs to return the occurences of a specific character (for each character that is found)
    count = 0
    # Return the number of occurrences
    # in a list which has no empty characters
    # First clean list with remove_empty_character
    clean = clean_list(list, end_char)
    for clean in clean:
         count += 1
    return count
 
# counts the occurances of each charater in a list
def count_list_members(list):
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

# returns a specific charaters count, pass a list and a charater you want to know how many are in the list(upper or lower case)
def count_specific_member(list, character):
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

# counts all of the charaters in a list using json format to return
def count_list_members_json(tape):
    tape_data = {}
    for character in tape:
        if character in tape:
            tape_data[character] += 1
        else:
            tape_data[character] = 1
    return tape_data

# calls the previous function to return a specific value in the json 
# takes in tape data and a charater
def count_specific_member_json(tape, character):
    tape_data = count_list_members_json(tape)
    char_count = tape_data[character]
    return char_count

# System call to determine the function needed to clear the terminal
def os_check():
    #os_name2 = os.name
    os_name = system() 
    #print(os_name)
    #print(os_name2)
    return os_name

# cli clear for unix
def print_system_clear():
    #print cli clear unix(as if you type cls or clear depending on os)
    os.system('clear')

# cli clear for windows
def print_system_cls():
    #print cli cls for windows
    os.system('cls')

#this function takes all of a specific character and converts it to a space
#def json_cleaner(character, json):
#    print(json)
#    for character in json[character]:
#        json[character] = " "
    #for character in json["writeValue"]:
        #character = " "
#    print(json)
#    return json

# function that encodes a transition
# links each part of the transition to a string of 0's and 1's
# tests all parts of the transtion to assign it a common value
# returns the encoding in the proper format (current state, readhead)-->(next state, write, move direction)
def transition_encode(writeValue, nextState, moveTo, currentState, readHead):
    #pass in current transition from UTM run and return an int string of 0's and 1's
    #Extra
    char_none = "1111"
    char_error = "XXXX"
    char_delta = "1001"

    #states    
    char_q0 = "0000"
    char_q1 = "0001"
    char_q2 = "0010"
    char_q3 = "0011"
    char_q4 = "0100"
    char_q5 = "0101"
    char_q6 = "0111"
    char_q7 = "1000"
    char_q8 = "1001"
    char_q9 = "1010"
    char_q10 = "1011"
    char_qdone = "1100"
    
    #tape charaters
    char_X = "0000"
    char_Y = "0001"
    char_a = "0010"
    char_b = "0011"
    char_c = "0100"
    char_left_bracket = "0101"
    char_right_bracket = "0110"
    char_arrow = "0111"
    char_space = "1000"
    char_zero = "1001"
    char_one = "1010"

    #directions
    char_L = "0"
    char_R = "1"

    #end values
    current_state = ''
    read_head = ''
    next_state = ''
    write = ''
    move = ''

    #current state
    if(currentState == 'q0'):
        current_state = char_q0
    elif(currentState == 'q1'):
        current_state = char_q1
    elif(currentState == 'q2'):
        current_state = char_q2
    elif(currentState == 'q3'):
        current_state = char_q3
    elif(currentState == 'q4'):
        current_state = char_q4
    elif(currentState == 'q5'):
        current_state = char_q5
    elif(currentState == 'q6'):
        current_state = char_q6
    elif(currentState == 'q7'):
        current_state = char_q7
    elif(currentState == 'q8'):
        current_state = char_q8
    elif(currentState == 'q9'):
        current_state = char_q9
    elif(currentState == 'q10'):
        current_state = char_q10
    elif(currentState == 'qdone'):
        current_state = char_qdone
    elif(currentState == 'None'):
        current_state = char_none
    else:
        current_state = char_error

    #next state
    if(nextState == 'q0'):
        next_state = char_q0
    elif(nextState == 'q1'):
        next_state = char_q1
    elif(nextState == 'q2'):
        next_state = char_q2
    elif(nextState == 'q3'):
        next_state = char_q3
    elif(nextState == 'q4'):
        next_state = char_q4
    elif(nextState == 'q5'):
        next_state = char_q5
    elif(nextState == 'q6'):
        next_state = char_q6
    elif(nextState == 'q7'):
        next_state = char_q7
    elif(nextState == 'q8'):
        next_state = char_q8
    elif(nextState == 'q9'):
        next_state = char_q9
    elif(nextState == 'None'):
        next_state = char_none
    elif(nextState == 'q10'):
        next_state = char_q10
    elif(nextState == 'qdone'):
        next_state = char_qdone
    else:
        next_state = char_error
    
    #readhead
    if(readHead == 'X'):
        read_head = char_X
    elif(readHead == 'Y'):
        read_head = char_Y
    elif(readHead == 'a'):
        read_head = char_a
    elif(readHead == 'b'):
        read_head = char_b
    elif(readHead == 'c'):
        read_head = char_c
    elif(readHead == '>'):
        read_head = char_arrow
    elif(readHead == '['):
        read_head = char_left_bracket
    elif(readHead == ']'):
        read_head = char_right_bracket
    elif(readHead == ' '):
        read_head = char_space
    elif(readHead == 'None'):
        read_head = char_none
    elif(readHead == 'Δ'):
        read_head = char_delta
    elif(readHead == '0'):
        read_head == char_zero
    elif(readHead == '1'):
        read_head = char_one 
    else:
        read_head = char_error



    #write
    if(writeValue == 'a'):
        write = char_a
    elif(writeValue == 'b'):
        write = char_b
    elif(writeValue == 'c'):
        write = char_c
    elif(writeValue == 'None'):
        write = char_none
    elif(writeValue == ' '):
        write = char_space
    elif(writeValue == 'Δ'):
        write = char_delta
    elif(writeValue == '0'):
        write == char_zero
    elif(writeValue == '1'):
        write = char_one 
    else:
        write = char_error
    
    
    #direction
    if(moveTo == 'right'):
        move = char_R
    elif(moveTo == 'left'):
        move = char_L
    elif(moveTo == ' '):
        move = char_space
    elif(moveTo == 'None'):
        move = char_none
    else:
        move = char_error

    #(q1, a)-->(q2, b, L)
    #(current_state, read_head)-->(next_state, write, move)


    #append all values and return
    return current_state + read_head + next_state + write + move