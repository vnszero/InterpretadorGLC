from typing import List

def find_new_var_name(upper_ASCII : List, increment : int, used_variables : List) -> str:
    '''
        find a new name to a variable and use ascii to keep
        the parameter as a reference and hold the current value
        to future calls
    '''
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
    '''
        used to remove terms from rules
    '''
    return string[:pos] + string[pos+1:]