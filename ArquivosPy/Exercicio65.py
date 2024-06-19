num = int(input('Digite um número: '))
somatotal = maior = menor = num
contador = 1
resposta = str(input('Quer continuar[s/n]? ')).strip().lower()
while resposta == 's':
    num = int(input('Digite um número: '))
    somatotal += num
    contador += 1
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    resposta = str(input('Quer continuar[s/n]? ')).strip().lower()
media = somatotal / contador
print(f'Você digitou {contador} números e a média foi {media}')
print(f'O Maior valor foi {maior} e o menor foi {menor}')
