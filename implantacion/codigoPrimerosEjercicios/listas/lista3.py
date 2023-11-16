notas = []

print(len(notas))
for i in range(5):
    nota = float(input("dime una nota: "))
    notas.append(nota)

print(notas)

notas.sort(reverse=True)

media = 0
for i in range(len(notas)):
    media += notas[i]

media /= len(notas)

print(notas)
print(media)
print(max(notas))
print(min(notas))
print(notas[0])
print(notas[-1])