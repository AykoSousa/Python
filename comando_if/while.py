import os

i = 0
while i <= 10:
    print(i)
    i += 1
print("Fim do loop")

os.system('cls')

lista = ["Laranja", "Banana", "Kiwi", "Manga", "Pera", "Maçã", "Pessego", "Melancia", "Tomate", "Limão"]

for i in lista:
    print(i)
    if i == "Tomate":
        print("Erro")
        break
    i = + 1
    