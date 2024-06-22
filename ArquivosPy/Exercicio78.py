lista = list()
posicaomaior = posicaomenor = valormaior = valormenor = 0
for c in range(0, 5):
    num = int(input(f'Digite o {c+1}º número: '))
    lista.append(num)
    if c == 0:
        posicaomaior = posicaomenor = 1
        valormaior = valormenor = num
    else:
        if num > valormaior:
            valormaior = num
            posicaomaior = c+1
        if num < valormenor:
            valormenor = num
            posicaomenor = c+1
    print(lista)
    print(f'O maior número da lista é {valormaior}, na {posicaomaior}ª posição.')
    print(f'O menor número da lista é {valormenor}, na {posicaomenor}ª posição.')
    print('-=-'*20)
print(lista)
print(f'O MAIOR número da lista é {valormaior}, na {posicaomaior}ª posição.')
print(f'O MENOR número da lista é {valormenor}, na {posicaomenor}ª posição.')
