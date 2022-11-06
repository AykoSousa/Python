#Funcção é um bloco de código que posso executar a qualquer momento quando eu chamo pelo nome
def somar():
    print("Curso de Python")

somar()#Chamando função

#####################################

n1 = 10
n2 = 5
def soma():
    result = n1 + n2
    print("O resultado da soma de {} e {} é igual a {}".format(n1, n2, result))
soma()

######################################

n3 = 20
n4 = 7
def sub():
    r = n3 - n4
    print("O resultado da subtração de {} e {} é igual a {}".format(n3, n4, r))
sub()

########################################

#Chamando funções com uma função
def calculos():
    soma()
    sub()

calculos()