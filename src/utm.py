#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import sys
import os

from PyInquirer import style_from_dict, Token, prompt, Separator
from examples import custom_style_1

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from render import *
from utils import *

class TuringMachine(object):


    def __init__(self, transitions, input_tape, start_state, ending_state, end_markings, speed, rendered_tape_length):
        #initialize variables
        self.end_char = end_markings
        self.transitions = transitions
        self.tape = list(input_tape)
        self.speed = float(speed)
        self.start_state = start_state
        self.current_state = start_state
        self.end_state = ending_state
        self.step_number = 0
        self.position = 0
        self.dis_length = int(rendered_tape_length)
        self.validate_transition(self.transitions, self.end_state)
        self.pos1 = 0
        self.pos2 = 0


    def run(self):
        
        #render_output
        #render_init(self.position, self.step_number, self.current_state, self.tape, self.speed, self.dis_length)
        render(self.position, self.step_number, self.current_state, self.tape, self.speed, self.dis_length, self.transitions, self.end_state, self.end_char)
        #Add to step_number of steps and move position
        while self.current_state != self.end_state:
            self.step_number += 1
            self.position = self.next_state(self.position)
            render(self.position, self.step_number, self.current_state, self.tape, self.speed, self.dis_length, self.transitions, self.end_state, self.end_char)
        # render final position
        render_final(self.position, self.step_number, self.current_state, self.tape, self.speed, self.dis_length, self.transitions, self.end_state, self.end_char)
        #return the string version of the tape
        return stringify(clean_list(self.tape, self.end_char, self.pos1, self.pos2))

    def next_state(self, position):
        #if at the begining of the tape, (position -1) then insert an empty character to signify that
        if position == -1:
            self.tape.insert(0, self.end_char) # INSERT END CHARACTER
            position = 0
            self.pos1 = 1
            

        #if at the end of the tape, (position at length of tape) then append and empty character to signify that
        if position == len(self.tape):
            self.tape.append(self.end_char)
            self.pos2 = 1

        #read_head = self.tape[position]

#position == len(self.tape) and 
        #if read_head == self.end_char:
        #    position = next_position(position, "left")
        #    print("THIS DID A THING")
        #    return position

        #elif position == 0 and read_head == self.end_char:
        #    position = next_position(position, "right")
        #    print("THIS DID A THING TOO")
        #    return position

        #else:
        #    print("THIS DIDNT DO A THING")
        # set an object (action) to json object from transitions 
        action = self.transitions[self.current_state][self.tape[position]]
        self.tape[position] = action['writeValue']
        self.current_state = action['nextState']
        position = next_position(position, action['moveTo'])
        return position


    @staticmethod
    def validate_transition(transitions, end_state):
        for transition in transitions:
            for case in transitions[transition]:
                action = transitions[transition][case]
                if len(action['writeValue']) != 1:
                    raise Exception('Invalid config! Use ONE character, instead of "{}"!'.format(action['writeValue']))
                if action['moveTo'] not in tape_movements():
                    raise Exception('Invalid config! Use "right" or "left", not "{}"!'.format(action['moveTo']))
                if action['nextState'] not in transitions and action['nextState'] != end_state:
                    raise Exception('Invalid config! State "{}" needs to be defined!'.format(action['nextState']))


def request_user_input():
    questions = [
        {
            'type' : 'input',
            'name' : 'input_tape',
            'message':'Enter the input tape:',
            'validate': lambda answer: 'ERROR: You must input a tape!' \
                if len(answer) == 0 else True
        },
        {
            'type' : 'input',
            'name' : 'transitions',
            'message':'Enter the path to the transitions file:',
            'validate': lambda answer: 'ERROR: You must input a path the file!' \
                if len(answer) == 0 else True
        },
        {
            'type': 'input',
            'name': 'start_state',
            'message': 'Enter the start state (default: q0):',
            'default': 'q1',
            'validate': lambda answer: 'ERROR: You must input a starting state!' \
                if len(answer) == 0 else True
        },
        {
            'type' : 'input',
            'name' : 'end_state',
            'message':'Enter the final state (default: qdone):',
            'default': 'q2',
            'validate': lambda answer: 'ERROR: You must input a final state!' \
                if len(answer) == 0 else True
        },
        {
            'type' : 'input',
            'name' : 'end_markings',
            'message':'Enter the character for end markings (default: " "):',
            'default': 'Δ',
            'validate': lambda answer: 'ERROR: You must input an end marker!' \
                if len(answer) == 0 else True
        },
        {
            'type' : 'input',
            'name' : 'speed',
            'message':'Enter the speed of the output (default: 0.03):',
            'default': '0.03',
            'validate': lambda answer: 'ERROR: You must input a speed!' \
                if len(answer) == 0 else True
        },
        {
            'type' : 'input',
            'name' : 'rendered_tape_length',
            'message':'Enter how much of the tape you would like to see (default: 15):',
            'default': '15',
            'validate': lambda answer: 'ERROR: You must input a length!' \
                if len(answer) == 0 else True
        }
    ] 
    answers = prompt(questions, style=custom_style_1)
    return answers













#end state to favorable state??
#encoding of transactions
# print what the given transactions are -- print what the encoding transactions are after it finishes running
# maybe encode off of the transition q1,q2,q3?
#if index goes out of bounds?
#after 10 minutes, ask the user if their thing is nondetermanistic