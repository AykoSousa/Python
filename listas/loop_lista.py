thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

#comando for de forma reduzida    
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#percorrer os itens da lista consultando seu número de índice
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

