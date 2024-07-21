lista = list()
for c in range(0, 5):
    lista.append(int(input(f'Digite o {c+1}º número: ')))
print(lista)
print(f'O maior número da lista é {max(lista)} na posição ', end='')
for indice, valor in enumerate(lista):
    if valor == max(lista):
        print(f'{indice+1}...', end='')
print()
print(f'O menor número da lista é {min(lista)} na posição ', end='')
for indice, valor in enumerate(lista):
    if valor == min(lista):
        print(f'{indice+1}...', end='')
print()
