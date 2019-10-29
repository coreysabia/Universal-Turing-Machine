# -*- coding: utf-8 -*-

# Set the length of the tape 
# that is visable to the user
USER_VISIBLE_TAPE_LENGTH = 20
# Set the allowed tape movements
ALLOWED_TAPE_MOVEMENTS = {'right': 1, 'left': -1}
# For returning an empty character 
# when needed
EMPTY_CHARACTER = ' '


def allowed_tape_movements():
    return settings.ALLOWED_TAPE_MOVEMENTS.keys()


def tape_movement_for(direction):
    return settings.ALLOWED_TAPE_MOVEMENTS[direction]


def empty_char():
    return settings.EMPTY_CHARACTER


def user_visible_tape_length():
    return settings.USER_VISIBLE_TAPE_LENGTH


def stringify(to_stringify):
    # Concatenate lists into string
    return


def pipeify(string):
    return


def next_index(index, direction):
    next_index = index + tape_movement_for(direction)
    return next_index


def remove_empty_character(non_empty_list):
    # Remove empty characters from a list which 
    # might have empty characters and return it
    return


def count_occurrences(in_list):
    # Return the number of occurrences
    # in a list which has no empty characters
    # First clean list with remove_empty_character 
   return