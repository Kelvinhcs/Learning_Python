lista = list()
while True:
    resposta = ''
    numero = int(input('Digite um número: '))
    if numero in lista:
        print('Valor Duplicado, Desconsiderando...')
    else:
        print('Valor Adicionado com sucesso!')
        lista.append(numero)
    while resposta not in ('s', 'n'):
        resposta = str(input('Quer continuar [s/n] ? ')).strip().lower()[0]
        if resposta not in ('s', 'n'):
            print(f'Resposta Inválida, tente novamente...')
    if resposta == 'n':
        break
print(f'A lista final é')
lista.sort()
for numerobonito in lista:
    print(f'{numerobonito}-->', end='')
print('Fim!')
