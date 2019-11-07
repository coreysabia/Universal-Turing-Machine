from src.utils import *
from src.utm import *
import os
import time

#IGNORE THIS FILE FOR NOW PLEASE

def render(position, step_number, current_state, tape, speed, dis_length):
    # Clear screen to wipe previous state
    print_system_clear()
    # Initialize dynamic padding variables
    empty, pad_end, pad_start, dis_length, vis_tape = dynamic_padding(position, tape, dis_length)
    # Print step, postion, current state information
    print_info(position, step_number, current_state)
    # Return for spacing
    print()
    # Print dynamic tape
    print_tape(empty, pad_end, pad_start, dis_length, vis_tape)
    # IF speed was passed in via argparse, set the speed of the rendering
    if speed:
        time.sleep(speed)

def dynamic_padding(position, tape, dis_length):
    # Get the length of the tape
    length = len(tape)
    # Get the amount of tape length to display as set by the user via argparse
    empty = empty_char()
    pad_start = dis_length - position
    pad_end = dis_length - (length - (position + 1))
    dynamic_start = position - dis_length if position >= dis_length else 0
    dynamic_end = length - (length - position - dis_length) if length - position > dis_length else length
    vis_tape = stringify(tape)[dynamic_start:dynamic_end]
    return empty, pad_end, pad_start, dis_length, vis_tape

def print_tape(empty, pad_end, pad_start, dis_length, visible_tape_section):
    pad_icons = dis_length * 2 * '•'
    print(pad_icons + '↓' + pad_icons)
    print(tape_visualization(pad_start * empty + visible_tape_section + pad_end * empty))
    print(pad_icons + '↑' + pad_icons)

def print_info(position, step_number, current_state):
    print('Step Number: {}'.format(str(step_number).rjust(12)))
    print('Current State: {}'.format(str(current_state).rjust(10)))
    print('Tape Position: {} '.format(str(position).rjust(10)))


