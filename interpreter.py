from structure.tree import Tree
from structure.stack import Stack
from file_manager import loader, output
from structure.GLC import GLC
from structure.greibach_path import GreibachPaths
from structure.stack import Stack
from structure.constants import LAMDA
from structure.word_keeper import WordKeeper
from lexical.reviewer import state_and_alpha_review
import sys

def main(args):
    # ler do terminal: python3 interpreter.py ex.json 4
    file_name = args[1]
    word_size_limit = int(args[2])

    artefact = loader.read_json(file_name)
    
    if artefact != None:
        language = GLC()
        language.set_state_list(artefact['glc'][0])
        language.set_alpha_list(artefact['glc'][1])
        language.set_transitions_list(artefact['glc'][2])
        language.set_initial_state(artefact['glc'][3])

        state_l = language.get_state_list()
        alpha_l = language.get_alpha_list()
        transition_l = language.get_transitions_list()
        ist = language.get_initial_state()
        
        state_and_alpha_review(state_l, alpha_l, transition_l, ist)

        paths = GreibachPaths(language)
        
        stack = Stack(ist)

        tree = Tree(stack)
        keeper = WordKeeper()
        paths_dict = paths.get_paths_dict()
        
        # verificar se a linguagem gera lambda
        key = LAMDA + ist
        if key in paths_dict.keys():
            keeper.insert_word(LAMDA)
            extend_alpha_l = alpha_l + [LAMDA]

        tree.get_root().call_next_node(keeper, extend_alpha_l, paths_dict, word_size_limit)

        output.file_generator("words.txt", str(keeper))
        output.file_generator("saida_lang.txt", str(language))

if __name__ == '__main__':
    sys.exit(main(sys.argv))