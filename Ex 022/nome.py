nome = input('Digite seu nome completo: ').strip()

print(f'''Analisando seu nome...
Seu nome em maiúsculas é {nome.upper()}
Seu nome em minúsculas é {nome.lower()}
Seu nome tem ao todo {len(nome)-(len(nome.split())-1)} letras
Seu primeiro nome é {nome.split()[0]} e ele tem {len(nome.split()[0])} letras''')