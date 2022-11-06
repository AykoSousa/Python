lista1 = ["maçã", "banana", "laranja"]
lista2 = [1, 2, 3]
lista3 = lista1 + lista2
print(lista3)

# anexando todos os itens da lista2 na lista1
for x in lista2:
    lista1.append(x)

print(lista1)

#metodo extend()
lista1 = ["maçã", "banana", "laranja"]
lista2 = [1, 2, 3]
lista1.extend(lista2)
print(lista1)