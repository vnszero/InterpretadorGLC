from structure.constants import POS_INC
from lexical.usefull_funct import find_new_var_name
from structure.GLC import GLC
from typing import List

def alpha_to_var(language : GLC):
    '''
        replace alphas with new variables in middle of rules
    '''
    upper_ASCII = [65]
    used_variables = language.get_variable_list()
    used_alphas = language.get_alpha_list()
    new_var_dict = dict()
    new_transition_list = []
    # there are new variables for all alphas
    for alpha in used_alphas:
        var_name = find_new_var_name(upper_ASCII, POS_INC, used_variables)
        transition = [var_name, alpha]
        new_var_dict[alpha] = var_name
        language.insert_into_transition_list(transition)
    
    # maybe some of then will become useless
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
        else:
            new_transition_list.append(transit)
            
    language.set_transitions_list(new_transition_list)