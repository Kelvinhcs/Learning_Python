valor = float(input("Digite o valor do preço do imóvel: "))
salario = float(input("Digite o valor do seu salário atual: "))
anos = int(input("Digite a quantidade de anos que será financiado: "))
print('-=-'*27)
print(f"Um Financiamento de {anos} anos resultaria em {anos*12} parcelas mensais")
if valor / (anos*12) >= (salario*30)/100:
    print("Visto que a prestação mensal do seu financiamento é R${:.2f}\nE 30% do seu salário é R${:.2f}\nVocê foi NEGADO para o nosso empréstimo".format(valor / (anos*12), (salario*30)/100))
else:
    print("Visto que a prestação mensal do seu financiamento é R${:.2f}\nE 30% do seu salário é R${:.2f}\nVocê foi APROVADO para o nosso empréstimo".format(valor / (anos*12), (salario*30)/100))
