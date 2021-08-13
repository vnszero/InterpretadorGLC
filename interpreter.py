from file_manager import loader, output
from structure.GLC_obj import GLC
from lexical.reviewer import state_and_alpha_review

def main():
    # ler do terminal: python3 interpreter.py ex.json 4

    artefact = loader.read_json("ex3_glc.json")
    
    language = GLC()
    language.set_state_list(artefact['glc'][0])
    language.set_alpha_list(artefact['glc'][1])
    language.set_transitions_list(artefact['glc'][2])
    language.set_initial_state(artefact['glc'][3])

    sl = language.get_state_list()
    al = language.get_alpha_list()
    tl = language.get_transitions_list()
    initial_state = language.get_initial_state()

    #reviwer
    state_and_alpha_review(sl, al, tl, initial_state)

    output.file_generator("saida_ex1.txt", str(language))

main()