import sys
from typing import List

def state_and_alpha_review(state_list : List, alpha_list : List, transitions_list : List, initial_state : str):
    try:
        if not(initial_state in state_list):
            raise ValueError('There is no state '+f'{initial_state}'+', tip: check the JSON file')
    except ValueError as e:
        print(e)
        sys.exit(1)

    for transition in transitions_list:
        state = transition[0]
        argument = transition[1]
        try:
            if not(state in state_list):
                raise ValueError('There is no state '+f'{state}'+', tip: check the JSON file')

            for arg in argument:
                if not(arg in state_list or arg in alpha_list or arg == '#'):
                     raise ValueError('There is no state or alphabet simbol for '+f'{arg}'+', tip: check the JSON file')

        except ValueError as e:
            print(e)
            sys.exit(1)
