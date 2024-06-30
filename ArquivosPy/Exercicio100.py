from random import randint
numeros = []
def sorteia():
    for cont in range(0, 5):
        numeros.append(randint(1,10))
    print(numeros)
def SomaPar(num):
    somavalorespares = 0
    for valorunico in num:
        if valorunico % 2 == 0:
            somavalorespares += valorunico
    print(somavalorespares)

sorteia()            
SomaPar(numeros)
