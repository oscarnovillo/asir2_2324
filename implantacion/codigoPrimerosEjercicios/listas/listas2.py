palabras = []

for i in range(5):
    palabra = input("dime una palabra: ")
    palabras.append(palabra)


print(palabras[1])
print(palabras[1:3].reverse())
print(palabras[2:])
print(palabras[:3])
print(palabras[4::-1])

indice = int(input("dime un indice: "))

print(palabras[indice])

palabras.reverse()

print(palabras[:].reverse())
print(palabras)

palabras_filtradas = []

for i in range(len(palabras)):
    if "a" in palabras[i]:
        palabras_filtradas.append(palabras[i])

palabras.filter(lambda palabra: "a" in palabra, palabras_filtradas)


