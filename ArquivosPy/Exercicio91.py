from random import randint
from operator import itemgetter
from time import sleep
maior = 0
TodasAsJogadas = {'Jogador 1': randint(1,6), 'Jogador 2': randint(1,6), 'Jogador 3':randint(1,6), 'Jogador 4': randint(1,6)}
ranking = {}
ranking = sorted(TodasAsJogadas.items(), key=lambda item: item[1], reverse=True)
print(f'{' ORDEM DAS JOGADAS ':=^42}')
for Jogador, Valor in TodasAsJogadas.items(): 
    sleep(1)
    print(f'{Jogador} tirou {Valor} no dado.')
print(f'{' VENCEDORES ':=^42}')
for Posicao, Jogada in enumerate(ranking):
    sleep(1)
    print(f'{Posicao+1}º Lugar = {Jogada[0]} que tirou {Jogada[1]} no dado.')
    