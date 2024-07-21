def ficha(n=0, g=0):
    if n == 0 or n.strip() == '':
        n = '<desconhecido>'
    if g.isnumeric() == False:
        g = 0
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


nome = input('Digite o nome do jogador: ')
gols = input(f'Digite quantos gols fez: ')
ficha(nome, gols)


#Existe a opção também de verificar o len da frase pra caso seja 0 declarar como desconhecido