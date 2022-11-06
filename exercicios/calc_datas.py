import datetime

print("A data a ser inserida deve ser no seguinte formato -> M/D/YY")

print('*'*40)

data = str(input("Digite a data em que deseja calcular: "))
curr_date = data #Armazenando a data inserida

curr_date_temp = datetime.datetime.strptime(curr_date, "%m/%d/%y")

dias = int(input("Digite quantos dias de contrato: "))
dia = datetime.timedelta(days = dias)

new_date = curr_date_temp + dia

print("O prazo contratual terminara dia: " + str(new_date))