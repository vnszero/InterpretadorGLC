from typing import Dict, List
from structure.stack import Stack
from structure.word_keeper import WordKeeper
from structure.constants import LAMBDA, OVERFLOW

class Node:
    '''
        ex of a Node:
        holds the reference to only the next Node (not all, overwrite)
        holds his depth in tree
        holds the current formed word
        holds an stack of next variables
    '''
    def __init__(self, alpha : str, stack : Stack, word : str = '', depth : int = 0):
        self.next = None
        if alpha == LAMBDA:
            # depth keep his old value if LAMBDA
            self.depth = depth
        else:
            self.depth = depth + 1

        if alpha == LAMBDA:
            # keep the old formed word
            self.formed_word = word
        else:
            self.formed_word = word + alpha

        self.stack = stack
    
    def get_formed_word(self) -> str:
        return self.formed_word

    def depth_control(self, word_size_limit) -> bool:
        '''
            verify the limit of search in Nodes
        '''
        if self.depth > word_size_limit:
            return OVERFLOW
        else:
            return not OVERFLOW

    def call_next_node(self, keeper : WordKeeper, alpha_list : List, paths_dict : Dict, word_size_limit : int):
        '''
            verify if it is a reconized word
            for each alpha allowed, create new Node
        '''
        # take a look at the stack
        if self.stack.get_stack_len() == 0:
            # empty stack, so we got a word
            keeper.insert_word(self.formed_word)

        # pop effect
        top = self.stack.get_stack_top()
        if top != 'END':
            for alpha in alpha_list:
                key = alpha + top
                if key in paths_dict.keys():
                    # if there is a key, there is a path and a new node
                    for path in paths_dict[key]:
                        new_stack = Stack(path.get_stack(), self.stack.get_stack_full())
                        self.next = Node(alpha, new_stack, self.formed_word, self.depth)
                        #if self.next.depth_control(word_size_limit)and self.next.stack_control(word_size_limit):
                        if self.next.depth_control(word_size_limit):
                            # keep going
                            self.next.call_next_node(keeper, alpha_list, paths_dict, word_size_limit)
                        else:
                            # overflow, just stop tree evolution
                            pass

class Tree:
    '''
        ex of a Tree:
        only hold the root and start Node
    '''
    def __init__(self, stack : Stack, alpha : str = LAMBDA):
        self.root = Node(alpha, stack)
    
    def get_root(self) -> Node:
        return self.root