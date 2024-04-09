import math

#calcular la distancia recorrida (m) 
# por un móvil que tiene velocidad constante 100 (m/s) durante un tiempo T 30 (Sg), 
# considerar que es un MRU (Movimiento Rectilíneo Uniforme)


print("Ingrese la velocidad recorrida  ")
v = int(input())
print("Ingrese el tiempo en segundos ")
s = int(input())
dis = v * s
print("la distancia:", dis, "m")



#Se necesita obtener el promedio simple de un 
# estudiante a partir de sus tres notas parciales.
print("Ingrese las tres notas")
not1 = float(input())
not2 = float(input())
not3 = float(input())

total= (not1+not2+not3)/3
print("El promedio es: ", total)
     
#Elaborar un algoritmo que solicite el número de respuestas correctas, 
# incorrectas y en blanco, correspondientes a postulantes, y muestre su puntaje      
#final considerando, que por cada respuesta correcta tendrá 4 puntos, 
# respuestas incorrectas tendrá -1 y respuestas en blanco tendrá 0.


print("Ingrese el número de respuestas correctas:")
correctas = int(input())
print("Ingrese el número de respuestas incorrectas:")
incorrectas = int(input())
print("Ingrese el número de respuestas en blanco:")
en_blanco = int(input())

puntaje = (correctas * 4) + (incorrectas * -1) + (en_blanco * 0)
print("El puntaje final es:", puntaje)


#Elaborar un algoritmo que permita ingresar el 
# número de partidos ganados, perdidos y empatados, 
# por algún equipo en el torneo apertura, se debe de mostrar su puntaje total, 
# teniendo en cuenta que por cada partido ganador obtendrá 3 puntos, 
# empatado 1 punto y perdido 0 puntos.

print("Ingrese el numero de partidos ganados")
pg= int(input())
print("Ingrese el numero de partidos empatados")
pe = int(input())
print("Ingrese el numero de partidos perdidos")
pp = int(input())

ppg = pg * 3
ppe = pe * 1
pt = ppg + ppe
print("El puntaje total es: ", pt)



#Se requiere el algoritmo para elaborar la planilla de un empleado. 
# Para ello se disponSe requiere el algoritmo para elaborar la planilla de un empleado. Para ello se dispone de sus horas laboradas en el mes, así como de la tarifa por hora.e de sus horas laboradas en el mes, 
# así como de la tarifa por hora.

print("Ingrese sus horas laboradas en el mes:")
hlm = int(input())
print("Ingrese la tarifa por hora")
th = float(input())
p = hlm * th
print("el total de la planilla es: ", p)


#Elabore un algoritmo que lea los 3 lados de un triángulo cualquiera y 
# calcule su área, considerar: Si A, B y C son los lados, y S el semi perímetro.

print("Ingrese el lado A")
la = int(input())
print("Ingrese el lado B")
lb = int(input())
print("Ingrese el lado C")
lc = int(input())

ls = (la+lb+lc)/2
at = (ls * (ls - la) * (ls - lb) * (ls - lc)) ** 0.5
print("EL area del triangulo es: ", at)


#Elaborar un algoritmo que permita calcular el número de CDs necesarios 
# para hacer una copia de seguridad, de la información almacenada en un disco cuya capacidad se conoce. 
# Hay que considerar que el disco duro está lleno de información, además expresado en gigabyte. 
# Un CD virgen tiene 700 Megabytes de capacidad y una Gigabyte es igual a 1,024 megabyte.

print("Ingrese la capacidad del disco duro en gigabytes:")
capacidad_disco = int(input())

capacidad_cd = 700  
megabytes_por_gigabyte = 1024

capacidad_disco_megabytes = capacidad_disco * megabytes_por_gigabyte

num_cds = capacidad_disco_megabytes // capacidad_cd

print("El número de CDs necesarios es:", num_cds)


#Se tiene los puntos A y B en el cuadrante positivo del plano cartesiano,
# elabore el algoritmo que permite obtener la distancia entre A y B.


print("Ingrese las coordenadas del punto A:")
x1 = float(input("Ingrese la coordenada x: "))
y1 = float(input("Ingrese la coordenada y: "))

print("Ingrese las coordenadas del punto B:")
x2 = float(input("Ingrese la coordenada x: "))
y2 = float(input("Ingrese la coordenada y: "))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("La distancia entre A y B es:", distancia)

#https://interactivechaos.com/es/manual/tutorial-de-python/la-libreria-math
