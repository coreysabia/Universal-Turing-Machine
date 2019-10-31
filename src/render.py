from src.utils import *
from src.utm import *

#IGNORE THIS FILE FOR NOW PLEASE

def render(self, position=None, step_number=None):
    empty, padding_end, padding_start, visible_length, visible_tape_section = tape_format_calc(position)
    print_system_clear()
    print_statistics(position, step_number)
    self.print_render_mode_information()
    self.print_tape(empty, padding_end, padding_start, visible_length, visible_tape_section)
    self.print_sign_occurrences()
    if self.speed:
        time.sleep(self.speed)

def tape_format_calc(self, position=None):
    length = len(self.tape)
    visible_length = Config.visible_tape_length()
    empty = Config.empty_character()
    padding_start = visible_length - position
    padding_end = visible_length - (length - (position + 1))
    dynamic_start = position - visible_length if position >= visible_length else 0
    dynamic_end = length - (length - position - visible_length) if length - position > visible_length else length
    visible_tape_section = stringify(self.tape)[dynamic_start:dynamic_end]
    return empty, padding_end, padding_start, visible_length, visible_tape_section

def print_tape(self, empty, padding_end, padding_start, visible_length, visible_tape_section):
    padding_icons = visible_length * 2 * '~'
    print(padding_icons + '|' + padding_icons)
    print(pipeify(padding_start * empty + visible_tape_section + padding_end * empty))
    print(padding_icons + '|' + padding_icons)

def print_statistics(self, position, step_number):
    print('Step number {}'.format(str(step_number).rjust(7)))
    print('Current State {}'.format(self.state.rjust(7)))
    print('Tape position {} '.format(str(position).rjust(10)))