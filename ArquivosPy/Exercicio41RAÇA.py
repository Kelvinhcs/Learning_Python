from datetime import datetime
nasc = int(input('Digite o ano do seu nascimento: '))
aniversario = int(input('[0] Sim\n[1] Não\nVocê já fez aniversário esse ano?: '))
if nasc < 0:
    print('Desconsidere todos os calculos, digite um ano válido da próxima vez.')
if aniversario == 1:
    idade = (datetime.today().year - nasc) - 1
    if idade <= 9:
        categoria = 'Mirim'
    elif idade <= 14:
        categoria = 'Infantil'
    elif idade <= 19:
        categoria = 'Júnior'
    elif idade <= 25:
        categoria = 'Sênior'
    elif idade > 25:
        categoria = 'Master'
if aniversario == 0:
    idade = datetime.today().year - nasc
    if idade <= 9:
        categoria = 'Mirim'
    elif idade <=14:
        categoria = 'Infantil'
    elif idade <= 19:
        categoria = 'Júnior'
    elif idade <= 25:
        categoria = 'Sênior'
    elif idade > 25:
        categoria = 'Master'
print(f'Você tem {idade} anos\nE está na categoria {categoria}.')
