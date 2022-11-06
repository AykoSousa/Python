import os

casas = []

class Casa:
    cor = ""
    tamanho = 0
    preco = 0
    andar = 0
    status = False
    
    def __init__(self, cor, tamanho, preco, andar, vendido):
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco
        self.andar = andar
        self.status = False
        
    def vendido(self):
        self.status = True
        
    def disponivel(self):
        self.status = False
    
    def info(self):
        print("Cor:... " + self.cor)
        print("Tamanho:... " + str (self.tamanho))
        print("Preco:... " + str (self.preco))
        print("Andar:... " + str (self.andar))
        print("Status:... " + "Vendida" if self.status == True else "Disponivel")
        
def Menu():
    print("1 - Adicionar Casa")
    print("2 - Remover Casa")
    print("3 - Consultar Casa")
    print("4 - Casa Disponivel")
    print("5- Vender Casa")
    print("6 - Sair")
    opcao = input("Digite uma opcao: ")
    return opcao

def AdicionarCasa():
    os.system("cls") or None
    c = input("Digite a cor da casa: ")
    t = input("Digite o tamanho da casa: ")
    p = input("Digite o preco da casa: ")
    a = input("Digite quantos andares há na casa: ")
    s = input("Digite status da casa: ")
    cas = Casa(c, t, p, a, s)
    casas.append(cas)
    print("Casa adicionada!")
    os.system("pause")

def RemoverCasa():
    os.system("cls") or None
    i = input("Digite o numero da casa que deseja excluir: ")
    try:
        del casas [int(i)]
        print("Casa excluida!")
    except:
        print("Casa nao listada!")
    os.system("pause")

def ConsultarCasa():
    os.system("cls")
    i = input("Digite o numero da casa que deseja consultar: ")
    try:
        casas[int(i)].info()
    except:
        print("Casa nao listada!")
    os.system("pause")

def VenderCasa():
    os.system("cls")
    c = input("Digite o numero da casa que deseja vender: ")
    try:
        casas[int(c)].vendido()
        print("Casa Vendida!")
    except:
        print("Casa nao listada!")
    os.system("pause")

def CasaDisponivel():
    os.system("cls")
    c = input("Digite o numero da casa que deseja anunciar: ")
    try:
        casas[int(c)].disponivel()
        print("Casa Disponivel!")
    except:
        print("Casa nao listada!")
    os.system("pause")

ret = Menu()
while ret < "6":
    if ret == "5":
        VenderCasa()
    elif ret == "4":
        CasaDisponivel()
    elif ret == "3":
        ConsultarCasa()
    elif ret == "2":
        RemoverCasa()
    elif ret == "1":
        AdicionarCasa()
    ret = Menu()
os.system("cls") or None
print("Fim do Programa!")