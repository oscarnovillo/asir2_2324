
numero_introducido = int(input("Dime un numero"))
suma = 0
cantidad_numeros =0

while numero_introducido != 0:
    suma += numero_introducido
    cantidad_numeros += 1
    numero_introducido = int(input("Dime un numero"))

print(f"gracias {suma} {suma/cantidad_numeros}")


