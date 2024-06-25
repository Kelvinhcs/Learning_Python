Listagem = list()
placeholder = list()
MaisPesado = MaisLeve = 0
print('-=-'*22)
while True:
    resposta = ''
    placeholder.append(str(input('Digite o Nome: ')).strip().capitalize())
    placeholder.append(float(input('Digite o Peso: ')))
    if len(Listagem) == 0:
        MaisPesado = MaisLeve = placeholder[1]
    if placeholder[1] > MaisPesado:
        MaisPesado = placeholder[1]
    if placeholder[1] < MaisLeve:
        MaisLeve = placeholder[1]
    Listagem.append(placeholder[:])
    placeholder.clear()
    while resposta not in ('s', 'n'):
        resposta = str(input('Quer continuar[s/n]? ')).strip().lower()[0]
        if resposta not in ('s', 'n'):
            print('Resposta Inválida. Tente novamente...')
    print('-=-'*22)
    if resposta == 'n':
        break
print(f'O total de pessoas cadastradas é de {len(Listagem)}')
print(f'O peso da pessoa mais pesada é de {MaisPesado:.2f}Kg. Peso de ', end='')
for pessoa in Listagem:
    if pessoa[1] == MaisPesado:
        print(f'{pessoa[0]} -> ', end='')
print('Fim')
print(f'O mais leve registrado é de {MaisLeve:.2f}Kg. Peso de ', end='')
for pessoa in Listagem:
    if pessoa[1] == MaisLeve:
        print(f'{pessoa[0]} -> ', end='')
print('Fim')
print('-=-'*22)
