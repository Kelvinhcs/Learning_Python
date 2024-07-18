import funcionalidades
NomeDoArquivo = 'dados.json'
DadosLocais = funcionalidades.CarregarDadosLocalmente(NomeDoArquivo)
print(f'{' Exercicio Mais Dificil que eu já fiz ':=^60}')
while True:
    print("""[1] Cadastrar Novos Usuários
[2] Mostrar Usuários Cadastrados
[3] Encerrar programa""")
    while True:
        try:
            escolha = int(input('Qual a sua escolha?: '))
        except KeyboardInterrupt:
            funcionalidades.saida()
        except:
            funcionalidades.erro()
        else:
            if escolha in (1,2,3):
                break
            else:
                continue
    print('='*60)
    if escolha == 1:
        funcionalidades.CadastrarNovoUsuario(DadosLocais)
        funcionalidades.Salvar(DadosLocais, NomeDoArquivo)
    if escolha == 2:
        funcionalidades.MostrarDadosDaVarLocal(DadosLocais)
    if escolha == 3:
        funcionalidades.saida()



#Queria que salvar fosse uma ação ativa, nao um passivo do cadastro
#       Tentar Criar uma outra Lista placeholder pra colocar os dados do cadastro
#       Ao invés de colocar os dados do cadastro dentro da lista geral local
#       E então verificar como o arquivo .json se comporta sobre isso
#       E também se não quebra a maneira com que ele vai mostrar os dados
#Gostaria que pudesse ser visualizado a lista anterior aos escritos na run(cosequencia da feature acima)
#       Não tem muito oque dizer, se eu for escrever o da run em outra variavel
#       Pra mostrar o antigo sem ela é só carregar os dados do arquivo