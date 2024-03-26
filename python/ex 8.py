#triângulo
v1 = int(input("insira um valor"))
v2 = int(input("insira um valor"))
v3 = int(input("insira um valor"))
if v1 == v2 and v1 == v3:
    print('triângulo é equilátero')
else:
    if v1 == v2 or v1 == v3 or v2 == v3:
        print('triângulo é isoceles')
    else:
        print('triãngulo é escaleno')

