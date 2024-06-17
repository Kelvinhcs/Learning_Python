from time import sleep
from datetime import datetime
qtdmenores = 0
qtdmaiores = 0
valido = 0
data = datetime.now().year
print('-=-=-=-=-=-=-=-=-=- Bem Vindo -=-=-=-=-=-=-=-=-=-')
for c in range(1, 8):
    nasc = int(input(f'Digite O {c}º ano de nascimento: '))
    if nasc < 0 or nasc > datetime.now().year:
        print('Ano de nascimento inválido...')
    else:
        aniversario = str(input('Você fez aniversário este ano?(s/n): ')).strip().lower()
        if aniversario not in ('s', 'n'):
            print('Opção inválida...')
        else:
            if aniversario == 'n':
                valido += 1
                idade = (data - nasc) - 1
                if idade >= 18:
                    qtdmaiores += 1
                if idade < 18:
                    qtdmenores += 1
            elif aniversario == 's':
                valido += 1
                idade = data - nasc
                if idade >= 18:
                    qtdmaiores += 1
                if idade < 18:
                    qtdmenores += 1
    print('-=' * 24, end='')
    print('-')
if valido >= 1:
    sleep(1)
    print('Analisando...')
    sleep(2)
    print(f'Você digitou {valido} entradas VÁLIDAS.')
    print(f'Constam {qtdmaiores} Maiores de Idade.')
    print(f'Constam {qtdmenores} Menores de Idade.')
    print('-=' * 24, end='')
    print('-')
else:
    print('Desligando sistema...')
    sleep(2)
