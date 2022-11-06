# Variavel Global
num1=num2=res=0
canal = "CFB Cursos"
def cn ():
    print(canal)
cn()

# Variavel sendo definida global quando está dentro de uma função
num1=num2=res=0

def cn ():
    global canal
    canal = "CFB Cursos"
    
cn()

print(canal)