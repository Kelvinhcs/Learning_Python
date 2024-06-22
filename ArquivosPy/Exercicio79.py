lista = list()
resposta = ''
while True:
    numero = int(input('Digite um número: '))
    if numero in lista:
        print('Valor Duplicado, Desconsiderando...')
    else:
        print('Valor Adicionado com sucesso!')
        lista.append(numero)
    resposta = str(input('Quer continuar [s/n] ? ')).strip().lower()[0]
    if resposta not in ('s', 'n'):
        while resposta not in ('s', 'n'):
            print(f'Resposta Inválida, tente novamente...')
            resposta = str(input('Quer continuar [s/n] ? ')).strip().lower()[0]
    if resposta == 'n':
        break
print(f'A lista final é')
lista.sort()
for numerobonito in lista:
    print(f'{numerobonito}-->', end='')
print('Fim!')
