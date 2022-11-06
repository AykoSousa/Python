mylist = ["laranja", "banana", "maçã", "goiaba", "manga"]
mylist.append("carambola") #por padrão irá para ultimo lugar da lista

#anexar elementos de outra lista a atual - extend()
mylist = ["laranja", "banana", "maçã", "goiaba", "manga"]
tropical = ["abacaxi", "morango", "amora"]
mylist.extend(tropical)
print(mylist)


mylist = ["laranja", "banana", "maçã", "goiaba", "manga"]
mylist.insert(1,"limão")
print(mylist)