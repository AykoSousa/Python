class Carro:
    velMax = 0
    ligado = False
    cor = ""
    def __init__(self, v, l, c): #contrutor já declara instancias
        self.velMax = v
        self.ligado = l
        self.cor = c
    
    def mostrar(self):
        print("Velocidade Máxima: " + str(self.velMax))
        print("Cor.............: " + self.cor)
        print("Ligado...........: " + str(self.ligado))
        print("------------------------------")
    def ligar(self):
        self.ligado = True
    def desligar(self):
        self.ligado = False
    def andar(self):
        if (self.ligado):
            print("Andando")
        else:
            print("Carro desligado")

#Criando Instancias Objetos
c1 = Carro(200, False, "Preto")
c2 = Carro(500, False, "Verde")
c3 = Carro(150, False, "Azul")

#Chamando
c1.ligar()

c1.mostrar()
c2.mostrar()
c3.mostrar()

c1.andar()
c2.andar()