listagem = list()
listapar = list()
listaimpar = list()
while True:
    numero = int(input('Digite um número para adicionar a lista: '))
    listagem.append(numero)
    if numero % 2 == 0:
        listapar.append(numero)
    else:
        listaimpar.append(numero)
    resposta = str(input('Quer continuar[s/n]? ')).strip().lower()[0]
    if resposta not in ('s', 'n'):
        while resposta not in ('s', 'n'):
            print('Resposta inválida. Tente novamente: ')
            resposta = str(input('Quer continuar[s/n]? ')).strip().lower()[0]
    if resposta == 'n':
        break
print(f'A lista Total é: {listagem}')
print(f'A lista com os números pares é: {listapar}')
print(f'A lista com números impares é: {listaimpar}')
