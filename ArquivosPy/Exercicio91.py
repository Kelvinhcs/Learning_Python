from random import randint
maior = 0
TodasAsJogadas = {'Jogador1': randint(1,6), 'Jogador2': randint(1,6), 'Jogador3':randint(1,6), 'Jogador4': randint(1,6)}

Sorteio = dict(sorted(TodasAsJogadas.items(), key=lambda item: item[1]))
print('-=-=-=--=-'*3)
print(TodasAsJogadas)
print(Sorteio) 
print('-=-=-=--=-'*3)

print('-=-=-=--=-'*3)