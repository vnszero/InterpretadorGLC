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
    # command line: python3 interpreter.py ex.json 4
    if len(args) < 3:
        print('Usage: python3 interpreter.py json_file_name word_size_number')
    else:
        file_name = args[1]
        word_size_limit = int(args[2])
        artefact = loader.read_json(file_name)
        
        if artefact != None:
            # create the language based on json artefact
            language = GLC()
            language.set_variable_list(artefact['glc'][0])
            language.set_alpha_list(artefact['glc'][1])
            language.set_transitions_list(artefact['glc'][2])
            language.set_initial_variable(artefact['glc'][3])

            variable_l = language.get_variable_list()
            alpha_l = language.get_alpha_list()
            transition_l = language.get_transitions_list()
            ist = language.get_initial_variable()
            
            # just a check-up
            variable_and_alpha_review(variable_l, alpha_l, transition_l, ist)
            
            # 1st: removing lambda rules
            lambda_terminator(language)

            # 2nd: removing unitary rules
            unitary_rule_terminator(language)

            # 3rd: removing useless variable
            useless_variable_terminator(language)

            # 4th: swap alphas with new variables
            alpha_to_var(language)

            # 5th: some swaps can create useless variables
            '''
                Happens when a pretender variable is not used
            '''
            useless_variable_terminator(language)

            # 6th: to greibach format
            greibach_converter(language)

            # 7th: the outlaw
            '''
                In some languages, I found some unitary rules after
                the conversion. Happens when the start variable
                had a left call and the language has lambda.
                Imagine a new variable 'Z' to turn left call 
                into right call and when Z works with lambda
                emerges a new transition #Z = Z. The solution:
                lets call the unitary remover again
            '''
            unitary_rule_terminator(language)
            
            # to file
            output.file_generator("output_language.txt", str(language))
            
            # lets see all transition as: ALPHA. TOP | STACK
            paths = GreibachPaths(language)
            
            # starts with the start variable
            stack = Stack(ist)

            # Greybach machine derivation tree
            tree = Tree(stack)

            # hold all found words
            keeper = WordKeeper()

            # in search for lambda
            paths_dict = paths.get_paths_dict()
            key = LAMBDA + ist
            extend_alpha_l = alpha_l
            if key in paths_dict.keys():
                keeper.insert_word(LAMBDA)
                extend_alpha_l += [LAMBDA]

            # finding nexts nodes
            tree.get_root().call_next_node(keeper, extend_alpha_l, paths_dict, word_size_limit)

            # to files
            output.file_generator("output_words.txt", str(keeper))

            # to command line
            print(str(keeper))
        
if __name__ == '__main__':
    sys.exit(main(sys.argv))