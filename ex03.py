while True:
    numero = int(input('Insira um valor de 1 a 10 e veja sua tabuada: '))

    if numero > 10:
        print('valor inválido')
    elif numero < 1:
        print('valor inválido')
    else:
        for i in range(1,11):
            print(f"{numero} x {i} = {numero * i}")
        break
