linha1 = [[], [], []]
linha2 = [[], [], []]
linha3 = [[], [], []]
print('-=-'*22)
for c in range(0, 3):
    linha1[c].append(int(input(f'Digite o {c+1}º valor da primeira linha: ')))
for c in range(0, 3):
    linha2[c].append(int(input(f'Digite o {c+1}º valor da segunda linha: ')))
for c in range(0, 3):
    linha3[c].append(int(input(f'Digite o {c+1}º valor da terceira linha: ')))
print('-=-'*22)
for item in linha1:
    print(item, end='')
print()
for item in linha2:
    print(item, end='')
print()
for item in linha3:
    print(item, end='')
print()
print('-=-'*22)

