import sys
from typing import List

def variable_and_alpha_review(variable_list : List, alpha_list : List, transitions_list : List, initial_variable : str):
    try:
        if not(initial_variable in variable_list):
            raise ValueError('There is no variable '+f'{initial_variable}'+', tip: check the JSON file')
    except ValueError as e:
        print(e)
        sys.exit(1)

    for transition in transitions_list:
        variable = transition[0]
        argument = transition[1]
        try:
            if not(variable in variable_list):
                raise ValueError('There is no variable '+f'{variable}'+', tip: check the JSON file')

            for arg in argument:
                if not(arg in variable_list or arg in alpha_list or arg == '#'):
                     raise ValueError('There is no variable or alphabet simbol for '+f'{arg}'+', tip: check the JSON file')

        except ValueError as e:
            print(e)
            sys.exit(1)
