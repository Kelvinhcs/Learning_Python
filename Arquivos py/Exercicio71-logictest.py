saque = int(input('Valor do saque: '))
intermed = saque
notas50 = intermed // 50
intermed = intermed - (50*notas50)
notas20 = intermed // 20
intermed = intermed - (20*notas20)
notas10 = intermed // 10
intermed = intermed - (10*notas10)
notas1 = intermed % 10
print(f'Na tentativa de sacar R${saque}\nNosso caixa lhe entregou:')
print(f'{notas50} notas de R$50')
print(f'{notas20} notas de R$20')
print(f'{notas10} notas de R$10')
print(f'{notas1} notas de R$1')
