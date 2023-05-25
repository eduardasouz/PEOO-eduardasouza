print('digite o valor da prestação:')
valor = float(input())
print('digite a taxa de juros:')
taxa = float(input())
print('digite o tempo de atraso:')
tempo = float(input())

p = valor + (valor*(taxa/100))**tempo
print('o valor a pagar é',p)