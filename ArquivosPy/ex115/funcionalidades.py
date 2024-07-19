from json import load,dump
placeholder = []
def validacao(DadosLocais, NomeDoArquivo, msg, tipo=str):
    while True:
        try:
            digitado = tipo(input(msg))
        except KeyboardInterrupt:
            saida(DadosLocais, NomeDoArquivo)
        except:
            erro()
        else:
            return digitado

        
def saida(DadosLocais, NomeDoDataBase):
    print('\033[0;31mO Usuário decidiu encerrar o programa...\033[m')
    print(f'{' Encerramento ':*^60}')
    while True:
        try:
            escolha = int(input('[1] Enviar os dados salvos localmente para a DataBase\n[2] Ignorar a sessão atual\nQual sua escolha?: '))
        except KeyboardInterrupt:
            escolha = 2
            break
        except:
            erro()
        else: 
            if escolha in (1,2):
                break
    if escolha == 1:
        for item in placeholder:
            if item not in DadosLocais:
                DadosLocais.append(item)
        Salvar(DadosLocais, NomeDoDataBase)
        print('\033[0;31mEncerando...\033[m')
        print('*'*60)
        exit()
    elif escolha == 2:
        print('\033[0;31mDesconsiderando sessão atual.\033[m')
        print('\033[0;31mEncerando...\033[m')
        print(f'{' Encerramento ':*^60}')
        exit()


def erro():
    print('\033[0:31mERRO! Tente digitar novamente...\033[m')
    
    
def CarregarDadosLocalmente(NomeDoArquivo):
    try:
        with open(NomeDoArquivo, 'r') as Arquivo:
            return load(Arquivo)
    except:
        return []


def CadastrarNovoUsuario(DadosLocais, NomeDoArquivo):
    global placeholder
    while True:
        nome = validacao(DadosLocais, NomeDoArquivo, 'Digite o nome: ').strip()
        idade = validacao(DadosLocais, NomeDoArquivo, 'Digite a idade: ', tipo=int)
        print(f'{' Ultimos Dados Digitados ':~^60}')
        UltimosDigitados = {'nome':nome, 'idade':idade}
        placeholder.append(UltimosDigitados)
        print()
        for indice, item in enumerate(placeholder):
            if indice == len(placeholder)-1:
                print(f'{'\033[0;31mDados ainda não salvos localmente\033[m':^70}')
            else:
                print(f'{'\033[0;32mDado Cadastrado Localmente\033[m':^70}')
            print(f'{f'Nome: {item['nome']}':^60}')
            print(f'{f'Idade: {item['idade']}':^60}')
            print()
        print('~'*60)
        print('[1] Salvar Dado Localmente\n[2] Reescrever Ultimo Registro')
        while True:
            escolha = validacao(DadosLocais, NomeDoArquivo, 'Qual sua escolha?: ', tipo=int)
            if escolha in (1,2):
                break
        if escolha == 1:
            for item in placeholder:
                DadosLocais.append(item)
            break
        if escolha == 2:
            UltimosDigitados.clear()
            placeholder.pop()
            continue
        
    
def Salvar(DadosLocais, NomeDoArquivo):
    try:
        with open(NomeDoArquivo, 'w') as Arquivo:
            dump(DadosLocais, Arquivo, indent=4)
    except Exception as error:
        print('Desculpe, não consegui salvar no arquivo pelo motivo abaixo...')
        print(error)
        print('='*60)
        

def MostrarDadosAnteriores(VarDadosLocais):
    if not VarDadosLocais:
        print('Não foram encontrados dados para serem mostrados.')
        print('='*60)
    print(f'{'Nome':^30} {'Idade':^30}')
    for dicionario in VarDadosLocais:
        print(f'{dicionario['nome']:^30}  {dicionario['idade']:^29}')
