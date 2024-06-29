Dados = {}
GolsPorPartida = []

Dados['Nome'] = str(input('Nome do jogador: '))
Dados['QTDPartidas'] = int(input(f'Quantas partidas {Dados['Nome']} jogou?'))

for contador in range(Dados['QTDPartidas']):
    GolsPorPartida.append(int(input(f'Quantos gols marcados na partida {contador+1}: ')))
    
print(f'{Dados['Nome']} marcou {sum(GolsPorPartida)} gols em sua carreira em seus incriveis {Dados['QTDPartidas']} jogos.')
print(f'Respectivamente em cada partida seus gols foram:')

for indice, coisa in enumerate(GolsPorPartida):
    print(f' -Partida {indice+1}: {coisa} Gols.')