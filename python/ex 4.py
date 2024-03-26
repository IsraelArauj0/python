
letra = input('insira uma letra: ').lower()
if letra == 'a' or letra == 'e' or letra == 'o' or letra == 'u':
    print("vogal")
else:
    print('consoante')
vogais ="aeiou"
if letra in vogais:
    print('vogal')
else:
    print('consoante')
