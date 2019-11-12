#!/usr/bin/env python3
# coding=utf-8

from src.utm import request_user_input, TuringMachine
from neotermcolor import cprint
import json


def main():
    #request user input and set the output of that to requested_args 
    requested_args = request_user_input()

    try:
        #get the file path of the transitions from the transitions key and read in the json file at that path
        transitions = json.loads(open(requested_args['transitions']).read())
        #init the turingmachine with the transitions, input_tape, start_state, end_state, speed and render tape length
        #using keys to get the values for everything from the requested args dict except transitions since we already init'd that
        turing_machine = TuringMachine(transitions,
                               requested_args['input_tape'],
                               requested_args['start_state'],
                               requested_args['end_state'],
                               requested_args['speed'],
                               requested_args['rendered_tape_length']).run()
        print()

        input_text = ' Input Tape: {}'.format(requested_args['input_tape'])
        output_text = ' Output: {}'.format(turing_machine)

        cprint(input_text, 110)
        cprint(output_text, 110)

        print()
        print()

    except Exception as error:
        input_tape_list = list(requested_args['input_tape'])
        input_tape_string = requested_args['input_tape']

        if error not in input_tape_list:
            input_text_2 = ' Input Tape: {}'.format(requested_args['input_tape'])
            error_text =' Oops! There was an error with your input tape! The error was caused by: {} '.format(error)

            cprint(input_text_2, 110)
            print()
            cprint(error_text, 119, 'on_red', attrs=['bold'])
            print()
            print()
        else:
            input_text_2 = ' Input Tape: {}'.format(requested_args['input_tape'])
            error_text =' Oops! There was an issue! The issue was: {} '.format(error)
            cprint(input_text_2, 110)
            print()
            cprint(error_text, 119, 'on_red', attrs=['bold'])
            print()
            print()


if __name__ == '__main__':
    main()
