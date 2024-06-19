salario = float(input("Digite seu salário atual: "))
if salario > 1250:
    aumento = (salario*10)/100
    print('Com base no aumento de 10% para quem recebe mais de R$1250.00\nO aumento do seu salário foi de R${:.2f} resultando num total de R${:.2f}'.format(aumento, salario+aumento))
else:
    aumento = (salario*15)/100
    print('Com base no aumento de 15% para quem recebe menos de R$1250.00\nO aumento do seu salário foi de R${:.2f} resultando num total de R${:.2f}'.format(aumento, salario+aumento))
