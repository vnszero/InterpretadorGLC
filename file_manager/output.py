def file_generator(file_name : str, output : str):
    with open(file_name, 'w') as file:
        file.write(output)
