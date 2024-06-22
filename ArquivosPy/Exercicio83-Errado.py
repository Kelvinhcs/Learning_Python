listagem = list(str(input('Digite uma expressão: ')).strip())
if listagem.count('(') != listagem.count(')'):
    print('Expresão inválida.')
else:
    print('Expresão válida.')