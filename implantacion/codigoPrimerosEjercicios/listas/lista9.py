temps_max = [30,31,28,26,25]
temps_min = [15,10,14,12,10]

dias_semana = ["lunes", "martes", "miercoles", "jueves", "viernes"]

# for i in range(5):
#     temp_max.append(input("dime una temperatura maxima: 

temp_min = min(temps_min)

for i in range(len(temps_max)):
    temp_media = (temps_max[i] + temps_min[i]) / 2
    print(f"dia {dias_semana[i]} media {temp_media}")

for i in range(len(temps_max)):
    if (temp_min == temps_min[i]):
        print(f"dia {dias_semana[i]} dia mas frio")

temperatura = int(input("dime una temperatura: "))

temperatura_encontrada = False
for i in range(len(temps_max)):
    if (temperatura == temps_max[i]):
        print(f"{dias_semana[i]} este dia hizo esa temperatura")
        temperatura_encontrada = True

if (not temperatura_encontrada):
    print("no se encontro la temperatura")