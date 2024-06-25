#ListaGeral = [['Pedro',[9.5, 5.2]], ['Kelvin', [6.2, 5.0]], ['MatGx'[10.0, 5.0]]]
#ListaGeral = [[9.5, 5.2]]
ListaGeral = []
placeholder = []
for c in range(0, 2):
    placeholder.clear()
    NomeDigitado = [str(input('Nome do aluno: ')).strip().capitalize()]
    ListaGeral.append(NomeDigitado[:])
    print(ListaGeral)
    Notas = [float(input(f'Digite a 1ª nota: ')), float(input(f'Digite a 1ª nota: '))]
    ListaGeral.insert(c+1, Notas[:])
    print(ListaGeral)
