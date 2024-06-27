ListaGeral = []
print('-=-'*19)   
 
while True:
    resposta = ''
    GolsPorPartida = []
    SomaDosGols = 0
    Dados = {}
    Dados['Nome'] = str(input('Nome do jogador: '))
    Dados['QuantidadeDePartidas'] = int(input(f'Quantas partidas {Dados['Nome']} jogou?'))
    for Contador in range(Dados['QuantidadeDePartidas']):
        GolsPorPartida.append(int(input(f'Quantos gols marcados na partida {Contador+1}: ')))
        SomaDosGols += GolsPorPartida[Contador]
    Dados['GolsPorPartida'] = GolsPorPartida[:]
    Dados['SomaTotalDeGols'] = SomaDosGols
    ListaGeral.append(Dados)
    
    if resposta not in ('s', 'n'):
        while resposta not in ('s', 'n'):
            resposta = str(input('Quer continuar [s/n]? '))
    print('-=-'*19)    
    if resposta == 'n':
        break
                    
print(f'{"Nº":<2} | {"Nome":^14} | {"Gols":^8} | {"Total":^7}')
print('-=-'*19)
for Indice, DadosJogadorUnico in enumerate(ListaGeral):
    print(f'{Indice+1:>2} {DadosJogadorUnico['Nome']:^17} {DadosJogadorUnico['GolsPorPartida']} {DadosJogadorUnico['SomaTotalDeGols']:^10}')
    print()

while True:
    resposta = int(input('Digite o Indice do Jogador: '))
    if resposta == 999:
        break
    if resposta <= 0 or resposta > len(ListaGeral):
        print('Respota Inválida. Tente Novamente...')
    else:
        for Indice, DadosJogadorUnico in enumerate(ListaGeral):
            for chave, valor in DadosJogadorUnico.items():
                if Indice == resposta-1:
                        if chave == 'GolsPorPartida':
                                for numerodocaralho, goldocaralho in enumerate(valor):
                                    print(f'{numerodocaralho+1}º Jogo: {goldocaralho} gol(s).')
z