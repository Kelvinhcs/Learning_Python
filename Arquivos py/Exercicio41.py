from datetime import datetime
from time import sleep
nasc = int(input('Digite o ano do seu nascimento: '))
#separar as datas de nascimento inválidos
if nasc < 0 or nasc > datetime.today().year:
    print('Digite um ano válido por favor.')
else:
    aniversario = input('Você já fez aniversário esse ano?(s/n): ').strip().lower()
    print('-=-'*18)
    #faz a validação da entrada
    if aniversario != 's' and aniversario != 'n':
        print('Digite uma opção válida da próxima por favor.')
    idade = datetime.today().year - nasc
    #alterar a variável para a idade correta
    if aniversario == 'n':
        idade -= 1
    #executar os codigo caso seja algo válido
    elif aniversario == 's' or aniversario == 'n':
        print(f'Você tem {idade} anos.')
        if idade <= 9:
            print('Categoria MIRIM\nAté 9 anos.')
        elif idade <= 14:
            print('Categoria INFANTIL\nDe 10 a 14 anos.')
        elif idade <= 19:
            print('Categoria JUNIOR\nDe 15 a 19 anos.')
        elif idade <= 25:
            print('Categoria SÊNIOR\nDe 20 a 25 anos.')
        elif idade > 25:
            print('Categoria MASTER\nMaior que 25 anos.')
    print('-=-'*18)
    sleep(1)
    print('')
    print('Desligando Sistema...')
    sleep(2)
