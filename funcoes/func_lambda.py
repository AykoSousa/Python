#Lambda - Funçoes Anonimas
soma = lambda a,b: a + b
r = soma(5,6)
print(r)

mult = lambda a,b,c: (a+b)*c
print(mult(4, 9, 6))

#Ou
print((lambda a,b: a+b)(5,9))

r = lambda x,func:x+func(x)#Corresponde ao x + o resultado da função
res = r(2, lambda x: x*x)
print(res)