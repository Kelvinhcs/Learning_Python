from soundplay import playsound
from random import randint
print('-=-=-=-=-=-=- JO-KEN-PÔ -=-=-=-=-=-')
escolha = int(input("""[1] Pedra
[2] Papel
[3] Tesoura
Digite a opção desejada: """))
print('-=-'*12)
if escolha not in (1, 2, 3):
    print('Escolha inválida...')
else:
    pc = randint(1, 3)
    if escolha == pc:
        print("Vocês escolheram a mesma coisa!!")
        print("Eu vós declaro EMPATE!!")
    elif escolha == 1 and pc == 2:
        print("Você escolheu PEDRA.")
        print("A Máquina escolheu PAPEL.")
        print("Eu vós declaro DERROTA!!")
    elif escolha == 1 and pc == 3:
        print("Você escolheu PEDRA.")
        print("A Máquina escolheu TESOURA.")
        print("Eu vós declaro VITÓRIA!!")
    elif escolha == 2 and pc == 1:
        print("Você escolheu PAPEL.")
        print("A Máquina escolheu PEDRA.")
        print("Eu vós declaro VITÓRIA!!")
        playsound('C:/Users/Kelvin/Pictures/pasta do kelvin/jokenpocerto.mp3')
    elif escolha == 2 and pc == 3:
        print("Você escolheu PAPEL.")
        print("A Máquina escolheu TESOURA.")
        print("Eu vós declaro DERROTA!!")
    elif escolha == 3 and pc == 1:
        print("Você escolheu TESOURA.")
        print("A Máquina escolheu PEDRA.")
        print("Eu vós declaro DERROTA!!")
        playsound('C:/Users/Kelvin/Pictures/pasta do kelvin/jokenpocerto.mp3')
    elif escolha == 3 and pc == 2:
        print("Você escolheu TESOURA.")
        print("A Máquina escolheu papel.")
        print("Eu vós declaro VITÓRIA!!")
print('-=-'*12)
