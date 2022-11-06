import os

carros = []

# Criação da classe carro e seus métodos
class Carro:
    nome = ""
    potencia = 0
    velMax = 0
    ligado = False
    # Definindo o contrutor da classe carro
    def __init__(self, nome, potencia):
        self.nome = nome
        self.potencia = potencia
        self.velMax = int(potencia)*2
        self.ligado = False
        
    def ligar(self):
        self.ligado = True
        
    def desligar(self):
        self.ligado = False
        
    def info(self):
        print("Nome...:" + self.nome)
        print("Potencia...:" + str (self.potencia))
        print("Velocidade Maxima...:" + str (self.velMax))
        print("Estado...:" + ("Ligado" if self.ligado == True else "Desligado")) # Operador ternário

# Criando um menu
def Menu():
    os.system("cls") or None
    print("1 - Novo Carro")
    print("2 - Informacoes do Carro")
    print("3 - Excluir Carro")
    print("4 - Ligar Carro")
    print("5 - Desligar Carro")
    print("6 - Listar Carros")
    print("7 - Sair")
    print("Quantidade de carros: " + str(len(carros)))
    opc = input("Digite uma opcao: ")
    return opc

# Craição das funções do menu
def NovoCarro():
    os.system("cls") or None
    n = input("Nome do carro: ")
    p = input("Potencia do carro: ")
    car = Carro(n, p)
    carros.append(car)
    print("Novo carro criado!")
    os.system("pause")

def Informacoes():
    os.system("cls") or None
    n = input("Informe o numero do carro que deseja ver as informacoes: ")
    try:
        carros[int(n)].info()
    except:
        print("Carro nao existe na lista")
    os.system("pause")

def excluirCarro():
    os.system("cls") or None
    n = input("Informe o numero do carro que deseja excluir: ")
    try:
        del carros[int(n)]
        print("Carro excluido!")
    except:
        print("Carro nao existe na lista")
    os.system("pause")

def ligarCarro():
    os.system("cls") or None
    n = input("Informe o numero do carro que deseja ligar: ")
    try:
        carros[int(n)].ligar()
        print("Carro ligado!")
    except:
        print("Carro nao existe na lista")
    os.system("pause")
    
def desligarCarro():
    os.system("cls") or None
    n = input("Informe o numero do carro que deseja desligar: ")
    try:
        carros[int(n)].desligar()
        print("Carro desligado!")
    except:
        print("Carro nao existe na lista")
    os.system("pause")
    
def listarCarros():
    os.system("cls") or None
    p = 0
    for c in carros:
        print(str(p + " - " + c.nome))
        p = p+1
    os.system("pause")
    
ret = Menu()
while ret < "7":
    if ret == "1":
        NovoCarro()
    elif ret == "2":
        Informacoes()
    elif ret == "3":
        excluirCarro()
    elif ret == "4":
        ligarCarro()
    elif ret == "5":
        desligarCarro()
    elif ret == "6":
        listarCarros()
    ret = Menu()
os.system("cls") or None
print("Programa Finalizado!")