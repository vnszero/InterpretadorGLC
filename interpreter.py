from lexical.greibach_converter import greibach_converter
from lexical.alpha_to_var import alpha_to_var
from lexical.useless_variable_terminator import useless_variable_terminator
from lexical.unitary_rule_terminator import unitary_rule_terminator
from lexical.lambda_terminator import lambda_terminator
from structure.tree import Tree
from structure.stack import Stack
from file_manager import loader, output
from structure.GLC import GLC
from structure.greibach_path import GreibachPaths
from structure.stack import Stack
from structure.constants import LAMBDA
from structure.word_keeper import WordKeeper
from lexical.reviewer import variable_and_alpha_review
import sys

def main(args):
    # ler do terminal: python3 interpreter.py ex.json 4
    file_name = args[1]
    word_size_limit = int(args[2])

    artefact = loader.read_json(file_name)
    
    if artefact != None:
        language = GLC()
        language.set_variable_list(artefact['glc'][0])
        language.set_alpha_list(artefact['glc'][1])
        language.set_transitions_list(artefact['glc'][2])
        language.set_initial_variable(artefact['glc'][3])

        variable_l = language.get_variable_list()
        alpha_l = language.get_alpha_list()
        transition_l = language.get_transitions_list()
        ist = language.get_initial_variable()
        
        variable_and_alpha_review(variable_l, alpha_l, transition_l, ist)
        
        lambda_terminator(language)
        unitary_rule_terminator(language)
        useless_variable_terminator(language)
        alpha_to_var(language)
        useless_variable_terminator(language)
        #print(language.get_transitions_list())
        greibach_converter(language)
        
        
        '''
        paths = GreibachPaths(language)
        
        stack = Stack(ist)

        tree = Tree(stack)
        keeper = WordKeeper()
        paths_dict = paths.get_paths_dict()
        
        # verificar se a linguagem gera lambda
        key = LAMBDA + ist
        if key in paths_dict.keys():
            keeper.insert_word(LAMBDA)
            extend_alpha_l = alpha_l + [LAMBDA]

        tree.get_root().call_next_node(keeper, extend_alpha_l, paths_dict, word_size_limit)

        output.file_generator("words.txt", str(keeper))
        output.file_generator("saida_lang.txt", str(language))
        '''

if __name__ == '__main__':
    sys.exit(main(sys.argv))