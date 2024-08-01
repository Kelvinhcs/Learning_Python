#Crie um programa que defina a classe "Círculo" com um construtor que recebe um parâmetro, o raio do círculo.
#O programa deve criar duas instâncias da classe "Círculo", "c1" e "c2", com diferentes valores para o parâmetro raio.
#Em seguida, o programa deve imprimir o raio e a área de cada um dos círculos criados.

class Círculo:
    def __init__(self, raio) -> None:
        self.raio = raio
        self.area = 3.14*(self.raio*self.raio)
        
        
c1 = Círculo(5)
c2 = Círculo(2.5)

print(f"O Círculo com raio de {c1.raio} tem {c1.area}")
print(f"O Círculo com raio de {c2.raio} tem {c2.area}")
        
