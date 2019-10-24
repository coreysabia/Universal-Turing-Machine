# -*- coding: utf-8 -*-

# Set the length of the tape 
# that is visable to the user
USER_VISIBLE_TAPE_LENGTH = 20

# Set the allowed tape movements
ALLOWED_TAPE_MOVEMENTS = {'right': 1, 'left': -1}

# For returning an empty character 
# when needed, maybe we should move 
# this to utils.py, not sure yet
EMPTY_CHARACTER = ' '

class Settings:
    @staticmethod
    def allowed_tape_movements():
        return ALLOWED_TAPE_MOVEMENTS.keys()

    @staticmethod
    def tape_movement_for(direction):
        return ALLOWED_TAPE_MOVEMENTS[direction]

    @staticmethod
    def empty_char():
        return EMPTY_CHARACTER

    @staticmethod
    def user_visible_tape_length():
        return USER_VISIBLE_TAPE_LENGTH