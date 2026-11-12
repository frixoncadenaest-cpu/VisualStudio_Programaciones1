'''
Menu de usuarios
1.Ingrese el nombre: Mensaje de bienvenida
2.Menu de preguntas: Le va a preguntar las 11 preguntas Pregunta 1: listas Pregunta 2: Diccionario... Salir: 12
3.Salir

'''
def menu_usuarios():
    while True:
        print("==========================")
        print("      MENÚ DE USUARIOS     ")
        print("==========================")
        print("1. Ingrese el nombre: Mensaje de bienvenida")
        print("2. Menú de preguntas")
        print("3. Salir")
        try:
            opcion = int(input("Elija una opción (1-3): "))

            if opcion == 1:
                mensaje_bienvenida()
            elif opcion == 2:
                menu_preguntas()
            elif opcion == 3:
                print("Gracias por usar el programa")
                break
            else:
                print("Opción inválida. Intente de nuevo con 1, 2 o 3.")
        except ValueError:
            print("Error: Por favor, ingrese un número válido")

def mensaje_bienvenida():
    nombre = input("Ingrese su nombre: ")
    print("Bienvenido/a,", nombre, "Es un placer tenerte por aquí")


def menu_preguntas():
    while True: 
        print("--- MENÚ DE PREGUNTAS ---")
        print('1. ¿Qué imprime el siguiente código?: socio = {"nombre": "Ana", "saldo": 120}; print(socio.get("correo", "Sin correo"))')
        print('2. ¿Qué imprime el siguiente código?: print(int(9.99))')
        print('3. ¿Qué imprime el siguiente código?: print(type(10.0))')
        print('4. ¿Qué imprime el siguiente código?: a = {1, 2, 3, 4}; b = {3, 4, 5}; print(len(a & b))')
        print('5. ¿Qué imprime el siguiente código?: frase = "aprendo Python en TEC"; print(len(frase.split()))')
        print('6. ¿Qué imprime el siguiente código?: notas = {"Ana": 10, "Luis": 8}; for nombre, nota in notas.items(): print(f"{nombre}:{nota}", end=" ")')
        print('7. ¿Qué imprime el siguiente código?: total = 0; n = 1; while n <= 5: total += n; n += 1; print(total)')
        print('8. ¿Qué imprime el siguiente código?: suma = 0; for n in range(1, 5): if n % 2 != 0: continue; suma += n; print(suma)')
        print('9. ¿Cuántas veces se imprime «*» en el siguiente código?: for i in range(3): for j in range(2): print("*", end="")')
        print('10. ¿Qué imprime el siguiente código?: for i in range(3, 0, -1): print(i, end=" ")')
        print('11. Pida una frase y determine si es un palíndromo.')
        print('12. Salir al menú principal')

        try:
            opcion = int(input("Seleccione una opción de pregunta (1-12): "))
            if opcion == 1:
                print("Resultado: Sin correo")
            elif opcion == 2:
                print("Resultado: 9")
            elif opcion == 3:
                print("Resultado: <class 'float'>")
            elif opcion == 4:
                print("Resultado: 2")  
            elif opcion == 5:
                print("Resultado: 4")  
            elif opcion == 6:
                print("Resultado: Ana:10 Luis:8")
            elif opcion == 7:
                print("Resultado: 15")
            elif opcion == 8:
                print("Resultado: 6")  
            elif opcion == 9:
                print("Resultado: 6")  
            elif opcion == 10:
                print("Resultado: 3 2 1")
            elif opcion == 11:
                frase = input("Ingrese una frase: ")
                frase_limpia = frase.replace(" ", "").lower()
                frase_invertida = frase_limpia[::-1]
                if frase_limpia == frase_invertida:
                    print(frase, "es palíndromo")
                else:
                    print(frase, "no es palíndromo")
            elif opcion == 12:
                print("Saliendo del menú de preguntas...")
                break
            else:
                print("Opción no válida. Por favor, elija un número entre 1 y 12.")
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")
menu_usuarios()