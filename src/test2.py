from utils import *
from utm import *
import json


with open('test_json.json') as json_file:
    data = json.load(json_file)




print('***os_check function:')
os_check()

print('***argument_parser_pyinquirer:')
print()
argument_parser_pyinquirer()
print('\n')

print("***tranistion encode***") # *****cant test without potentially breaking working utm due to import weirdness******
transition_encode(json_file)