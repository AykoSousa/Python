def somar(n1, n2):
    r = n1 + n2
    print("A soma de {} e {} é igual a {}".format(n1, n2, r))
somar(5,9)

def textos(*txt):
    for t in txt:
        print(t)

textos("CFB CURSOS", "Python", "Canal", "Curso", "Computador")

def soma(*num):
    result = 0
    for n in num:
        result += n
    print(result)
soma(5,6,8,10,9)#Agora podemos passar diversos valores de forma arbitrária

valores = [1, 5, 9, 8]
def sub(num):
    resultado = 0
    for n in num:
        resultado -= n
        
    print(resultado)
sub(valores)