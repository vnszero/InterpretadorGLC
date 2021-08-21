from typing import List
class Stack:
    def __init__(self, terms : str, old_stack : List = []):
        '''
        terms = 'STACK'

        self.stack_top() = 'S'
        '''
        self.stack = old_stack
        for term in terms[::-1]:
            self.stack.append(term)
            
    def get_stack_len(self) -> int:
        return len(self.stack)

    def get_stack_top(self) -> str:
        try:
            return self.stack.pop()
        except IndexError:
            return 'END'

    def get_stack_full(self) -> List:
        # a copy of the stack to avoid non-capsule trouble
        copy = []
        for element in self.stack:
            copy.append(element)
        return copy

    def __repr__(self) -> str:
        string = ''
        for term in self.stack[::-1]:
            string += term + '\n'
        return string

    def __str__(self) -> str:
        string = ''
        for term in self.stack[::-1]:
            string += term + '\n'
        return string

    def put_one_on_top(self, top : str):
        self.stack.append(top)
    
    def is_empty(self) -> bool:
        if self.stack:
            return False
        return True