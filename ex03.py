import os

os.system("cls")

numb = int(input('Digite um numero para ver sua tabuada: '))

tab = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in tab:
    multi = numb * number 
    print(f"{numb} X {number} = {multi}")



