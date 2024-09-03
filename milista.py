# Ejemplo de uso de listas
Misnovias=["Agripina", "Anastacia", "Maria"]
Misnumeros=[666, 77, 10]
# Mostramos mis novias
print(Misnovias)
# Mostramos mis numeros raros
print(Misnumeros)

print("-----Accediendo a los elementos de la lista-----")
print(Misnovias[-2])

if "Ana" in Misnovias:
    print("Si, 'Anastacia' esta en la lista de mis novias")
else:
    print("Chale no eres mi novia")
print("Numero de novias")
Nnovias=len(Misnovias)
print(f"Numero de novias = {Nnovias}")

print("Ciclo for en listas")
posicion=0
for medianaranja in Misnovias:
    print(posicion,"",medianaranja)
    posicion=posicion+1