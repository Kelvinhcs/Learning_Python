listagem = [[[],[],[]], [[],[],[]], [[], [], []]]
for principal in range(0, 3):
    for contador in range(0,3):
        digitado = int(input(f'Digite um valor para posição [{principal}, {contador}]: '))
        listagem[principal][contador].append(digitado)
for item in listagem:
    for vezes, coisa in enumerate(item):
        print(coisa, end='')
    print()
            