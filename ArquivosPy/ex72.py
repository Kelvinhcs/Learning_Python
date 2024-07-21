while True:
    escolha = int(input('Digite um número entre 0 e 20: '))
    if escolha <= 0 or escolha <=20:
        break
    print('Tente novamente')
tup = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
print(f'Você digitou o número {tup[escolha]}.')
