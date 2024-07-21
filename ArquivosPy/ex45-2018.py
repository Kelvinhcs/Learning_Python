import time
from random import randint
pc = randint(0, 2)
itens = ('Pedra','Papel','Tesoura')
n = int(input('''Suas Opções
[0] Pedra
[1] Papel
[2] Tesoura
Escolha uma opção: '''))
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO')
time.sleep(1)
print('-=-' * 10)
print('Você Escolheu {}'.format(itens[n]))
print('O Computador Escolheu {}'.format(itens[pc]))
if n == 0 and pc == 2:
    print('Você Venceu')
if n == 0 and pc == 1:
    print('O Computador Venceu')
if n == 0 and pc == 0:
    print('O Jogo Empatou')
if n == 1 and pc == 0:
    print('Você Venceu')
if n == 1 and pc == 1:
    print('O Jogo Empatou')
if n == 1 and pc == 2:
    print('O Computador Venceu')
if n == 2 and pc == 0:
    print('O Computador Venceu')
if n == 2 and pc == 1:
    print('Você Venceu')
if n == 2 and pc == 2:
    print('O Jogo Empatou')
print('-=-' * 10)