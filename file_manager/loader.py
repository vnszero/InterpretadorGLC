import json
def read_json(file_name : str):
    glc = 0 #define a new glc obj
    with open(file_name, "r") as file:
        glc = json.load(file)
    return glc