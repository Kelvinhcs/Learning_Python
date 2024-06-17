from random import randint
qtd = 0
print('============================ PAR / IMPAR ============================')
while True:
    num = int(input('Digite um número de 0 a 10: '))
    if num < 0 or num > 10:
        while num < 0 or num > 10:
            print('-=-' * 23)
            print('Escolha inválida... Tente outra vez...')
            num = int(input('Digite um número VÁLIDO desta vez: '))
    pc = randint(1, 10)
    resposta = str(input('Você quer Par ou Impar [P/I]? ')).strip().lower()[0]
    if resposta not in ('p', 'i'):
        while resposta not in ('p', 'i'):
            print('-=-' * 23)
            print('Escolha inválida... Tente outra vez...')
            resposta = str(input('Por favor, escolha entre Par ou Impar [P/I]: ')).strip().lower()[0]
    print('-=-'*23)
    total = pc + num
    print(f'Sua escolha foi {num} e o computador escolheu {pc} dando um total de {total}.')
    if total % 2 == 0:
        print(f'O número {total} é PAR.')
        if resposta == 'i':
            print('Você PERDEU!!!')
            break
        elif resposta == 'p':
            print(f'Você VENCEU!!! Continue jogando.')
            qtd += 1
    else:
        print(f'O número {total} é IMPAR.')
        if resposta == 'p':
            print('Você PERDEU!!!')
            break
        elif resposta == 'i':
            print(f'Você Venceu!!! Continue jogando.')
            qtd += 1
    print('-=-'*23)
print('='*69)
print(f'Fim do programa. Você acertou {qtd} vezes.')
print('='*69)
