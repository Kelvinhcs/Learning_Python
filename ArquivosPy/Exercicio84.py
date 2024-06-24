listagem = list()
placeholder = list()
total = pesopp = pesopl = 0
print('-=-'*22)
while True:
    resposta = ''
    nome = str(input('Digite o Nome: ')).strip().capitalize()
    peso = float(input('Digite o Peso: '))
    placeholder.append(nome)
    placeholder.append(peso)
    listagem.append(placeholder[:])
    placeholder.clear()
    if total == 0:
        pesopp = pesopl = listagem[total][1]
    if peso > pesopp:
        pesopp = listagem[total][1]
    if peso < pesopl:
        pesopl = listagem[total][1]
    total += 1
    while resposta not in ('s', 'n'):
        resposta = str(input('Quer continuar[s/n]? ')).strip().lower()[0]
        if resposta not in ('s', 'n'):
            print('Resposta Inválida. Tente novamente...')
    print('-=-'*22)
    if resposta == 'n':
        break
print(f'O total de pessoas cadastradas é de {total}')
print(f'O peso da pessoa mais pesada é de {pesopp:.2f}Kg. Peso de ', end='')
for pessoa in listagem:
    if pessoa[1] == pesopp:
        print(f'{pessoa[0]}->', end='')
print('Fim')
print(f'O mais leve registrado é de {pesopl:.2f}Kg. Peso de ', end='')
for pessoa in listagem:
    if pessoa[1] == pesopl:
        print(f'{pessoa[0]}->', end='')
print('Fim')
print('-=-'*22)
