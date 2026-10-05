

numb = int(input('Digite um numero para ver sua soma: '))

numeros = list(range(1, 101))

for i in numeros:
    soma = numb + i
    print (f'• {numb} + {i} = {soma}')

