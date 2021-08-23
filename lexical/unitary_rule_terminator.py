from structure.GLC import GLC
from structure.constants import LAMBDA
from typing import List

def unitary_rule_terminator(language : GLC):
    '''
        find and remove unitary rules from language
    '''
    chaining_dict = dict()
    for variable in language.get_variable_list():
        chain_list = []
        for transation in language.get_transitions_list():
            if transation[0] == variable:
                only_variables = transation[1]
                if len(only_variables) == 1:
                    for alpha in language.get_alpha_list():
                        only_variables = only_variables.replace(alpha, '')
                    only_variables = only_variables.replace(LAMBDA, '')
                    chain_list[:0] = only_variables

        chain_list = list(set(chain_list))
        if variable in chain_list:
            chain_list.remove(variable)
        chaining_dict[variable] = chain_list

    visited_variables_list = []
    while len(visited_variables_list) < len(language.get_variable_list()):
        for variable in language.get_variable_list():
            if chaining_dict[variable] == []:
                visited_variables_list.append(variable)
            else:
                check = True
                for variable_check in chaining_dict[variable]:
                    if not(variable_check in visited_variables_list):
                        check = False
                if check:
                    new_transitions = []
                    for checked_variable in chaining_dict[variable]: 
                        for transition in language.get_transitions_list():
                            if checked_variable == transition[0]:
                                new_transition = [variable, transition[1]]
                                new_transitions.append(new_transition)
                    for new_t in new_transitions:
                        language.insert_into_transition_list(new_t)
                    visited_variables_list.append(variable)

    no_unitary_transitions = []
    for transition in language.get_transitions_list():
        if len(transition[1]) > 1 or transition[1] in language.get_alpha_list() or transition[1] in [LAMBDA]:
            no_unitary_transitions.append(transition)

    language.set_transitions_list(no_unitary_transitions)