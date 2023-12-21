import pathlib

file_path = pathlib.Path(__file__).parent

text = 'Manipulando txt'


file = open( str(file_path) + '\Arquivo.txt', 'w')

file.write(text)

file.close()