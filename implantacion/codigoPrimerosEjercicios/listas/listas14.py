import random

baraja = []
palos = ["espadas", "bastos", "oros", "copas"]

for i in range (4):
    for j in range(10):
        carta = []
        carta.append(j+1)
        carta.append(palos[i])
        baraja.append(carta)

print(baraja)
random.shuffle(baraja)

print(baraja)
for i in range(len(baraja)):
    print(baraja[i])