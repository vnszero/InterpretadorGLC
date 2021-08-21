from structure.GLC import GLC
from structure.constants import LAMBDA
from typing import List

def find_new_var_name(upper_ASCII : List, used_variables : List) -> str:
    name = None
    while name == None:
        if chr(upper_ASCII[0]) in used_variables:
            # already exists, call next
            upper_ASCII[0] += 1
        else:
            name = chr(upper_ASCII[0])
            upper_ASCII[0] += 1
    return name

def alpha_to_var(language : GLC):
    upper_ASCII = [65]
    used_variables = language.get_variable_list()
    used_alphas = language.get_alpha_list()
    new_var_dict = dict()
    new_transition_list = []
    for alpha in used_alphas:
        var_name = find_new_var_name(upper_ASCII, used_variables)
        transition = [var_name, alpha]
        new_var_dict[alpha] = var_name
        language.insert_into_transition_list(transition)
    
    # there are new transitions for all alphas
    # let's replace and see if we need then all
    used_new_var = []
    for transit in language.get_transitions_list():
        variable, rule = transit
        if len(rule) > 1:
            update_rule = rule[0]
            for instant_rule in rule[1:]:
                if instant_rule in used_alphas:
                    update_rule += new_var_dict[instant_rule]
                    used_new_var.append(instant_rule)
                else:
                    update_rule += instant_rule

            if update_rule != rule:
                new_transition_list.append([variable, update_rule])
            else:
                new_transition_list.append(transit)

    for alpha in used_alphas:
        if alpha in used_new_var:
            variable = new_var_dict[alpha]
            new_transition_list.append([variable, alpha])

    language.set_transitions_list(new_transition_list)