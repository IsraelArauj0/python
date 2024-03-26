#salario
sal = int(input("insira o seu salario"))
venda = int(input('insira o valor das vendas'))
if venda <= 1500:
    comissao = venda * 0.03 + sal
    print(comissao)
else:
    comissao = (venda - 1500) * 0.05 + 45 + sal
    print(comissao)
