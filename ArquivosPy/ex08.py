print("Bem-Vindo ao conversor de medidas")
me = float(input("Digite a metragem: "))
c = me*100
m = me*1000
print("Com base em {:.2f} metros\nVocê possuiria {:.2f} centímetros\nE {:.2f} milímetros".format(me,c,m))
