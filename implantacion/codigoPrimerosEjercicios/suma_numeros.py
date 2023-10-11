final = int(input("dime un numero"))

i = 1
suma_pares = 0
suma_impares = 0

while i <= final:

    if (i%2) == 0:
        suma_pares += i
    else:
        suma_impares += i
    i += 1

while i<= 100:
    print("No se pinta en las paredes")
    i+=1
str = input("dime una palabra")
cantida_palabras = 0

while str != "salir":
    print("No se pinta en las paredes")
    str = input("dime una palabra")
    cantida_palabras += 1



print(f"La suma de los numeros pares es {suma_pares} " +
      f" y los impares{suma_impares}")

