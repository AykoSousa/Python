#Existem três tipos numéricos em Python:
#int,float,complex.
x = 1 #int
y = 1.7 #float
z = 2j #complex
# Float também pode ser números científicos com um "e" para indicar a potência de 10.
a = 35e3
b = 12E4
c = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#Os números complexos são escritos com um "j" como a parte imaginária.

# Conversão de tipo
d = 1
e = 2.9
f = 2j

#int => float
g = float(d)

# float => int
h = int(e)

#int => complex
i = complex(f)

#Python tem um módulo embutido chamado randomque pode ser usado para fazer números aleatórios:
import random
print(random.randrange(1,10))