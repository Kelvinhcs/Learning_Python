resposta = int(input('Digite um número inteiro [999 para parar]: '))
cont = 0
soma = 0
while resposta != 999:
    cont += 1
    soma += resposta
    resposta = int(input('Digite um número inteiro [999 para parar]: '))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')
