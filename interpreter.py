from structure.stack import Stack
from file_manager import loader, output
from structure.GLC import GLC
from structure.greibach_path import GreibachPaths
from structure.stack import Stack
from lexical.reviewer import state_and_alpha_review
import sys

def main(args):
    # ler do terminal: python3 interpreter.py ex.json 4
    file_name = args[1]
    word_size = args[2]

    artefact = loader.read_json(file_name)
    
    if artefact != None:
        language = GLC()
        language.set_state_list(artefact['glc'][0])
        language.set_alpha_list(artefact['glc'][1])
        language.set_transitions_list(artefact['glc'][2])
        language.set_initial_state(artefact['glc'][3])

        sl = language.get_state_list()
        al = language.get_alpha_list()
        tl = language.get_transitions_list()
        ist = language.get_initial_state()

        state_and_alpha_review(sl, al, tl, ist)

        output.file_generator("saida_ex1.txt", str(language))

        paths = GreibachPaths(language)
        
        stack = Stack(ist)
        #print(language)
        #print(paths)
        #print(stack)

if __name__ == '__main__':
    sys.exit(main(sys.argv))