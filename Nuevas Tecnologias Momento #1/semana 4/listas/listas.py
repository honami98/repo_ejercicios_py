
nombre = ["Luis", "Lolo", "Luli", "Maria", "Pepo"]
edad = [25, 19, 21, 33, 40]
estatura = [1.80, 1.65, 1.74, 1.66, 1.54]
casado = [False, False, False, True, True]
usuario = ["Luis", 25, 1.80, False]

print(len(edad))

print(type(nombre))
print(type(edad))
print(type(estatura))
print(type(casado))
print(type(usuario))


print(usuario[0:3])
print(nombre[1:3])
print(nombre[:3])
print(nombre[1:])
print(nombre[:-1])
print(nombre[:4])
print(nombre[-4:-1])
print(nombre[1:4])

if "Luis" in nombre:
    print("el nombre esta en la lista")
else:
    print("No se encontró el nombre buscado")

usuario[0] = "Luis"

nombre[0:3] = "Manuel", "Jorge", "Andrea"
print(nombre[0:5])

nombre.insert(0, "Luis")
print(nombre[0:])

nombre.append("Laura")
print(nombre[0:])

nombre2 = ["Ricardo", "Erre"]
nombre.extend(nombre2)
print(nombre)


nombre.remove("Erre")
print(nombre[0:])

nombre.pop(4)
print(nombre[0:])


del nombre[1]
print(nombre[0:])


nombre.clear()

del nombre

for i in edad:
    print(i)

for i in range(len(estatura)):
    print(estatura[i])


print("-------------------")

[print(x) for x in edad]

print("-------------------")

i = 0

while i < len(usuario):
    print(usuario[i])
    i += 1


print("-------------------")

for i, edad in enumerate(edad):
    print(i, edad)

print("-------------------")
