import  random
import os

erros = 0
sorteado = random.randrange(0,100)#Aqui escolhemos dentro da biblioteca random um número aleatório de 0 a 100
print("Seja bem vindo(a) ao meu game de adivinhação!")

nome = str(input("Digite seu nome "))
print("Vamos começar, " + nome + "!")

jogador = int(input("Digite um número: "))

while (sorteado != jogador):
    os.system("cls") #Limpar a tela
    if sorteado > jogador:
        print("ERRO!, o número é maior")
    elif(sorteado < jogador):
        print("ERRO!, o número é menor")
    erros += 1 #Implementando mais 1 a varável erro que iniciou em zero
    jogador = int(input("Digite um número: "))

print("Número: " + str(jogador) + ", você acertou em " + str(erros+1) + "tentativas!")