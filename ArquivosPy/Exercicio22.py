n = str(input("Digite o seu nome: ")).strip()
s = n.split()
print("Seu nome é", n)
print("Todo maiúsculo ficaria", n.upper())
print("Todo minusculo ficaria", n.lower())
print("Seu nome possui {} caracteres".format(len(n) - n.count(' ')))
print("Seu primeiro nome é {}".format(s[0]))
print("A Quantidade de caracteres dele é {}".format(len(s[0])))
print("A Quantidade de caracteres dele é {}".format(n.find(' ')))




