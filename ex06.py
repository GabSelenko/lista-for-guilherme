import random
dentroIntervalo = []
foraIntervalo = []

for i in range(0,10):
    numero = random.randint(0,30)
    if numero < 20 and numero > 10:
        dentroIntervalo.append(numero)
    else:
        foraIntervalo.append(numero)

print(f"Quantidade de numeros dentro do intervalo entre [10,20]: {len(dentroIntervalo)} ({dentroIntervalo})")
print(f"Quantidade de numeros fora do intervalo entre [10,20]: {len(foraIntervalo)} ({foraIntervalo})")