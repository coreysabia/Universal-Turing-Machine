from src.utils import *
from src.utm import *
import os
import time
from neotermcolor import cprint
#IGNORE THIS FILE FOR NOW PLEASE

def render(position, step_number, current_state, tape, speed, dis_length):
    # Clear screen to wipe previous state
    print_system_clear()

    # Initialize dynamic padding variables
    empty, pad_end, pad_start, dis_length, vis_tape = dynamic_padding(position, tape, dis_length)

    # Print step, postion, current state information
    print_info(position, step_number, current_state)
    print()

    # Print dynamic tape
    print_tape(empty, pad_end, pad_start, dis_length, vis_tape)
    print()

    # Print counts of characters seen in tape
    #print_counts(tape)
    # Pause for amount of seconds passed in by user
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
    pad_icons_outer = dis_length * 2 * '═'
    pad_icons_inner = dis_length * 2 * ' '
    top_pad_icons_outer = pad_icons_outer + '╦' + pad_icons_outer
    top_pad_icons_inner = pad_icons_inner + '↓' + pad_icons_inner
    bottom_pad_icons_inner = pad_icons_inner + '↑' + pad_icons_inner
    bottom_pad_icons_outer = pad_icons_outer + '╩' + pad_icons_outer
    pad_tape = tape_visualization(pad_start * empty + visible_tape_section + pad_end * empty)

    cprint(top_pad_icons_outer, 30)
    cprint(top_pad_icons_inner, 30, attrs=['bold'])
    cprint(pad_tape, 119, attrs=['bold'])
    cprint(bottom_pad_icons_inner, 30, attrs=['bold'])
    cprint(bottom_pad_icons_outer, 30)

def print_info(position, step_number, current_state):
    step_number_text = ' Step Number: {} '.format(str(step_number).rjust(12))
    current_state_text = ' Current State: {} '.format(str(current_state).rjust(10))
    tape_position_text = ' Tape Position: {} '.format(str(position).rjust(10))
    cprint(step_number_text, 60)
    cprint(current_state_text, 60)
    cprint(tape_position_text, 60)


    
def print_counts(tape):
    zero = '0'
    if zero in tape:
        print('Count of 0: {}'.format(str(count_specific_member_json(tape, zero)).rjust(13)))


def test_render(position, step_number, current_state, tape, speed, dis_length):
    # TEST RENDER just print one output to test the render function
    # Initialize dynamic padding variables
    empty, pad_end, pad_start, dis_length, vis_tape = dynamic_padding(position, tape, dis_length)
    # Print step, postion, current state information
    print_info(position, step_number, current_state)
    print_counts(tape)
    # Return for spacing
    print()
    # Print dynamic tape
    print_tape(empty, pad_end, pad_start, dis_length, vis_tape)