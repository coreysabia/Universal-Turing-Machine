#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyInquirer import *
import argparse
from src.render import *
from src.utils import *


class TuringMachine(object):


    def __init__(self, transitions, input_tape, start_state, ending_state, speed, rendered_tape_length):
        #initialize variables
        self.transitions = transitions
        self.tape = list(input_tape)
        self.speed = speed
        self.start_state = start_state
        self.current_state = start_state
        self.end_state = ending_state
        self.step_number = 0
        self.position = 0
        self.dis_length = int(rendered_tape_length)
        self.validate_transition(self.transitions, self.end_state)

    def run(self):
        
        #render_output
        render(self.position, self.step_number, self.current_state, self.tape, self.speed, self.dis_length)

        #Add to step_number of steps and move position
        while self.current_state != self.end_state:
            self.step_number += 1
            self.position = self.next_state(self.position)
            render(self.position, self.step_number, self.current_state, self.tape, self.speed, self.dis_length)
        render(self.position, self.step_number, self.current_state, self.tape, self.speed, self.dis_length)

        #return the string version of the tape
        return stringify(clean_list(self.tape))

    def next_state(self, position):
        #if at the begining of the tape, (position -1) then insert an empty character to signify that
        if position == -1:
                self.tape.insert(0, empty_char()) # INSERT EMPTY CHARACTER
                position = 0

        #if at the end of the tape, (position at length of tape) then append and empty character to signify that
        if position == len(self.tape):
            self.tape.append(empty_char())

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


#def argument_parser(): #***matt will change***
#    ap = argparse.ArgumentParser(description='A Universal Turing Machine for COMSC 330')
#    ap.add_argument('-b', '--start_state', type=str, action='store', default='q0', help='Define the begining state, default is q0')
#    ap.add_argument('-e', '--ending_state', type=str, action='store', default='qdone', help='Define the ending state, default is qdone')
#    ap.add_argument('-s', '--speed', type=float, action='store', default=.3, help='Define the speed of the states as they are rendered in the CLI')
#    ap.add_argument('-l', '--rendered_tape_length', type=float, action='store', default=15, help='Define the rendered length of the tape')
#    r_args = ap.add_argument_group('Required arguments')
#    r_args.add_argument('-i', '--transitions', type=str, action='store', default=False, required=True, help='Define the path to the UTM Transitions, as a JSON file.')
#    r_args.add_argument('-t', '--input_tape', type=str, action='store', default=False, required=True, help='Define the path to the input tape, as a txt file.')

#    return ap.parse_args()

def argument_parser_pyinquirer():
    questions = [
        {
            'type' : 'input',
            'name' : 'input_tape',
            'message':'Enter the full path to the tape:'
        },
        {
            'type' : 'input',
            'name' : 'transitions',
            'message':'Enter the full path to the transitions:'
        },
        {
            'type': 'input',
            'name': 'start_state',
            'message': 'Enter the start state (default: q0):',
            'default': 'q0'
        },
        {
            'type' : 'input',
            'name' : 'end_state',
            'message':'Enter the final state (default: qdone):',
            'default': 'qdone'
        },
        {
            'type' : 'input',
            'name' : 'speed',
            'message':'Enter the desired speed of the Turing Machine:',
            'default': '0.03'
        },
        {
            'type' : 'input',
            'name' : 'rendered_tape_length',
            'message':'Enter how much of the tape you would like to see:'
        }
    ] 
    answers = prompt(questions)
    return answers