print("Bem-Vindo ao nosso calculador de medidas")
l = float(input("Digite a largura da parede: "))
a = float(input("Digite a altura da parede: "))
area = a*l
tinta = area/2
print("Com uma parede de {:.2f}m de Largura\nE {:.2f}m de Altura\nA Área total seria de {:.2f}m2\nMas a quantidade necessária de tinta será de {:.2f} Litros".format(l,a,area,tinta))
