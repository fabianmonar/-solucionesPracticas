"""EJERCICIO 1: Un estudiante está cursando 5 materias, tiene la nota de cada
materia y quiere saber cuál es su promedio."""
# Notas del estudiante
nota1 = float(input("Ingrese la nota de la materia 1: "))
nota2 = float(input("Ingrese la nota de la materia 2: "))
nota3 = float(input("Ingrese la nota de la materia 3: "))
nota4 = float(input("Ingrese la nota de la materia 4: "))
nota5 = float(input("Ingrese la nota de la materia 5: "))

# Calculando el promedio
promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

print("El promedio del estudiante es:", promedio)