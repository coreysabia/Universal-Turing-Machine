#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
from src.render import Render
from src.utils import next_position, stringify, clean_list, pipeify, check_list_length

def argument_parser():
    ap = argparse.ArgumentParser(description='A Universal Turing Machine for COMSC 330')
    ap.add_argument('-b', '--begining_state', type=str, action='store', default='q0', help='Define the begining state, default is q0')
    ap.add_argument('-e', '--ending_state', type=str, action='store', default='qdone', help='Define the ending state, default is qdone')
    ap.add_argument('-s', '--speed', type=float, action='store', default=.3, help='Define the speed of the states as they are rendered in the CLI')
    ap.add_argument('-r', '--render', action='store_true', default=False, help='Render turing machine')
    r_args = ap.add_argument_group('Required arguments')
    r_args.add_argument('-i', '--transitions', type=str, action='store', default=False, required=True, help='Define the path to the UTM Transitions, as a JSON file.')
    r_args.add_argument('-t', '--input_tape', type=str, action='store', default=False, required=True, help='Define the path to the input tape, as a txt file.')
    return ap.parse_args()

class TuringMachine(object):

    def __init__(self, transitions, input_tape, begining_state, ending_state, speed, render):
        #initialize variales
        self.transitions = transitions
        self.tape = list(input_tape)
        self.speed = speed
        self.start_state = begining_state
        self.current_state = start_state
        self.end_state = ending_state
        self.validate_transition(self.transitions, self.end_state)

    def run(self):
        #initialize position and counter
        position = 0
        count_of_steps = 0
        
        #render_output
        self.render_output(position, count_of_steps, force_render=True)

        #Add to count of steps and move position
        while self.current_state != self.end_state:
            count_of_steps += 1
            position = self.calculate_next_state(position)
            self.render_output(position, count_of_steps)
        self.render_output(position, count_of_steps, force_render=True)

        #return the string version of the tape
        return stringify(clean_list(self.tape))

    def next_state(self, position):
        if position == -1:
                self.tape.insert(0, settings.empty_char()) # INSERT EMPTY CHARACTER
                position = 0

        if position == len(self.tape):
            self.tape.append(Config.empty_character())

        action = self.transitions[self.state][self.tape[position]]
        self.tape[position] = action['write']
        self.current_state = action['nextState']
        position = next_position(position, action['move'])

        return position

    @staticmethod
    def validate_transition(transitions, end_state):
        for transition in transitions:
            for case in transitions[transition]:
                action = transitions[transition][case]
                if len(action['write']) != 1:
                    raise Exception('Invalid config! Use ONE character, instead of "{}"!'.format(action['write']))
                if action['move'] not in Config.allowed_tape_movements():
                    raise Exception('Invalid config! Use "right" or "left", not "{}"!'.format(action['move']))
                if action['nextState'] not in transitions and action['nextState'] != end_state:
                    raise Exception('Invalid config! State "{}" needs to be defined!'.format(action['nextState']))