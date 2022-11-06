frutas = ["banana", "maçã", "laranja", "pera", "pessego", "kiwi"]
newList = []
for i in frutas:
    if "a" in i:
        newList.append(i)
print(newList)

#Fazendo de forma resumida
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#sintaxe newlist = [expression for item in iterable if condition == True]

# A condição é como um filtro que aceita apenas os itens que avaliam como True.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

#Retornar em maiusculo
newlist = [x.upper() for x in fruits]

newlist = ['hello' for x in fruits]
print(newlist)