from time import sleep
from random import randint
advinhacao = int(input("Tente advinhar o número: "))
pc = randint(0,5)
print("-=-=-=-=- Calculando -=-=-=-=-")
sleep(3)
if advinhacao == pc:
    print(f"Parabéns, Você Digitou {advinhacao}\nE a máquina gerou {pc}\nLogo você ACERTOU.")
else:
    print(f"Que pena, Você Digitou {advinhacao}\nE a máquina gerou {pc}\nLogo você ERROU.")
sleep(2)
print("-=-=-=-=- Desligando -=-=-=--=-")
sleep(3)