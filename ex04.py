idades = []
soma = 0
media = 0
for i in range(0,5):
    idade = int(input(f'insira a {i+1}ª idade: '))
    idades.append(idade)
    soma += idade
    media = soma/len(idades)
print(f'A media das idades é de {media}')