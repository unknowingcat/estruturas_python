import os


has_invitation = is_vip = False

invited = age = vip = str()

# Limpa a tela do terminal CMD
os.system("cls")

age = int(input('Digite a idade: '))
vip = input("Voce é VIP? ")



# Define o valor da variável

while vip.lower() != 'sim' or 'nao':
    vip.lower() = input("Resposta nao aceita, digite novamente: ")

    

if vip.lower() == 'sim':
    is_vip = True
    print("Seja muito bem vindo, voce pode entrar!")

else:
    invited = input('Tem convite? ')


if invited.lower() == 'sim' and age >= 18:
    # Neste caso, altera o valor da variável
    has_invitation = True
    print("Voce pode entrar!")

else:
    print("Voce nao pode entrar!")




