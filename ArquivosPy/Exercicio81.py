listagem = list()
while True:
    resposta = ''
    numero = int(input('Digite seu número: '))
    listagem.append(numero)
    while resposta not in ('s', 'n'):
        resposta = str(input('Quer continuar[s/n]? ')).strip().lower()[0]
        if resposta not in ('s', 'n'):
            print('Resposta inválida. Digite novamente...')
    if resposta == 'n':
        break
print()
listadecrescente = listagem[:]
listadecrescente.sort(reverse=True)
print(f'Você digitou {len(listagem)} números.')
print(f'A Lista orginal é {listagem}.')
print(f'A lista ordenada é: {sorted(listagem, reverse=True)}.')
if 5 in listagem:     
    print(f'O número 5 foi digitado na {listagem.index(5)+1}ª posição.')
else: 
    print('O número 5 não foi encontrado.')
    