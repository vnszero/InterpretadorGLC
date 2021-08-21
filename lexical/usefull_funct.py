from typing import List

def find_new_var_name(upper_ASCII : List, increment : int, used_variables : List) -> str:
    name = None
    while name == None:
        if chr(upper_ASCII[0]) in used_variables:
            # already exists, call next
            upper_ASCII[0] += increment
        else:
            name = chr(upper_ASCII[0])
            upper_ASCII[0] += increment
    return name

def remove_substring(pos : int, string : str) -> str:
    return string[:pos] + string[pos+1:]