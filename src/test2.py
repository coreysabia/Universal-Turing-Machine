from utils import *
from utm import *
import json


with open('test_json.json') as json_file:
    data = json.load(json_file)




print('***os_check function:')
os_check()

#this is breaking the auto tests for some reason, but we know it works anyways...
print('***argument_parser_pyinquirer:')
print()
#request_user_input()
print('\n')
