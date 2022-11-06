#Tratamento de erros
try:
    print(x)

except:
    print("Erro no programa")

else: #Else contrário do except
    print("Tudo certo")

finally: #Execução final
    print("Fim do tratamento")
    
################################
num = -10
if num < 1:
    raise Exception("Valor nao permitido.") #Excecão

num = "Ayko"
if not type(num) is int:
    raise Exception("Somente numeros sao permitidos")
else:
    print(str(num))