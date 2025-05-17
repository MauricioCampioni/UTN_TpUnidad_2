#Ejercicio 1
# edad = input("¿Cuál es tu edad? ")
# if int(edad) >= 18:
#     print("Es mayor de edad")
    
    
#Ejercicio 2
# nota = input("¿Cuál es tu nota? ")
# if int(nota) >= 6:
#     print("Aprobado")
# else:
#     print("Desaprobado")
    
    
    
#Ejercicio 3
# numero= int(input("Ingrese un número: "))
# if numero % 2 == 0:
#     print("Ha ingresado un número par")
# else:
#     print("Por favor ingrese un número par")


#Ejercicio 4
# edad = int(input("¿Cuál es tu edad? "))
# if edad < 12:
#     print("Niño/a de 0 a 12 años")
# elif edad >= 12 and edad < 18:
#     print("Adolescente: entre 12 y 17 años")
# elif edad >= 18 and edad < 30:
#     print("Adulto/a joven: entre 18 y 29 años")
# elif edad >= 30:
#     print("Adulto/a: 30 años o más")


#Ejercicio 5
# contraseña = input("Ingrese la contraseña: ")
# if len(contraseña) >= 8 and len(contraseña) <= 14:
#     print("Ha ingresado una contraseña correcta")
# else:
#     print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


#Ejercicio 6
# from statistics import mode, median, mean
# import random

# numeros_aleatorios = [random.randint(1, 100) for i in range(10)]

# media = mean(numeros_aleatorios)
# mediana = median(numeros_aleatorios)
# moda = mode(numeros_aleatorios)

# print ("Media: ", media)
# print ("Mediana: ", mediana)
# print ("Moda: ", moda)

# if media > mediana > moda:
#     print("La media es mayor que la mediana y la moda")
# elif media < mediana < moda:
#     print("La media es menor que la mediana y la moda")
# elif media == mediana == moda:
#     print("La media, la mediana y la moda son iguales")
# else:
#     print("No se cumple ninguna de las condiciones anteriores")


#Ejercicio 7
# frase = input("Ingrese una frase: ")
# if frase [-1].lower() in "aeiou":
#     print("La frase termina en vocal")
#     frase += "!"
# print(frase)


#Ejercicio 8
# nombre = input("Ingrese su nombre: ")

# opcion = int(input("Ingrese una opción (1, 2 o 3): "))
# if opcion == 1:
#     nombre = nombre.upper()
#     print("Su nombre en mayúsculas es:", nombre)
# elif opcion == 2:
#     nombre = nombre.lower()
#     print("Su nombre en minúsculas es:", nombre)
# elif opcion == 3:
#     nombre = nombre.title()
#     print("Su nombre es:", nombre)

#Ejercicio 9
# Magnitud_terremeto = float(input("Ingrese la magnitud del terremoto: "))
# if Magnitud_terremeto < 3.0:
#     print("Muy Leve")
# elif Magnitud_terremeto >= 3.0 and Magnitud_terremeto < 4.0:
#     print("Ligeramente perceptible")
# elif Magnitud_terremeto >= 4.0 and Magnitud_terremeto < 5.0:
#     print("Moderado")
# elif Magnitud_terremeto >= 5.0 and Magnitud_terremeto < 6.0:
#     print("Fuerte")
# elif Magnitud_terremeto >= 6.0 and Magnitud_terremeto < 7.0:
#     print("Muy fuerte")
# elif Magnitud_terremeto >= 7.0:
#     print("Extremo")


#Ejercicio 10
def ejercicio_10():
    hemisferio = input("Ingrese el hemisferio (N/S): ").upper()
    mes = int(input("Ingrese el número del mes (1-12): "))
    dia = int(input("Ingrese el día del mes: "))
    if (mes == 12 and dia >= 21) or mes in [1, 2] or (mes == 3 and dia <= 20):
        estacion_norte = "Invierno"
        estacion_sur = "Verano"
    elif (mes == 3 and dia >= 21) or mes in [4, 5] or (mes == 6 and dia <= 20):
        estacion_norte = "Primavera"
        estacion_sur = "Otoño"
    elif (mes == 6 and dia >= 21) or mes in [7, 8] or (mes == 9 and dia <= 20):
        estacion_norte = "Verano"
        estacion_sur = "Invierno"
    else:
        estacion_norte = "Otoño"
        estacion_sur = "Primavera"
    if hemisferio == "N":
        print(estacion_norte)
    elif hemisferio == "S":
        print(estacion_sur)
    else:
        print("Hemisferio inválido")
    