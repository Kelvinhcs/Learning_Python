from datetime import date

Dados = {}
AnoAtual = date.today().year

Dados['Nome'] = str(input('Digite o nome: ')).strip()
Dados['Nascimento'] = int(input('Digite o ano de nascimento: '))
Dados['Idade'] = AnoAtual - Dados['Nascimento']

Dados['Ctps'] = int(input('Digite o número da sua CTPS [0 para nenhuma]: '))
if Dados['Ctps'] > 0:
    Dados['AnoDeContratação'] = int(input('Ano da sua primeira contratação: '))
    Dados['Salario'] = float(input('Digite o seu salários: '))
    Dados['AnoDaAposentadoria'] = Dados['AnoDeContratação'] + 35
    Dados['IdadeAposentadoria'] = (Dados['AnoDaAposentadoria'] - AnoAtual) + Dados['Idade']
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

for Referencia, Valores in Dados.items():
    if Referencia == 'IdadeAposentadoria' and Dados['IdadeAposentadoria'] <= Dados['Idade']:
        print(f'{Referencia} = {Valores} VOCE JÁ PODE SE APOSENTAR')
    else:
        print(f'{Referencia} = {Valores}')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
