r1 = float(input('Digite o primeiro lado:'))
r2 = float(input('Digite o segundo lado: '))
r3 = float(input('Digite o terceiro lado: '))
print('-=-'*22)
if r1 < r2+r3 and r2 < r1+r3 and r3 < r2+r1:
    if r1 == r2 and r1 == r3:
        print('Este triângulo possui os 3 lados iguais\nPor tanto ele é um Equilátero')
    elif r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2:
        print('Este triângulo possui 2 lados iguais e 1 diferente\nPortanto ele é um Isósceles')
    #Existe a opção de utilizar else, já que é a unica opção restante, mas prefiro especificar
    elif r1 != r2 and r1 != r3:
        print('Todos os lados deste triângulo são diferentes\nPortanto ele é um Escaleno')
else:
    print('Triângulo inválido tente uma outra vez.')
