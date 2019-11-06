# -*- coding: utf-8 -*-

from utils import *

a = ["a","b","c","d"]
b = ["a","b","","c"]
c = 0
d = ["a","b"," ","c"]
e = ["a","b","","c", " "]
f = [">","b","c","d","X","X","Y","[","a","b","c","]","a","b","c","]","a","b","c","a"] # list has an intentional unkown charater

string = stringify(a)
print("Stringify test:")
print(string)
print("\n")

print("clean test:")
print(clean_list(b))
print(clean_list(d))
print(clean_list(e))
print("\n")

print("checklist length test:")
print(check_list_length(b))
print(check_list_length(f))
print("\n")

print("next position:")
print(next_position(c, "right"))
print("\n")


print("count_list_members test:")
print("the tested list:")
print(f)
print("[char_a, char_b, char_c, char_arrow, char_x, char_y, char_left_bracket, char_right_bracket, char_unknown]")
print(count_list_members(f))

print("count_specific_member test:")
#prints out the number of a specific charatcer in a list
#can be passed an upper or lower case charater
print(count_specific_member(f, "A"))
#unknown characters are addded up in the function aswell, can use this to check the string is valid with our stirng alphabet
print(count_specific_member(f, "v"))
