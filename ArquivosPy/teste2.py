import json

def carregar_dados(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def salvar_dados(nome_arquivo, dadoslocais):
    with open(nome_arquivo, 'w') as f:
        json.dump(dadoslocais, f, indent=4)

def cadastrar_pessoa(dadoslocais):
    nome = input('Digite o nome: ')
    idade = input('Digite a idade: ')
    dadoslocais.append({'nome': nome, 'idade': idade})

def mostrar_dados(dadoslocais):
    if not dadoslocais:
        print('Nenhum dado cadastrado.')
    else:
        for pessoa in dadoslocais:
            print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}")

def main():
    nome_arquivo = 'dados.json'
    VarDadosLocais = carregar_dados(nome_arquivo)
    
    while True:
        print("\nMenu:")
        print("1. Cadastrar Nome e Idade")
        print("2. Mostrar Dados Cadastrados")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_pessoa(VarDadosLocais)
            salvar_dados(nome_arquivo, VarDadosLocais)
        elif opcao == '2':
            mostrar_dados(VarDadosLocais)
        elif opcao == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()