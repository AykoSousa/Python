print("Hello")

a = "Olá"

#String de várias linhas
b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.""" #ou três aspas simples '''

#Strings são Arrays
a = "Hello World"
print(a[1])

#Loop
for letra in "banana":
    print(letra)

#Tamanho de uma string
b = "Hello World"
print(len(a))

#String de verificação
txt = "The best things in life are free!"
print("free" in txt)

#Colocando uma condição
txt = "The best things in life are free!"
if "free" in txt:
    print("Sim, 'free' está presente")

#not in
txt = txt = "The best things in life are free!"
print("expensive" not in txt)

#Condição
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("Não, 'expensive' não está no texto!")

