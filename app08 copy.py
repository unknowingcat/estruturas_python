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

    match x:
        case '0':
            print("\nAcabou")
            break
        
        case '1':
            print('\nVai comer')
            input('Tecle [Enter] para coninuar.')
        
        case '2':
            print('\nBeba água')
            input('Tecle [Enter] para continuar.')

        case '3':
            print('\nVa dormir')
            input('Tecle [Enter] para continuar')

        case _:
            print('\nNâo entendi!')
            input('Digite [Enter] para continuar')



   