maiorpos = 1
menorpos = 1
peso1 = float(input('Digite o 1º Peso: '))
menor = peso1
maior = peso1
for c in range(2, 6):
    peso = float(input(f'Digite o {c}º Peso: '))
    if peso > maior:
        maiorpos = c
        maior = peso
    if peso < menor:
        menor = peso
        menorpos = c
print(f'O maior peso digitado foi de {maior}kg\nNa Posição {maiorpos}')
print(f'O menor peso digitado foi de {menor}kg\nNa Posição {menorpos}')
