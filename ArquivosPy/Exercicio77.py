listagem = ('Abacaxi', 'Sofa', 'Elefante', 'Livro', 'Janela', 'Mesa', 'Casa', 'Ovo', 'Cadeira', 'Porta')
for c in listagem:
    qtda = qtde = qtdi = qtdo = qtdu = 0
    print(f'Na Palavra {c} tem as Vogais: ',end='')
    if c.find('a') >= 0 or c.find('A') >= 0:
        qtda = 1
    if c.find('e') >= 0 or c.find('E') >= 0:
        qtde = 1
    if c.find('i') >= 0 or c.find('I') >= 0:
        qtdi = 1
    if c.find('o') >= 0 or c.find('o') >= 0:
        qtdo = 1
    if c.find('u') >= 0 or c.find('U') >= 0:
        qtdu = 1
    print('A'*qtda, 'E'*qtde, 'I'*qtdi, 'O'*qtdo, 'U'*qtdu)
