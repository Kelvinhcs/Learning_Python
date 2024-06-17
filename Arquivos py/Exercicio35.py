r1 = float(input("Digite a primeira reta: "))
r2 = float(input("Digite a segunda reta: "))
r3 = float(input("Digite a terceira reta: "))
if r3 < r1+r2 and r2 < r1+r3 and r1 < r2+r3:
    print("Esse triangulo é valido")
else:
    print("Ele nao é valido")