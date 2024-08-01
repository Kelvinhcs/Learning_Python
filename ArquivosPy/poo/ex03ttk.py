# Crie um programa que defina a classe "Aluno" com um construtor que recebe três parâmetros, o nome, a idade e a nota do aluno.
# O programa deve criar duas instâncias da classe "Aluno", "a1" e "a2", com diferentes valores para os parâmetros nome, idade e nota.
# Em seguida, o programa deve imprimir o nome, a idade e a nota de cada um dos alunos criados.
# E por último, calcular e imprimir a média das notas dos dois alunos criados.

class Aluno:
    def __init__(self, nome, idade, nota) -> None:
        self.nome = nome
        self.idade = idade
        self.nota = nota
        
        
        
        
a1 = Aluno('João', 20, 5.5)
a2 = Aluno('Kleber', 15, 10)

print(f"O aluno {a1.nome} que tem {a1.idade} teve nota {float(a1.nota):.2f}")
print(f"O aluno {a2.nome} que tem {a2.idade} teve nota {float(a2.nota):.2f}")
print(f'A média das notas de {a1.nome} e {a2.nome} é {(a1.nota + a2.nota)/2}')