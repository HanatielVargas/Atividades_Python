while True:
    try:
        num = input('Digite um número: ')
    except:
        print('\033[1;31mOcorreu um erro!\033[m')
    else:
        print(f'''Analisando o número {num}
Unidade: {num[0] if len(num) > 0 else 0}
Dezena: {num[1] if len(num) > 1 else 0}
Centenas: {num[2] if len(num) > 2 else 0}
Milhar: {num[3] if len(num) > 3 else 0}
''')
        break
