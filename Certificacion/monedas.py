

monedas = {'Euro':'€', 'Dollar':'$', 'arroba':'@'}

divisa = input('Que divisa prefiere: ')
if divisa.title() in monedas:
    print(monedas[divisa.title()])
else:
    print('No tenemos esa divisa')