from structure.GLC import GLC
from structure.constants import LAMBDA
from typing import List

def unitary_rule_terminator(language : GLC):
    chaining_dict = dict()
    for state in language.get_state_list():
        chain_list = []
        for transation in language.get_transitions_list():
            if transation[0] == state:
                only_states = transation[1]
                if len(only_states) == 1:
                    for alpha in language.get_alpha_list():
                        only_states = only_states.replace(alpha, '')
                    only_states = only_states.replace(LAMBDA, '')
                    chain_list[:0] = only_states

        chain_list = list(set(chain_list))
        if state in chain_list:
            chain_list.remove(state)
        chaining_dict[state] = chain_list

    visited_states_list = []
    while len(visited_states_list) < len(language.get_state_list()):
        for state in language.get_state_list():
            if chaining_dict[state] == []:
                visited_states_list.append(state)
            else:
                check = True
                for state_check in chaining_dict[state]:
                    if not(state_check in visited_states_list):
                        check = False
                if check:
                    new_transitions = []
                    for checked_state in chaining_dict[state]: 
                        for transition in language.get_transitions_list():
                            if checked_state == transition[0]:
                                new_transition = [state, transition[1]]
                                new_transitions.append(new_transition)
                    for new_t in new_transitions:
                        language.insert_into_transition_list(new_t)
                    visited_states_list.append(state)

    no_unitary_transitions = []
    for transition in language.get_transitions_list():
        if len(transition[1]) > 1 or transition[1] in language.get_alpha_list() or transition[1] in [LAMBDA]:
            no_unitary_transitions.append(transition)

    language.set_transitions_list(no_unitary_transitions)