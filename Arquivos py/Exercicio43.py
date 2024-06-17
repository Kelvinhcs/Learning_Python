import math
peso = float(input('Digite o seu peso atual: '))
altura = float(input('Digite a sua altura em metros:(Ex: 1.75, 1.90) '))
imcpow = peso / math.pow(altura,2)
imc = peso / (altura*altura)
print(imc)
print(imcpow)
if imc < 10:
    print('Os dados digitados foram inválidos: ')
else:
    print(f'O seu IMC é de {imc:.1f}.')
    if imc <= 18.4:
        print('Você está classificado como ABAIXO DO PESO.')
    elif imc <= 25:
        print('Você está classificado como PESO IDEIAL.')
    elif imc <= 30:
        print('Você está classificado como SOBREPESO.')
    elif imc <= 40:
        print('Você está classificado como OBESIDADE I.')
    elif imc > 40:
        print('Você está classificado como OBESIDADE MÓRBIDA.')