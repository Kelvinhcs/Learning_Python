print("Bem-Vindo ao conversor de temperaturas")
c = float(input("Digite quantos graus deseja converter, em celsius: "))
k = c + 273.15
f = (c*9/5)+32
print("Com base em {:.2f}°C isso equivale a\n{:.2f}°F\n{:.2f}K".format(c,f,k))