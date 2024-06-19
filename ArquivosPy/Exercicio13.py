print("Bem-Vindo ao programa de reajuste salarial")
s = float(input("Digite o valor do seu salário atual: "))
r = s*15/100
a = s+r
print("Seu salário anterior era de R${:.2f}\nMas tivemos um reajuste de 15%, que significa R${:.2f}\nAgora seu salário será de R${:.2f}.".format(s,r,a))
