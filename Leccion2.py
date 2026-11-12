#Correcion leccion2
print('Pregunta 1: ¿Qué imprime el siguiente código?: socio = {"nombre": "Ana", "saldo": 120}; print(socio.get("correo", "Sin correo"))')
socio = {"nombre": "Ana", "saldo": 120}
print(socio.get("correo", "Sin correo"))

print('Pregunta 2: ¿Qué imprime el siguiente código?: print(int(9.99))')
print(int(9.99))

print('Pregunta 3: ¿Qué imprime el siguiente código?: print(type(10.0))')
print(type(10.0))

print('Pregunta 4: ¿Qué imprime el siguiente código?: a = {1, 2, 3, 4}; b = {3, 4, 5}; print(len(a & b))')
a = {1, 2, 3, 4}
b = {3, 4, 5}
print(len(a & b))

print('Pregunta 5: ¿Qué imprime el siguiente código?: frase = "aprendo Python en TEC"; print(len(frase.split()))')
frase = "aprendo Python en TEC"
print(len(frase.split()))

print('Pregunta 6: ¿Qué imprime el siguiente código?: notas = {"Ana": 10, "Luis": 8}; for nombre, nota in notas.items(): print(f"{nombre}:{nota}", end=" ")')
notas = {"Ana": 10, "Luis": 8}
for nombre, nota in notas.items():
    print(f"{nombre}:{nota}", end=" ")

print('Pregunta 7: ¿Qué imprime el siguiente código?: total = 0; n = 1; while n <= 5: total += n; n += 1; print(total)')
total = 0
n = 1
while n <= 5:
    total += n
    n += 1
print(total)

print('Pregunta 8: ¿Qué imprime el siguiente código?: suma = 0; for n in range(1, 5): if n % 2 != 0: continue; suma += n; print(suma)')
suma = 0
for n in range(1, 5):
    if n % 2 != 0:
        continue
    suma += n
print(suma)

print('Pregunta 9: ¿Cuántas veces se imprime «*» en el siguiente código?: for i in range(3): for j in range(2): print("*", end="")')
for i in range(3):
    for j in range(2):
        print("*", end="")

print('Pregunta 10: ¿Qué imprime el siguiente código?: for i in range(3, 0, -1): print(i, end=" ")')
for i in range(3, 0, -1):
    print(i, end=" ")

print('11: Pida una frase y determine si es un palíndromo.')
frase = input("Ingrese una frase: ")
frase_limpia = frase.replace(" ", "").lower()
frase_invertida = frase_limpia[::-1]
if frase_limpia == frase_invertida:
    print(frase, "es palíndromo")
else:
    print(frase, "no es palíndromo")