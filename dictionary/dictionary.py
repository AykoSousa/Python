carro = {"Fabricante":"Honda",
         "Modelo":"HRV",
         "Ano":"2016",
         "Cor":"Prata"
} #Dicionario trabalha com chave e valor
print(carro)
print(carro["Modelo"]) #Imprimir o valor da chave

#Ou podemos fazer cpm método get
fab = carro.get("Fabricante")
print(fab)

#Mudar valores
carro["Cor"] = "Preto"

#Loop
for i in carro:
    print(i) #Chave
    print(carro[i]) #Valores

#Ou
for c,v in carro.items(): #Usar items para imprimira chave e valor
    print(c + ": " + v)
    
#Verificar se exite valor
if "Modelo" in carro:
    print("Sim, modelo é uma chave!")

#Tamanho
print(str(len(carro)))#Converter para str, pois o LEN é int por padrão

#Adicionar
carro["Cambio"] = "Automatico"

#Remover
carro.pop("Cambio")

#Dicionario dentro de dicionario
carros = {
    "Carro1": {
        "Fabricante":"Honda",
        "Modelo":"HRV"
    },
    "Carro2": {
        "Fabricante": "Volkswagem",
        "Modelo": "Jetta"
    },
    "Carro3": {
        "Fabricante": "Ford",
        "Modelo": "Focus"
    }
}
print(carros["Carro1"])
print(carros["Carro2"]["Fabricante"])

# Adicionar dicionarios em um dicionario
Carro1 ={
    "Fabricante":"Honda",
    "Modelo":"HRV"
}

Carro2 ={
    "Fabricante": "Volkswagem",
    "Modelo": "Jetta"
}

Carro3 ={
    "Fabricante": "Ford",
    "Modelo": "Focus"
}

Carros = {
    "C1":Carro1,
    "C2":Carro2,
    "C3":Carro3
}
print(Carros["C1"])
print(Carros["C2"]["Modelo"])