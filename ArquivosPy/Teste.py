import timeit

nome = "Alice"
idade = 30

# Usando %s
def usando_percent():
    return "Nome: %s, Idade: %d" % (nome, idade)

# Usando f-string
def usando_fstring():
    return f"Nome: {nome}, Idade: {idade}"

# Medindo o desempenho
percent_time = timeit.timeit(usando_percent, number=1000000)
fstring_time = timeit.timeit(usando_fstring, number=1000000)

print(f"Tempo usando %s: {percent_time}")
print(f"Tempo usando f-string: {fstring_time}")
