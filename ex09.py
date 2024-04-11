import random
numeros = []

for i in range(0,10):
    numero = random.randint(0,100)
    numeros.append(numero)
    numeros.sort()

print(numeros)