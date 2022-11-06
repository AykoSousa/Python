#Odernar lista ordem crescente
lista = ["banana", "maçã", "kiwi", "pessego", "melão"]
lista.sort()
print(lista)

num = [100, 40, 1000, 25, 1, 4, 14, 99]
num.sort()
print(num)

#Ordenar lista ordem decrescente
mylist = ["Arroz", "Feijão", "Carne", "Batata", "Alface"]
mylist.sort(reverse=True)
print(mylist)

#Personalizando função
def myFunc(n):
    return abs(n - 50) #Valor absoluto de um número
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myFunc)
print(thislist)

list = ["banana", "Kiwi", "pessego", "Melancia"]
list.sort()
print(list)

#Ordenando sem distinguir maiusculas e minusculas
list = ["banana", "Kiwi", "pessego", "Melancia"]
list.sort(key = str.lower)
print(list)

list = ["banana", "Kiwi", "pessego", "Melancia"]
list.reverse()
print(list)