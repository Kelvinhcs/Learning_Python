print("Bem-Vindo ao nosso Alugador de carros")
km = float(input("Digite a quantidade de kilometros rodados: "))
d = int(input("Digite a quantidade de dias: "))
dp = 60*d
kmp = 0.15*km
t = dp+kmp
print("Os preços atuais são de R$60,00 por dia e R$0,15 por kilometro rodado\nAs informações dadas foram de {} Dias e {:.2f}Km\nPortanto o valor total será de R${:.2f}, com base em R${:.2f} pelos kilometros e R${:.2f} pelos dias".format(d,km,t,kmp,dp))
