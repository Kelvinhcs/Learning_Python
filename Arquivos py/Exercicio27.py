nome = str(input("Digite o seu nome completo: ")).strip()
separacao = nome.split()
print(f"Seu primeiro nome é {separacao[0]}")
print(f"Seu último nome é {separacao[-1]}")

""""Guanabara Solve
n = str(input('Digite o seu nome completo: ')).strip()
nome = n.split()
print("Seu primeiro nome é {}".format(nome[0]))
print("Seu ultimo nome é {}".format(nome[len(nome)-1]))"""
