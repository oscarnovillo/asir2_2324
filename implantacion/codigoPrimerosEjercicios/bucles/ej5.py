
caracter = input("Introduce un caracter: ")

while caracter != ' ':
    caracter_case  = caracter.lower()
    if (caracter_case=='a' or caracter_case=='e' 
        or caracter_case=='i' or caracter_case=='o' or caracter_case=='u'):
        print("Es una vocal")
    else:
        print("No es una vocal")
    caracter = input("Introduce un caracter: ")
    

bucle = True
while bucle:
    caracter_case  = caracter.lower()
    if (caracter_case=='a' or caracter_case=='e' 
        or caracter_case=='i' or caracter_case=='o' or caracter_case=='u'):
        print("Es una vocal")
    else:
        print("No es una vocal")
    caracter = input("Introduce un caracter: ")
    if (caracter == ' '):
        bucle = False
