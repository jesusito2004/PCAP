

precios_frutas = {
    "Plátano": 1.35,
    "Manzana": 0.80,
    "Pera": 0.85,
    "Naranja": 0.70
}

frutas = input("Introduce el nombre de la fruta: ").title()
kg =  float(input("Introduce el kilo de la fruta: "))

if frutas in precios_frutas:
    print(kg, 'kilos de', frutas, 'valen', precios_frutas[frutas]*kg, 'este es el precio')
else:
    print("no se encuentra la fruta")
    
        