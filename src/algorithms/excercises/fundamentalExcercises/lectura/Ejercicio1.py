print("---------------------------------");
print("Ejercicio 1 - Calcular Distancia");
print("---------------------------------");
print("");

''' Se desea calcular la distancia recorrida (m) por un móvil 
que tiene velocidad constante  (m/s) durante   un   tiempo   t (s),   
considerar   que   es   un   MRU (Movimiento Rectilíneo Uniforme). '''

print("Ingrese los datos que se le piden: ")
vl = float(input("Ingres la velocidad del objeto: "))
tp = int(input("Ingrese el tiempo que se ha movido el objeto: "))

distancia = vl * tp;

print("La distancia recorrida por el objeto es: " + str(distancia) + "ms");