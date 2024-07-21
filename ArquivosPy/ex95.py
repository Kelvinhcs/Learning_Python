ListaGeral = []
print('-=-'*19)  
#faz a leitura do nome, quantidade de partidas, e dos gols por partida. Tudo vai pro dict e dps pra ListaGeral  
while True:
    GolsPorPartida = []
    Dados = {}
    Dados['Nome'] = str(input('Nome do jogador: '))
    QuantidadeDePartidas = int(input(f'Quantas partidas {Dados['Nome']} jogou?'))
    for Contador in range(QuantidadeDePartidas):
        GolsPorPartida.append(int(input(f'Quantos gols marcados na partida {Contador+1}: ')))
    Dados['GolsPorPartida'] = GolsPorPartida[:]
    Dados['TotalDosGols'] = sum(GolsPorPartida)
    ListaGeral.append(Dados)
    #confirmação da resposta padrao
    while True:
        resposta = str(input('Quer continuar [s/n]? ')).strip().lower()[0]
        if resposta in 'sn':
            break
        print(f'ERRO! respostas aceitas: [s/n]')
    print('-=-'*19)    
    if resposta == 'n':
        break

#printando os valores semi organizados          
print(f'{"Nº":<2} | {"Nome":^16} | {"Gols":^16} | {"Total"}')
print('-=-'*19)
for Indice, DadosJogadorUnico in enumerate(ListaGeral):
    print(f'{Indice:>2}  ',end='')
    for dadoemcasa in DadosJogadorUnico.values():
        print(f'{str(dadoemcasa):<18} ',end='')
    print()
#recebendo valor para detalhar os dados
while True:
    resposta = int(input('Digite o Indice do Jogador: '))
    if resposta == 999:
        break
    if resposta <= 0 or resposta > len(ListaGeral):
        print('Respota Inválida. Tente Novamente...')
    else: #separa a key e o value do dicionário no indice escolhido
        for identificador, valor in enumerate(ListaGeral[resposta-1]['GolsPorPartida']):
            print(f' -{identificador+1}º Jogo: teve {valor} gol(s).')
                    