# nos divisores tem q entrar o 1 e o próprio número
numero = int(input('Insira um numero para ver seus divisores: '))
divisores = []
for i in range(1, (numero + 1)):
    if numero % i == 0:
        divisores.append(i)


print(f"divisores: {divisores}")
