carros = ["HRV", "Polo", "Jetta", "Cruze", "Fusion"]

itCarros = iter(carros)
#print(next(itCarros)) Não esquecer de usar o next().

#Forma rápida de percorrer uma lista, mas gera um por um.

while itCarros: #Aqui não precisamos se preocupar com o controle e nem com o tamanho da lista
    try:
        print(next(itCarros))
    except StopIteration:
        print("Fim da lista!")
        break

#for carro in carros:
#    print(carro)