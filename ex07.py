# 50 primeiros pares
# de 1 a 100 possuimos 50 pares e 50 impares, ou seja, range(1,101)
somaPar = 0
for i in range(1,101):
    if i % 2 == 0:
        somaPar+=i

print(somaPar) # retorno = 2550