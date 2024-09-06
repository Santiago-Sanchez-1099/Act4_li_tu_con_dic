# Tuplas
arcoiris=("Azul", "Verde", "Rojo", "Amarillo")
print(arcoiris)
print("-Longitud Arcoiris-")
print(len(arcoiris))

animales=("Pantera", 20, "Estatura", 1.7)
print(animales)

print("Elemento de la tupla")
print(animales[1])

rateros = ("Juan", "Ana", "Pedro")
y = list(rateros)
y[1] = "Polainas"
rateros = tuple(y)
print(rateros)

print("Agregando elementos")
Nanimal=("Boby", "Chetos")
y = list(Nanimal)
print(y)
y.append("Tontolin")
otratupla = tuple(y)
print(otratupla)


print("Uso de for en tuplas")
for elcolor in arcoiris:
    print(elcolor)