escolha = int(input("Digite um número para mostrar o seu nome: "))
while escolha < 0 or escolha > 20:
    escolha = int(input('Número inválido. Tente novamente: '))
tup = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
print(f'Você digitou o número {tup[escolha]}.')
