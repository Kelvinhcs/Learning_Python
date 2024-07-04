def ficha(n='<desconhecido>', g=0):
    if n == '':
        n = '<desconhecido>'
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


nome = str(input('Digite o nome do jogador: ')).strip()
gols = int(input(f'Digite quantos gols fez: '))
ficha(nome, gols)