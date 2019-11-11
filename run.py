#!/usr/bin/env python3
# coding=utf-8

from src.utm import request_user_input, TuringMachine
from neotermcolor import cprint
import json


def main():
    requested_args = request_user_input()
    try:
        transitions = json.loads(open(requested_args['transitions']).read())
        turing_machine = TuringMachine(transitions,
                               requested_args['input_tape'],
                               requested_args['start_state'],
                               requested_args['end_state'],
                               requested_args['speed'],
                               requested_args['rendered_tape_length']).run()
        print()
        print('Input: {}'.format(requested_args['input_tape']))
        print('Output: {}'.format(turing_machine))
    except Exception as error:
        error_text =' Something went wrong! Issue: {} '.format(error)
        cprint(error_text, 119, 'on_red', attrs=['bold'])

        print()
        print()

if __name__ == '__main__':
    main()