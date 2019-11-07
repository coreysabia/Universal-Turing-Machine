# -*- coding: utf-8 -*-
from utils import *
from render import *

a = ["a","b","c","d"]
b = ["a","b","","c"]
c = 0

string = stringify(a)
print("*** stringify test:")
print(string)
print("\n")

print("*** clean test:")
print(clean_list(b))
print("\n")

print("*** checklist length test:")
print(check_list_length(b))
print("\n")

print("*** next position:")
print(next_position(c, "right"))
print("\n")

p = 2
s = 3
current_state = 'idk'
print("*** stats test:")
print(print_statistics(s, p, current_state))
print("\n")

empty, pad_end, pad_start, dis_length, visible_tape_section = tape_format_calc(p, b)
print("*** tape test:")
print(print_tape(empty, pad_end, pad_start, dis_length, visible_tape_section))
print("\n")

print("*** render test:")
print(render(s, p, current_state, b))
print("\n")