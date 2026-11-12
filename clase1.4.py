#Declaracion de funciones
def saludar():
    print("Hola, Frixon")
saludar()

#Funcion con parametro
#def calcular_edad(anio_nacimiento, anio_actual):
 #   print("La edad es: ", anio_actual-anio_nacimiento," años")
#a=int(input("Ingrese su año de nacimiento: "))
#b=int(input("Ingrese el año actual: "))
#calcular_edad(a,b)

#Funciones con retorno
def calcular_iva(precio, iva):
    return precio*iva
resultado=calcular_iva(10,0.15)
print("El iva es: ",resultado)

#Funciones con valores por defecto
def calcular_iva(precio, iva=0.15):
    return precio*iva
resultado=calcular_iva(100, 0.14)
print("El iva es: ", resultado)

#Funciones con listas
def calcular_par(numeros):
    for e in numeros:
        if e%2==0:
            print("El número",e, "es par") 
        else:
            print("El número",e,"es impar")
lista_numeros= range(0,10)
calcular_par(lista_numeros)
lista_numeros=range(5,0,-1)
for e in lista_numeros:
    print(e, end=" ")

#Funciones con tuplas
def suma_numeros(*a):
    return sum(a)
print("la suma es: ",suma_numeros(1,2,3))

#Funciones con diccionarios
def estudiantes(**lista_estudiantes):
    suma_total=0
    for nombre, edad in lista_estudiantes.items():
        print("El estudiante ",nombre,"tiene ", edad," años")
        suma_total+=edad
        print("suma de edades: ", suma_total)
estudiantes(Frixon=20, Juan=25, Maria=30, Andres=40, Gina=34, David=18, Alex=20)

'''
Menu de usuarios
1.Ingrese el nombre: Mensaje de bienvenida
2.Menu de preguntas: Le va a preguntar las 11 preguntas Pregunta 1: listas Pregunta 2: Diccionario... Salir: 12
3.Salir

'''