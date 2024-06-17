nome = str(input("Qual é o seu nome?: ")).strip()
if nome.lower() == 'gustavo':
    print("Quem nome Bonito!")
elif nome.lower() == 'maria' or nome.lower() == 'joao':
    print("Que nome comum :0")
elif nome.lower() in 'jorge antonio cleber kelvin':
    print('Conheco algumas pessoas com esse nome também')
else:
    print("Seu nome é bem normal :(")
print(f"Tenha um bom dia, {nome}!")