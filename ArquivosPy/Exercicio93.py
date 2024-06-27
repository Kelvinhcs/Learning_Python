Dados = {}
GolsPorPartida = []
SomaDosGols = 0

Dados['Nome'] = str(input('Nome do jogador: '))
Dados['QTDPartidas'] = int(input(f'Quantas partidas {Dados['Nome']} jogou?'))

for contador in range(Dados['QTDPartidas']):
    GolsPorPartida.append(int(input(f'Quantos gols marcados na partida {contador+1}: ')))
    SomaDosGols += GolsPorPartida[contador]
    
Dados['QTDGols'] = GolsPorPartida[:]
Dados['TotalGols'] = SomaDosGols

print(f'{Dados['Nome']} marcou {Dados['TotalGols']} em sua carreira')
print(f'Em seus incriveis {Dados['QTDPartidas']} jogos.')
print(f'Respectivamente em cada partida seus gols foram:')

for indice, coisa in enumerate(GolsPorPartida):
    print(f'Partida {indice+1}: {coisa}')
    