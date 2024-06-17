#na minha tentativa eu tentei ao inves de utilizar um while infinito
#colocar um "while (saque - 50) > 0"
#em minha defesa é tipo isso, soq com while
notas50 = notas20 = notas10 = notas1 = 0
saque = int(input('Valor do saque: '))
placeholder = saque
while True:
    if placeholder >= 50:
        placeholder -= 50
        notas50 += 1
    else:
        if placeholder >= 20:
            placeholder -= 20
            notas20 += 1
        else:
            if placeholder >= 10:
                placeholder -= 10
                notas10 += 1
            else:
                if placeholder >= 1:
                    placeholder -= 1
                    notas1 += 1
                else:
                    break
print(f'Na tentativa de sacar R${saque}\nNosso caixa lhe entregou:')
if notas50 >= 1:
    print(f'{notas50} notas de R$50')
if notas20 >= 1:
    print(f'{notas20} notas de R$20')
if notas10 >= 1:
    print(f'{notas10} notas de R$10')
if notas1 >= 1:
    print(f'{notas1} notas de R$1')
