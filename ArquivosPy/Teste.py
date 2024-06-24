#ListaGeral = [['Pedro',[9.5, 5.2]], ['Kelvin', [6.2, 5.0]], ['MatGx'[10.0, 5.0]]]
#ListaGeral = [[9.5, 5.2]]
ListaGeral = []
placeholder = []
for c in range(0, 2):
    placeholder.clear()
    NomeDigitado = [str(input('Nome do aluno: ')).strip().capitalize()]
    print(NomeDigitado)
    Notas = [float(input(f'Digite a 1ª nota: ')), float(input(f'Digite a 1ª nota: '))]
    ListaGeral.append(NomeDigitado[:])
    print(Notas)
    ListaGeral.append(Notas[:])
    print(ListaGeral)
    ListaGeral

[[9.5, 5.2, ['Pedro']]]
###encontrei a opção de gerar uma lista vazia antes e apagala para assim poder utilizar o indice
"""
ListaGeral = []
placeholder = []
for c in range(0, 2):
    placeholder.clear()
    NomeDigitado = str(input('Nome do aluno: ')).strip().capitalize()
    Nota1 = float(input(f'Digite a 1ª nota: '))
    Nota2 = float(input(f'Digite a 2ª nota: '))
    placeholder.append(Nota1)
    placeholder.append(Nota2)
    ListaGeral.append(list('nada'))
    ListaGeral[c].clear()
    ListaGeral[c].append(placeholder[:])
    ListaGeral[c].append(NomeDigitado)
print(ListaGeral)
"""