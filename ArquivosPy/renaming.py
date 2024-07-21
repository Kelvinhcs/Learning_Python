import os 
allnames = os.listdir()
for item in allnames:
    if 'Exercicio' in item:
        os.renames(item, item.replace('Exercicio', 'ex'))   