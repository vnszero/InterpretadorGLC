def file_generator(file_name : str, output : str):
    '''
        create a new file and write the output on it
    '''
    with open(file_name, 'w') as file:
        file.write(output)
