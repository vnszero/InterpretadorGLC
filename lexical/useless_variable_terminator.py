from structure.GLC import GLC
from structure.constants import LAMBDA
from typing import List

def useless_variable_terminator(language : GLC):
    # 1st part
    used_variables = []
    discovered_variables = []
    for transition in language.get_transitions_list():
        variable, rule = transition
        if rule in language.get_alpha_list() and not(variable in discovered_variables):
            discovered_variables.append(variable)
    used_variables = discovered_variables

    while discovered_variables != []:
        discovered_variables = []
        for transition in language.get_transitions_list():
            variable, rule = transition
            if not (variable in used_variables):
                check = True
                for part_rule in rule:
                    if not(part_rule in language.get_alpha_list()) and not(part_rule in used_variables):
                        check = False
                if check:
                    discovered_variables.append(variable)
                used_variables += discovered_variables
    
    language.set_variable_list(used_variables)
    used_transitions_1st_part = []
    for transition in language.get_transitions_list():
        variable, rule = transition
        if variable in used_variables:
            used_transitions_1st_part.append(transition)
    language.set_transitions_list(used_transitions_1st_part)

    # 2nd part
    discovered_variables = [language.get_initial_variable()]
    used_variables = discovered_variables
    while discovered_variables != []:
        discovered_variables = []
        for transition in language.get_transitions_list():
            variable, rule = transition
            if variable in used_variables:
                for part_rule in rule:
                    if part_rule in language.get_variable_list():
                        if not (part_rule in used_variables) and not (part_rule in discovered_variables):
                            discovered_variables.append(part_rule)
        used_variables += discovered_variables

    language.set_variable_list(used_variables)
    used_transitions_2nd_part = []
    for transition in language.get_transitions_list():
        variable, rule = transition
        if variable in used_variables:
            used_transitions_2nd_part.append(transition)
    language.set_transitions_list(used_transitions_2nd_part)