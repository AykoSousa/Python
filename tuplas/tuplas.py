carros = ["HRV", "Argo", "Golf"]
t_carros = ("Argo", "HRV", "Golf") #Tuplas são feitas com parenteses

t_carros[2] = "Focus" ##Retorna erro, pois tupla não suporta alterações de valor.

for x in t_carros:
    print(x)
    
l_carros = list(t_carros) #Se fizer a converção podemos modificar os valores da tupla.