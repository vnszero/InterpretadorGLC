# Abstract:
This is an interpreter for Free Context Languages in Python 3 to find all words for that language based in file and in size limit for words.

# How to use:
python3 interpreter.py json_file_name word_size_limit

# Example:
python3 interpreter.py ex2_glc.json 5

# Output:
An well succed execution should create two files: `output_language.txt` and `output_words.txt`. First one show us the chosen language in Greibach Normal Form and the second one hold all found words.

# Overview:
The main idea is to make a depth search in a tree and store found words in array. It uses a back-track strategy to return to old state and search in other ways. The depth search stop in two cases: if the algorithm found no more terms to continue or if the node depth overflow the size limit.

# Issues
It isn't so fast and the cost grows fast. For an example: when try to run ex5_glc.json for 10 as size limit will expend no more than 7 minutes to found 678 words.

# Author
Vinícius Nascimento Silva

# Subject
Linguagens Formais e Autômatos - DECOM - CEFET