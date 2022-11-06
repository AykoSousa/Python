#remove
myList = ["laranja", "maçã", "banana", "pera"]
myList.remove("banana")
print(myList)

#método pop remove uma idice especificado
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#método pop remove por padrão o ultimo item
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#A palavra- delchave também remove o índice especificado
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#del pode excluir toda lista
thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist)

#método clear limpa a lista
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)