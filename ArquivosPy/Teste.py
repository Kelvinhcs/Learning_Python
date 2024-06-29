while True:
    resposta = str(input('Quer continuar [s/n]? '))
    if resposta in 'sn':
        break
    print(f'ERRO! respostas aceitas: [s/n]')
        
        
        
resposta = ''
if resposta not in 'sn':
    while resposta not in 'sn':
        resposta = str(input('Quer continuar [s/n]? '))
    print(f'ERRO! respostas aceitas: [s/n]')

        