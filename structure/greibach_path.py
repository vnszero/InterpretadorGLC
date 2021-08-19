from structure.GLC import GLC

class Path:
    def __init__(self, alpha : str, top : str, stack : str):
        self.alpha = alpha
        self.top = top
        self.stack = stack
    
    def __repr__(self) -> str:
        return f'{self.alpha}'+', '+f'{self.top}'+' | '+f'{self.stack}'

    def __str__(self) -> str:
        return f'{self.alpha}'+', '+f'{self.top}'+' | '+f'{self.stack}'

class GreibachPaths:
    def __init__(self, language : GLC):
        self.paths_dict = dict()
        for transition in language.get_transitions_list():
            alpha = transition[1][0]
            top = transition[0]
            stack = transition[1][1:]
            key = alpha+top
            self.paths_dict[key] = Path(alpha, top, stack)

    def __repr__(self) -> str:
        string = ''
        for key in self.paths_dict:
            string += f'{self.paths_dict[key]}'+'\n'
        return string
        
    def __str__(self) -> str:
        string = ''
        for key in self.paths_dict:
            string += f'{self.paths_dict[key]}'+'\n'
        return string