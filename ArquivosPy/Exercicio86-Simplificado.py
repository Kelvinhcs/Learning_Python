Matriz = [[[],[],[]], [[],[],[]], [[], [], []]]
for Linha in range(0, 3):
    for Coluna in range(0,3):
        Digitado = int(input(f'Digite um valor para posição [{Linha}, {Coluna}]: '))
        Matriz[Linha][Coluna].append(Digitado)
for Linha in Matriz:
    for Coluna in Linha:
        print(Coluna, end='')
    print()
            