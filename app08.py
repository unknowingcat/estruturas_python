import os

os.system("cls")


while True:
    os.system('cls')
    print( '''
            1) Estou com fome
            2) Estou com sede
            3) Estou com sono
          
          0) Sair
    ''')

    x = input("Escolha uma opção: ")

    if x == '1':
        print("\nVai comer")
        input('Tecle [Enter] para continuar')

    elif x == '2':
        print('\nBeba água')
        input("Tecle [Enter] para continuar.")
    
    elif x == '3':
        print("\nVa dormir.")
        input('Tecle [Enter] para continuar.')

    elif x == '0':
        print("\nAcabou")
        break

    else:
        print("\nNao entendi!!")
        input("Tecle [Enter] para continuar.")
