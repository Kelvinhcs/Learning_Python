from utilidadescev.moeda import numeros
from utilidadescev.dado import validacao
real = validacao.LeiaDinheiro('Digite o preço: R$')
numeros.resumo(real, 50, 10)