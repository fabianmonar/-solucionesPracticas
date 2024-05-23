"""Desarrollar en Python las siguientes consignas utilizando los recursos ya vistos (variables, input, print, if, if - else, while, for) que consideren adecuados para cada uno de estos casos:

Pedir al usuario que ingrese 10 nombres de personas (input en un ciclo) no repetidas, guardarlos en una lista y mostrarlos. 

Eliminar la tercer y la última persona de la lista del ejercicio 1, luego ordenar la lista y mostrarlo

Guardar en un diccionario los datos de una persona: nombre, apellido, dni, email, fecha de nacimiento.

En un nuevo diccionario llamado familia guardar 4 personas, cada una de ellas con los mismos 5 datos (nombre, apellido, dni, email, fecha de nacimiento)

Guardar en una tupla los primeros n números pares. El valor de n que lo ingrese el usuario (input). Luego mostrar los datos de la tupla.

Nota: para saber si el número i es par hacer i % 2 == 0"""

# 1. Pedir al usuario que ingrese 10 nombres de personas (input en un ciclo) no repetidas, guardarlos en una lista y mostrarlos:
nombres = []
for _ in range(10):
    nombre = input("Ingrese un nombre de persona: ")
    if nombre not in nombres:
        nombres.append(nombre)
    else:
        print("El nombre ya ha sido ingresado. Intente nuevamente.")
print("Nombres ingresados:", nombres)

# 2. Eliminar la tercera y última persona de la lista del ejercicio 1, luego ordenar la lista y mostrarla:
del nombres[2]
del nombres[-1]
nombres.sort()
print("Nombres después de eliminar la tercera y última persona y ordenarlos:", nombres)

