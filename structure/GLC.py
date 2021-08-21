from typing import List

class GLC:
    def __init__(self):
        self.variable_list = None
        self.alpha_list = None
        self.transitions_list = None
        self.initial_variable = None

    def __str__(self) -> str:
        display = ''
        for transition in self.transitions_list:
            display += f'{transition[0]}'+' -> '+f'{transition[1]}'+'\n'
        return display
    
    def __repr__(self) -> str:
        display = ''
        for transition in self.transitions_list:
            display += f'{transition[0]}'+' -> '+f'{transition[1]}'+'\n'
        return display

    def set_variable_list(self, variable_list : List):
        self.variable_list = variable_list

    def set_alpha_list(self, alpha_list : List):
        self.alpha_list = alpha_list
    
    def set_transitions_list(self, transitions_list : List):
        self.transitions_list = transitions_list

    def set_initial_variable(self, initial_variable : str):
        self.initial_variable = initial_variable

    def get_variable_list(self) -> List:
        return self.variable_list

    def get_alpha_list(self) -> List:
        return self.alpha_list
    
    def get_transitions_list(self) -> List:
        return self.transitions_list

    def get_initial_variable(self) -> str:
        return self.initial_variable

    def insert_into_transition_list(self, transition : List):
        self.transitions_list.append(transition)

    def insert_into_variable_list(self, variable : str):
        self.variable_list.append(variable)

    def delete_in_transition_list(self, transition : List):
        self.transitions_list.remove(transition)