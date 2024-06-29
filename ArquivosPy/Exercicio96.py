def area(base,altura):
    areadoterreno = base*altura
    print(f'Com base em {base}(m) de largura e {altura}(m) de comprimento')
    print(f'A área do terreno é de {areadoterreno}m².')


print(f'   Controle de Terrenos')
print(f'--------------------------')
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
print(f'--------------------------')
area(largura,comprimento)
