pago_total = 0
pago_mensual = 10

for i in range(0,20):
    print(f"Mes {i+1}: {pago_mensual}")
    pago_mensual *= 2
    pago_total += pago_mensual

print(f"Has pagado {pago_total} euros en 20 meses")

