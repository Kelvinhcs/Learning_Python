Aluno = {}
Aluno['Nome'] = str(input('Digite o nome do aluno: ')).strip().capitalize()
Aluno['Media'] = float(input(f'Média de {Aluno["Nome"]}: '))
if Aluno['Media'] < 7:
    Aluno['Situacao'] = 'Reprovado'
if Aluno['Media'] >= 7:
    Aluno['Situacao'] = 'Aprovado'
print(f'O aluno {Aluno['Nome']} tem média {Aluno['Media']}.')
print(f'Portanto sua situação atual é: {Aluno['Situacao']}.')
