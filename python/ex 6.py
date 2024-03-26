#exercicio 6: horas e minutos

hora = int(input("insira o valor das horas"))
min = int(input("insira o valor dos minutos"))
if hora >= 00 or hora <= 23 and min >= 00 or min <= 59:
    print('horário válido')
else:
    print('horário invalido')
    print(hora)
