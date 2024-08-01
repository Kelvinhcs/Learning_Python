#Crie um programa que defina a classe "Carro" com um construtor que receba dois parâmetros, a cor e a marca do carro.
#O programa deve criar duas instâncias da classe "Carro", "c1" e "c2", com diferentes valores para os parâmetros cor e marca.
#Em seguida, o programa deve imprimir a cor e a marca de cada um dos carros criados.
from random import choice
marcas = ['Fiat', 'Renault', 'Pegeout', 'Lamborguini', 'Ferrari', 'McLaren', 'BYD', 'Tesla', 'Toyota']
cores = ['Vermelho', 'Verde', 'Azul', 'Amarelo', 'Roxo', 'Branco', 'Preto', 'Rosa']
class Carro:
    def __init__(self, cor, marca) -> None:
        self.cor = cor
        self.marca = marca
        

c1 = Carro(cor=choice(cores), marca=choice(marcas))
c2 = Carro(cor=choice(cores), marca=choice(marcas))
print(f'O carro 1 da marca {c1.marca} é da cor {c1.cor}.')
print(f'O carro 2 da marca {c2.marca} é da cor {c2.cor}.')
