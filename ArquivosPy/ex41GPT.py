from datetime import datetime
nasc = int(input('Digite o ano do seu nascimento: '))
ano_atual = datetime.today().year
if nasc < 0 or nasc > ano_atual:
    print('Digite um ano válido por favor.')
else:
    fez_aniversario = input('Você já fez aniversário este ano? (s/n): ').strip().lower()
    idade = ano_atual - nasc
    if fez_aniversario == 'n':
        idade -= 1
    print(f'Você tem {idade} anos.')
# Determinar e exibir a categoria do usuário com base na idade
    if idade <= 9:
        print('Categoria MIRIM\nAté 9 anos.')
    elif idade <= 14:
        print('Categoria INFANTIL\nDe 10 a 14 anos.')
    elif idade <= 19:
        print('Categoria JUNIOR\nDe 15 a 19 anos.')
    elif idade <= 25:
        print('Categoria SÊNIOR\nDe 20 a 25 anos.')
    else:
        print('Categoria MASTER\nMaior que 25 anos.')
