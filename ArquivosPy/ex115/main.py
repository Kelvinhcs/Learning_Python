import funcionalidades
NomeDoArquivo = 'dados.json'
DadosAnteriores = funcionalidades.CarregarDadosLocalmente(NomeDoArquivo)
DadosLocais = funcionalidades.CarregarDadosLocalmente(NomeDoArquivo)


while True:
    print(f'{' Gerenciador de Cadastros ':=^60}')
    print("""[1] Cadastrar Novos Usuários
[2] Mostrar usuários Cadastrados no banco de Dados
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
    if escolha == 1:
        print(f'{' Cadastramento ':~^60}')
        funcionalidades.CadastrarNovoUsuario(DadosLocais, NomeDoArquivo)
    if escolha == 2:
        print(f'{' Banco De Dados ':=^60}')
        funcionalidades.MostrarDadosAnteriores(DadosAnteriores)
    if escolha == 3:
        print('='*60)
        funcionalidades.saida(DadosLocais, NomeDoArquivo)
