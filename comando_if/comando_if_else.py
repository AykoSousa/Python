a = 10
b = 5
res = 0
op = "-"

if op == "+":
    res = a + b
elif op == "-": #elif é o mesmo que senão se.
    res = a - b
elif op == "*":
    res = a * b
else:
    print("Fim do programa!")
    
    
    
tempo = "Ensolarado"
dinheiro = 500
lugar = ""

if tempo == "Ensolarado" and dinheiro >= 500:
    lugar = "Praia"
else:
    lugar = "Cama"
print("Vou para a " + str(lugar))