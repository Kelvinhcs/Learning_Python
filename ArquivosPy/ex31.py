distancia = float(input("Digite a distância da viagem em km: "))
if distancia <= 200:
    preco = distancia * 0.50
    print("Por andar {}km a R$0.50 será cobrado R${:.2f}".format(distancia, preco))
else:
    preco = distancia * 0.45
    print("Por andar {}km a R$0.45 será cobrado R${:.2f}".format(distancia, preco))