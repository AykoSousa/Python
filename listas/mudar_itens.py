mylist = ["laranja", "banana", "maçã", "goiaba", "manga"]
mylist [1] = "pera"
print(mylist)

# mudar valores em um range
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(len(thislist))

#inserir itens sem substituir
mylist = ["laranja", "banana", "maçã", "goiaba", "manga"]
mylist.insert(2, "pera") #este método é para inserir um item em um lugar especifico, por isso se passa a posição


lista = ["maçã", "banana", "laranja", "pera", "limão", "batata", "arroz"]
print(lista[2:6])