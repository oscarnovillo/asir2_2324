n  =1
while n<=10:
    numero_mayor = int(n**0.5)
    i=2

    while i<=numero_mayor:
        if (n%i==0):
            print("no es primo")
            break
        i+=1
    else:
        print(f"es primo {n}")
    n+=1


es_primo = True
while (numero_mayor > 1 and es_primo):
    if (n%numero_mayor==0):
        es_primo = False
    numero_mayor -= 1

if (es_primo):
    print("es primo")

