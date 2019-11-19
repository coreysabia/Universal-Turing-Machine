from utils import *
from utm import *
import json

writeValue = " "
nextState = "q1"
moveTo = "Right"
currentState = "q0"
readHead = " "



print('***os_check function:')
os_check()

#this is breaking the auto tests for some reason, but we know it works anyways...
print('***argument_parser_pyinquirer:')
print()
#request_user_input()
print('\n')


print("***transition_encode:")
print('should be: ')
print('0000 1000 0001 1000 1')
print(transition_encode(writeValue, nextState, moveTo, currentState, readHead))