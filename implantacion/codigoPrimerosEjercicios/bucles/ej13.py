horas_totales = 0
cobra_por_hora = int(input("¿Cuánto cobras por hora? "))

for i in range(0, 6):
    horas = int(input("¿Cuántas horas has trabajado? "))
    horas_totales += horas


print(f"Has trabajado {horas_totales} horas y has cobrado {horas_totales * cobra_por_hora} euros")