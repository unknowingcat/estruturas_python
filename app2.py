print("So é aceito numeros  PARES!!!")

number = int(input("Digite um numero: "))

print(f"Voce digitou o numero {number}")

if (number % 2 == 0):
    print("Esse numero é par!")

else:
    print("Esse numero é impar")

while (number % 2 != 0):
    number = int(input("Errado, escreva novamente: "))

print(f"Agora sim o numero {number} é par")









    
