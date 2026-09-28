import os

os.system('cls')

frutas = ['banana', 'maçã', 'pera']


# i  -> é utilizado para dizer a posiçao do item da lista
for i, fruta in enumerate(frutas, start=1):
    print(f'{i} - {fruta}')

chose = str(input("Escolha uma fruta: "))

chose.lower

print(f"voce escolheu a fruta {chose}")