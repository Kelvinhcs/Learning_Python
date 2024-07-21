from time import sleep #Adicionei tempo e -=- para ficar mais bonito
vel = float(input("Digite a velocidade do veículo: "))
multa = (vel-80) * 7
print('-=-'*27)
sleep(2)
if vel > 80:
    print("Você exedeu o limite de 80km/h e foi multado com base nos seguinte parâmetros:")
    print("A multa é calculada com base em R$7.00 para cada Kilometro por hora exedente.")
    print(' ')
    sleep(2)
    print(f"Seu veículo estava a {vel}Km/h isso excede {vel-80}Km/h do limite.")
    print("Você está condenado a pagar R${:.2f} de multa.".format(multa))
    print('-=-' * 27)
    sleep(2)
print("Tenha um bom dia\nDirija com segurança")