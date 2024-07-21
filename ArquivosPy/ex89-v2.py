ListaGeral = []
print('-=-'*11)

while True:
    #le o nome, 2 notas, Calcula a media e joga tudo na ListaGeral
    resposta = ''
    NomeDigitado = str(input('Nome do aluno: ')).strip()
    Nota1 = float(input(f'Digite a 1ª nota: ')) 
    Nota2 = float(input(f'Digite a 2ª nota: '))
    Media2Notas = (Nota1+Nota2) / 2
    ListaGeral.append([NomeDigitado,[Nota1, Nota2], Media2Notas])
    #codigo padrão de validação de resposta 
    if resposta not in ('s', 'n'):
        while resposta not in ('s', 'n'):
            resposta = str(input('Quer continuar[s/n]? ')).strip().lower()[0]
    print('-=-'*11)
    if resposta == 'n':
        break
    
#obtem a posição do aluno na ListaGeral e armazena em Indice, e também separa seus dados em DadosDoAluno
print('Nº | Nome Do Aluno | Média')
for Indice, DadosDoAluno in enumerate(ListaGeral):
    print(f'{Indice+1:<2} -> {DadosDoAluno[0]:^13} -> {DadosDoAluno[2]}')
print('-=-'*11)

#mostra a nota individual do aluno com base no indice digitado
while True:
    EscolhendoAluno = int(input('Digite o número do aluno para mostrar suas notas individuais [999 Interompe]: '))
    if EscolhendoAluno == 999:
        break
    if EscolhendoAluno <= 0 or EscolhendoAluno > len(ListaGeral):
        print('Escolha Inválida. Tente Novamente...')
    else:     
        print(f'As notas individuais do aluno {ListaGeral[EscolhendoAluno-1][0]} foram {ListaGeral[EscolhendoAluno-1][1]}.')
        print('-=-'*11)
print('Encerando...')
print('-=-'*11)
