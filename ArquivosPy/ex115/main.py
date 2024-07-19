import funcionalidades
NomeDoArquivo = 'dados.json'
DadosAnteriores = funcionalidades.CarregarDadosLocalmente(NomeDoArquivo)
DadosLocais = funcionalidades.CarregarDadosLocalmente(NomeDoArquivo)


print(f'{' Exercicio Mais Dificil que eu já fiz ':=^60}')
while True:
    print("""[1] Cadastrar Novos Usuários
[2] Mostrar Usuários Cadastrados Anteriormente
[3] Encerrar programa""")
    while True:
        try:
            escolha = int(input('Qual a sua escolha?: '))
        except KeyboardInterrupt:
            funcionalidades.saida(DadosLocais, NomeDoArquivo)
        except:
            funcionalidades.erro()
        else:
            if escolha in (1,2,3):
                break
            else:
                continue
    print('='*60)
    if escolha == 1:
        funcionalidades.CadastrarNovoUsuario(DadosLocais, NomeDoArquivo)
    if escolha == 2:
        funcionalidades.MostrarDadosAnteriores(DadosAnteriores)
    if escolha == 3:
        funcionalidades.saida(DadosLocais, NomeDoArquivo)
    