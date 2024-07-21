from time import sleep
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
resposta = 0
while resposta != 5:
    print('-=-'*16)
    print('[1] Somar\n[2] Dividir\n[3] Maior\n[4] Novos números\n[5] Sair do programa')
    resposta = int(input('Selecione a opção desejada: '))
    print('-=-'*16)
    if resposta == 1:
        print(f'O resultado da opção desejada é \n{n1} + {n2} = {n1+n2}.')
    elif resposta == 2:
        print(f'A divisão do número {n1} por {n2} resulta em {n1/n2:.1f}.')
    elif resposta == 3:
        if n1 > n2:
            print(f'O número {n1} é maior em relação a {n2}.')
        elif n2 > n1:
            print(f'O número {n2} é maior em relação a {n1}.')
        elif n1 == n2:
            print(f'Não existe número maior entre os digitados\nAmbos os números são equivalentes.')
    elif resposta == 4:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
    elif resposta == 5:
        print('Finalizando...')
        print('-=-'*16)
    if resposta not in (1, 2, 3, 4, 5):
        print('Opção inválida... Tente novamente: ')
    sleep(1)
print('Fim do programa.\nObrigado por utilizar!')
