from typing import List

class GLC:
    def __init__(self):
        self.state_list = None
        self.alpha_list = None
        self.transitions_list = None
        self.initial_state = None

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

    def set_state_list(self, state_list : List):
        self.state_list = state_list

    def set_alpha_list(self, alpha_list : List):
        self.alpha_list = alpha_list
    
    def set_transitions_list(self, transitions_list):
        self.transitions_list = transitions_list

    def set_initial_state(self, initial_state):
        self.initial_state = initial_state

    def get_state_list(self) -> List:
        return self.state_list

    def get_alpha_list(self) -> List:
        return self.alpha_list
    
    def get_transitions_list(self) -> List:
        return self.transitions_list

    def get_initial_state(self) -> str:
        return self.initial_state