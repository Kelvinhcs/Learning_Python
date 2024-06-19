soma = 0
qtd = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        qtd += 1
        soma += c
print(f'A quantidade final de valores é {qtd}\nE a soma total é de {soma}')
