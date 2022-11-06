carros = ["HRV", "Golf", "Focus", "Jetta"] #Array / List

for x in carros:
    print(x)


m_carros = [
    ["Modelo", "HRV"], 
    ["Fabricante", "Honda"], 
    ["Ano", 2016]
]
print(m_carros[0][0])#Imprimirá "modelo", linha 0 coluna 0

m_carros.append(["Cor", "Prata"])
for line, column in m_carros:
    print(line + " | " + str(column))
    
#Tomar cuidado com a converção de str em int, pois eles não se concatenam