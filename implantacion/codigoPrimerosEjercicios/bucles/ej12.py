

i = 0
ahorrado = 0

while i < 12:
    ahorrado_mes = int(input("¿Cuánto dinero has ahorrado este mes? "))) 

    ahorrado += ahorrado_mes
    print(f"Has ahorrado {ahorrado} euros hasta mes {i+1}")
    i+=1

print(f"Has ahorrado {ahorrado} euros en un año")