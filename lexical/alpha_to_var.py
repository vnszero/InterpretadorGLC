from structure.GLC import GLC
from structure.constants import LAMBDA
from typing import List

def alpha_to_var(language : GLC):
    upper_ASCII = 65
    used_variable = language.get_variable_list()
    for transition in language.get_transitions_list():
        variable, rule = transition

        var_check = False
        if len(rule) > 1:
            alpha_only_check = False
            for part_rule in rule:
                if part_rule in used_variable:
                    alpha_only_check = True
            
            if alpha_only_check:
                # no var in a rule with len() > 1
                part_rule = rule[-1]
                while True:
                    if chr(upper_ASCII) in used_variable:
                        upper_ASCII += 1
                    else:
                        # new comming
                        var = chr(upper_ASCII)
                        language.insert_into_variable_list(var)
                        new_transition = [var, part_rule]
                        language.insert_into_transition_list(new_transition)

                        # fix the old one
                        rule.replace(part_rule, var)
                        old_transition = [variable, rule]
                        language.delete_in_transition_list(transition)
                        language.insert_into_transition_list(old_transition)

                        # break while
                        break

            for part_rule in rule:
                if part_rule in used_variable:
                    var_check = True
                if var_check and part_rule in language.get_alpha_list():
                    while True:
                        if chr(upper_ASCII) in used_variable:
                            upper_ASCII += 1
                        else:
                            # new comming
                            var = chr(upper_ASCII)
                            language.insert_into_variable_list(var)
                            new_transition = [var, part_rule]
                            language.insert_into_transition_list(new_transition)

                            # fix the old one
                            rule.replace(part_rule, var)
                            old_transition = [variable, rule]
                            language.delete_in_transition_list(transition)
                            language.insert_into_transition_list(old_transition)

                            # break while
                            break
