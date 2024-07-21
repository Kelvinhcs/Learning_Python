listagem = [[[],[],[]], [[],[],[]], [[], [], []]]
for principal in range(0, 3):
    if principal == 0: 
        for contador in range(0,3):
            listagem[0][contador].append(int(input(f'Digite um valor para a posição [{principal}, {contador}]: ')))
    if principal == 1:
        for contador in range(0,3):
            listagem[1][contador].append(int(input(f'Digite um valor para a posição [{principal}, {contador}]: ')))
    if principal == 2:
        for contador in range(0,3):
            listagem[2][contador].append(int(input(f'Digite um valor para a posição [{principal}, {contador}]: ')))
for item in listagem:
    for vezes, coisa in enumerate(item):
        print(coisa, end='')
    print()