minutos_totales = int(input("dime unos minutos"))

horas = minutos_totales//60

minutos = minutos_totales % 60

print (f"{horas:2d}:{minutos:02d}")