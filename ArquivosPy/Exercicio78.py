lista = list()
posicaomaior = posicaomenor = valormaior = valormenor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite o {c+1}º número: ')))
    if c == 0:
        posicaomaior = posicaomenor = c
        valormaior = valormenor = lista[c]
    else:
        if lista[c] > valormaior:
            posicaomaior = c
        if lista[c] < valormenor:
            posicaomenor = c
lista.sort()
print(f'O maior número da lista é {lista[-1]}, na {posicaomaior+1}ª posição.')
print(f'O menor número da lista é {lista[0]}, na {posicaomenor+1}ª posição.')
