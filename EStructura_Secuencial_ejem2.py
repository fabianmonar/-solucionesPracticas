"""EJERCICIO 2: Un pintor de casas debe hacer un presupuesto para un cliente. Lo

que cobra se calcula de acuerdo a los metros cuadrados que debe pintar. El

cliente le indica que necesita conocer el costo de mano de obra para pintar una

pared rectangular de un galpón. El pintor cobra un monto ﬁjo por cada metro

cuadrado. Puedes hacer un algoritmo para calcular el costo de mano de obra para

pintar la pared."""
# Dimensiones de la pared
largo = float(input("Ingrese el largo de la pared en metros: "))
ancho = float(input("Ingrese el ancho de la pared en metros: "))

# Costo por metro cuadrado
costo_por_metro_cuadrado = float(input("Ingrese el costo por metro cuadrado de pintura: "))

# Calculando el área de la pared
area_pared = largo * ancho

# Calculando el costo de mano de obra
costo_mano_de_obra = area_pared * costo_por_metro_cuadrado

print("El costo de mano de obra para pintar la pared es:", costo_mano_de_obra)