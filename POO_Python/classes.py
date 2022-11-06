#Classe = conjunto de regras de um objeto
#Objeto = instancia da classe

#Criação da classe
class Carro:
    velMax = 0
    ligado = False
    cor = ""

#Criando Instancias Objetos
c1 = Carro()
c2 = Carro()
c3 = Carro()

#Declarando Instancias
c1.velMax = 200
c1.cor = "Preto"
c1.ligado = False

print("Velocidade Máxima: " + str(c1.velMax))
print("Cor: " + c1.cor)
print("Ligado: " + str(c1.ligado))