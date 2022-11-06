print("Tabuada")
print('*' * 20)

base = int(input("Entre com um numero para consultar a tabuada: "))
valor = 0

print('*' * 20)

while valor <= 10:
    print("{} x {} = {}".format(base, valor, (base*valor)))
    valor += 1