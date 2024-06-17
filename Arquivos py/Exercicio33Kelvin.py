n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
#teste maior
if n1 > n2 and n1 > n3:
    print(f"O maior número é {n1} da primeira posição")
if n2 > n1 and n2 > n3:
    print(f"O maior número é {n2} da segunda posição")
if n3 > n1 and n3 > n2:
    print(f"O maior número é {n3} da terceira posição")
#teste menor
if n1 < n2 and n1 < n3:
    print(f"O menor número é {n1} da primeira posição")
if n2 < n1 and n2 < n3:
    print(f"O menor número é {n2} da segunda posição")
if n3 < n1 and n3 < n2:
    print(f"O menor número é {n3} da terceira posição")