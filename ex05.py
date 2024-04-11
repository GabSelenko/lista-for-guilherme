import random
numerosImpares = []
numerosPares = []

for i in range(0,10):
    numero = random.randint(0,100)
    if numero % 2 == 0:
        numerosPares.append(numero)
    else:
        numerosImpares.append(numero)

print(f"Quantidade de numeros pares: {len(numerosPares)} ({numerosPares})")
print(f"Quantidade de numeros ímpares: {len(numerosImpares)} ({numerosImpares})")