import os

os.system("cls")

numb = int(input('Digite um numero para ver sua tabuada: '))

tab = list(range(0, 11))

for number in tab:
    multi = numb * number 
    print(f"{numb} X {number} = {multi}")



