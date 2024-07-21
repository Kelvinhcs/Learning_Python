listagem = ('Abacaxi', 'Sofa', 'Elefante', 'Livro', 'Janela', 'Mesa', 'Casa', 'Ovo', 'Cadeira', 'Porta')
for palavra in listagem:
    print(f'\nNa palavra {palavra} temos: ', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

            
    