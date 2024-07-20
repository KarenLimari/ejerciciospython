import math



#variables a utilizar
proteina = float(input("Ingrese los gr de proteina:\n>"))
carbohidratos = float(input("Ingrese los gr de carbohidratos:\n>"))
grasa = float(input("Ingrese los gr de grasa:\n>"))

calorias = 4 * (proteina + carbohidratos) + 9 * grasa
calorias = math.ceil(calorias) #operacion separada del print

print(calorias)
print (f"Las calorias totales del producto son: {calorias}")