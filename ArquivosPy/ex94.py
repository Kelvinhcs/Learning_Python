ListaGeral = []
ListaDasMulheres = []
ListaIdadeAcimaDaMedia =[]
SomaTotal = 0

print('-=-'*19)    
while True:
    DadosDaPessoa = {}
    DadosDaPessoa['Nome'] = str(input('Digite o nome: ')).strip()
    while True:
        DadosDaPessoa['Genero'] = str(input('Digite o seu gênero [m/f]: ')).strip().lower()[0]
        if DadosDaPessoa['Genero'] in 'mf':
            break
        print('Resposta Inválida. Tente novamente...')
    DadosDaPessoa['Idade'] = int(input('Digite a idade: '))
    if DadosDaPessoa['Genero'] == 'f':
        ListaDasMulheres.append(DadosDaPessoa.copy()['Nome'])
    SomaTotal += DadosDaPessoa['Idade']
    
    ListaGeral.append(DadosDaPessoa.copy())
    while True:
        resposta = str(input('Quer continuar [s/n]? ')).strip().lower()[0]
        if resposta in 'sn':
            break
        print(f'ERRO! respostas aceitas: [s/n]')
    print('-=-'*19)    
    if resposta == 'n':
        break

Media = SomaTotal / len(ListaGeral)   
                   
for Indice, DadosDaPessoaSeparado in enumerate(ListaGeral):
    for chave, valor in DadosDaPessoaSeparado.items():    
        if chave == 'Idade' and valor > Media:
            ListaIdadeAcimaDaMedia.append([ListaGeral[:][Indice]['Nome'], ListaGeral[:][Indice]['Idade']])
            
print(f'Foram cadastradas ao total {len(ListaGeral)} pessoas.')
print(f'A média de idade do grupo é: {Media:.2f}.')
print(f'Aqui está a o nome de todas as mulheres da lista: {ListaDasMulheres}.')
print()
print(f'Essas são as pessoas que tem a idade acima da média do grupo: {ListaIdadeAcimaDaMedia}.')
print('-=-'*19)    
