ListaGeral = []
ListaDasMulheres = []
ListaIdadeAcimaDaMedia =[]
SomaTotal = 0

print('-=-'*19)    
while True:
    resposta = ''
    DadosDaPessoa = {}
    DadosDaPessoa['Nome'] = str(input('Digite o nome: ')).strip()
    DadosDaPessoa['Genero'] = str(input('Digite o seu gênero [m/f]: ')).strip().lower()[0]  
    DadosDaPessoa['Idade'] = int(input('Digite a idade: '))
    if DadosDaPessoa['Genero'] == 'f':
        ListaDasMulheres.append(DadosDaPessoa.copy()['Nome'])
    SomaTotal += DadosDaPessoa['Idade']
    ListaGeral.append(DadosDaPessoa.copy())
    if resposta not in ('s', 'n'):
        while resposta not in ('s', 'n'):
            resposta = str(input('Quer continuar [s/n]? '))
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
