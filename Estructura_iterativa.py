#1. Mostrar los números desde el 0 al número solicitado al usuario (input):


# Solicitar al usuario un número
numero = int(input("Ingrese un número: "))

# Mostrar los números desde 0 hasta el número ingresado
for i in range(numero + 1):
    print(i)
#2. Mostrar sólo los números pares desde 0 hasta el número ingresado (input):


# Solicitar al usuario un número
numero = int(input("Ingrese un número: "))

# Mostrar solo los números pares desde 0 hasta el número ingresado
for i in range(numero + 1):
    if i % 2 == 0:
        print(i)
#3. Pedir que el usuario ingrese (input) nombres de personas y mostrarlos hasta que el valor de lo que ingresa sea “fin”:


# Pedir al usuario que ingrese nombres de personas
print("Ingrese los nombres de las personas. Para terminar, escriba 'fin'.")
nombres = []
nombre = input("Nombre: ")
while nombre != "fin":
    nombres.append(nombre)
    nombre = input("Nombre: ")

# Mostrar los nombres ingresados
print("Nombres ingresados:")
for nombre in nombres:
    print(nombre)