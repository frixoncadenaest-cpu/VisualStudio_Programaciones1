notas = [10,8,9,5]
notas.append(20)
notas.insert(1,10)
print("longitud: ",len(notas))
print("suma: ",sum(notas))
print("maximo: ",max(notas))
print("minimo: ",min(notas))
notas.remove(9)
print("ordenadas: ",sorted(notas))
print(notas[2:])
print(notas[:2])
print(notas[::-1])

#tuplas
meses = (1,2,3,4,5,6,7,8,9,10,11,12)
print(meses[0])
print(meses[-1])
#meses[3]=15 #error: tuplas son inmutables
 
#diccionarios
estudiante={
    "cedula": "123456789",
    "nombre": "Frixon Cadena",
    "correo": "frixon@gmail.com",
    "celular": "0964079231",
    "notas": [10, 8, 9, 5]
}
print(estudiante.get("nombre"))
print(estudiante.keys())

#conjuntos
conjunto_a={1,1,5,4,6,8}
conjunto_b={1,9,6,5,4}
print(conjunto_a & conjunto_b)
print(conjunto_a | conjunto_b)

#Practico

