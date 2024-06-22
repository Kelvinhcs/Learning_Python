while True:
    resposta = ''
    while resposta not in ('s', 'n'):
        resposta = str(input('Quer continuar [s/n] ? ')).strip().lower()[0]
        if resposta not in ('s', 'n'):
            print(f'Resposta Inválida, tente novamente...')
    if resposta == 'n':
        break
    if resposta == 's':
        print('Digitei certo, fechando...')
        break
print('Fim')
        