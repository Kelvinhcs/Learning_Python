from json import load,dump
def saida():
    print('\033[0;31mO Usuário decidiu encerrar o programa...\033[')
    print('\033[0;31mEncerando...\033[m')
    exit()


def erro():
    print('\033[0:31mERRO! Tente digitar novamente...\033[m')
    
    
def CarregarDadosLocalmente(NomeDoArquivo):
    try:
        with open(NomeDoArquivo, 'r') as Arquivo:
            return load(Arquivo)
    except:
        return []


def CadastrarNovoUsuario(VarDadosLocais):
    global UltimosDigitados
    while True:
        while True:
            try:
                nome = str(input('Digite o nome: ')).strip()
            except KeyboardInterrupt:
                saida()
            except:
                erro()
            else:
                break
        while True:
            try:
                idade = int(input('Digite a idade: '))
            except KeyboardInterrupt:
                saida()
            except:
                erro()
            else:
                break
        print(f'{' Ultimos Registros ':=^60}')
        UltimosDigitados = {'nome':nome, 'idade':idade}
        print(f'{f'Nome: {UltimosDigitados['nome']}':^60}')
        print(f'{f'Idade: {UltimosDigitados['idade']}':^60}')
        print('='*60)
        print('[1] Manter Dados Atuais\n[2] Excluir e tentar novamente')
        while True:
            try:
                escolha = int(input('Qual sua escolha?: '))
            except KeyboardInterrupt:
                saida()
            except:
                erro()
            else:
                if escolha in (1,2):
                    break
                else:
                    continue
        if escolha == 1:
            print('='*60)
            VarDadosLocais.append(UltimosDigitados)
            break
        if escolha == 2:
            print('='*60)
            UltimosDigitados.clear()
            continue
        
    
    
def Salvar(VarDadosLocais, NomeDoArquivo):
    try:
        with open(NomeDoArquivo, 'w') as Arquivo:
            dump(VarDadosLocais, Arquivo, indent=4)
    except KeyboardInterrupt: 
        saida()
    except Exception as error:
        print('Não consegui salvar no arquivo por algum motivo...')
        print('Calma. Os dados ainda estão armazenados localmente')
        print(error)
        print('='*60)

def MostrarDadosDaVarLocal(VarDadosLocais):
    if not VarDadosLocais:
        print('Não foram encontrados dados para serem mostrados.')
        print('='*60)
    print(f'{'Nome':^30} {'Idade':^30}')
    for dicionario in VarDadosLocais:
        print(f'{dicionario['nome']:^30}  {dicionario['idade']:^29}')
    print('='*60)
