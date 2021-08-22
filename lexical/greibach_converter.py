from structure.constants import LAMBDA, NEG_INC
from lexical.usefull_funct import find_new_var_name
from typing import List
from structure.GLC import GLC
from structure.stack import Stack

def left_call_only(rules : List, variable : str) -> List:
    left_rules = []
    for rule in rules:
        if rule[0] == variable:
            left_rules.append(rule)
    return left_rules

def left_call_remover(rules : List, variable : str) -> List:
    other_rules = []
    for rule in rules:
        if rule[0] != variable:
            other_rules.append(rule)
    return other_rules

def auxiliar_rule_creator(rules : List, upper_ASCII : List, used_var) -> List and str:
    var_name = find_new_var_name(upper_ASCII, NEG_INC, used_var)
    transitions = []
    for rule in rules:
        transitions.append([var_name, rule[1:]])
        transitions.append([var_name, rule[1:] + var_name])
    return transitions, var_name

def right_rule_generator(rules : List, variable : str, right_caller : str):
    transitions = []
    for rule in rules:
        transitions.append([variable, rule])
        if rule != LAMBDA:
            transitions.append([variable, rule + right_caller])
        else:
            transitions.append([variable, right_caller])
    return transitions

def replace_rule(rules : List, fixed : str) -> List:
    new_rule = []
    for rule in rules:
        new_rule.append(rule + fixed)
    return new_rule

def greibach_converter(language : GLC):
    upper_ASCII = [90]
    # remap
    order = 1
    transitions_dict = dict()
    keys_dict = dict()
    keys_order = dict()
    for transition in language.get_transitions_list():
        variable, rule = transition
        if not(variable in keys_dict.keys()):
            key = variable + str(order)
            keys_order[order] = variable
            keys_dict[variable] = key
            transitions_dict[key] = [rule]
            order += 1
        else:
            key = keys_dict[variable]
            transitions_dict[key].append(rule)
    
    # it is much better to work with a dictionary
    # Why did not I think about it before?
    # print(transitions_dict)

    # 2st step, remove left calls and out orders
    aux_dict = dict()
    order_stack = Stack('')
    for var_s_ord in keys_order:
        variable = keys_order[var_s_ord]
        order_stack.put_one_on_top(str(var_s_ord))
        key = keys_dict[variable]
        new_aux_transits = []
        new_transits = []
        #print(transitions_dict[key])
        need_to_repeat = True
        while need_to_repeat:
            need_to_repeat = False
            for rule in transitions_dict[key]:
                first = rule[0]
                
                if first in language.get_variable_list():
                    first_s_key = keys_dict[first]
                    first_s_ord = first_s_key[1]
                    if int(var_s_ord) == int(first_s_ord):
                        # left call detected
                        other_rules = left_call_remover(transitions_dict[key], variable)
                        left_rules = left_call_only(transitions_dict[key], variable)
                        new_aux_transits, var_name = auxiliar_rule_creator(left_rules, upper_ASCII, language.get_variable_list())
                        new_transits = right_rule_generator(other_rules, variable, var_name)
                        
                        k = var_name + str(order)
                        aux_dict[k] = []
                        for t in new_aux_transits:
                            r = t[1]    
                            aux_dict[k].append(r)
                        order += 1
                        need_to_repeat = True
                    elif var_s_ord > int(first_s_ord):
                        extend_rules = replace_rule(transitions_dict[first_s_key], rule[1:])
                        transitions_dict[key].remove(rule)
                        for e_rule in extend_rules:
                            transitions_dict[key].append(e_rule)
                        need_to_repeat = True

            #incorporate
            if new_transits != []:
                transitions_dict[key] = []
                for transition in new_transits:
                    rule = transition[1]
                    transitions_dict[key].append(rule)
                #print(transitions_dict[key])
                #print()
                #print(aux_dict)
                #print()
            #print(variable)
    #print(transitions_dict)
    #print(aux_dict)
    #print()

    #3rd step
    while not(order_stack.is_empty()):
        re_ord = int(order_stack.get_stack_top())
        variable = keys_order[re_ord]
        key = keys_dict[variable]
        need_to_repeat = True
        while need_to_repeat:
            need_to_repeat = False
            for rule in transitions_dict[key]:
                first = rule[0]
                if first in language.get_variable_list():
                    first_s_key = keys_dict[first]
                    extend_rules = replace_rule(transitions_dict[first_s_key], rule[1:])
                    transitions_dict[key].remove(rule)
                    for e_rule in extend_rules:
                        transitions_dict[key].append(e_rule)
                    need_to_repeat = True
    
    #aux fix
    need_to_repeat = True
    while need_to_repeat:
        need_to_repeat = False
        for aux_key in aux_dict:
            for rule in aux_dict[aux_key]:
                first = rule[0]
                if first in language.get_variable_list():
                    first_s_key = keys_dict[first]
                    extend_rules = replace_rule(transitions_dict[first_s_key], rule[1:])
                    aux_dict[aux_key].remove(rule)
                    for e_rule in extend_rules:
                        aux_dict[aux_key].append(e_rule)
                    need_to_repeat = True

    # back to List
    greibach_format_transitions = []
    for key in transitions_dict:
        variable = key[0]
        for rule in transitions_dict[key]:
            greibach_format_transitions.append([variable, rule])
    
    for key in aux_dict:
        variable = key[0]
        for rule in aux_dict[key]:
            greibach_format_transitions.append([variable, rule])
    
    language.set_transitions_list(greibach_format_transitions)