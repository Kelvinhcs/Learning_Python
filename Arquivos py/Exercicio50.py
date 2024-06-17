soma = 0
qtd = 0
for c in range(1,7):
    num = int(input('Digite um número: '))
    if num % 2 ==0:
        soma += num
        qtd += 1
print(f'O total dos {qtd} itens é {soma}.')