#ingresar 4 numeros y que me de el mayor, menor y el medio



numeros = []

for i in range(4):
    numero = int(input("Introduce el número {}: ".format(i + 1)))
    numeros.append(numero)

numeros.sort()
numero_menor = min(numeros[0], numeros[3])
numero_mayor = max(numeros[0], numeros[3])

print("Los dos números del medio son:", numeros[1], "y", numeros[2])
print("El número menor es:", numero_menor)
print("El número mayor es:", numero_mayor)
