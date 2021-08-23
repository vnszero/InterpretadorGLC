import json
def read_json(file_name : str) -> str or None:
    '''
        open the json file and return its content in str format
    '''
    glc = 0
    try:
        with open(file_name, "r") as file:
            glc = json.load(file)
        return glc
    except:
        print('There is a problem with: '+f'{file_name}.'+' Tip: verify the path')
        return None