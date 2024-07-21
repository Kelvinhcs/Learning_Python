primeiro = int(input('Digite o primeiro termo: '))
passo = int(input('Digite a razão: '))
decimo = primeiro + (10 - 1) * passo
for c in range(primeiro, decimo+1, passo):
    print(c)
