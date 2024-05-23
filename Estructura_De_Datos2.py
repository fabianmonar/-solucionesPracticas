"""Desarrollar en Python un módulo que gestione una agenda telefónica en un diccionario de Python utilizando los recursos ya vistos (variables, input, print, if, if - else, while, for) que consideren adecuados para cada uno de estos casos:

Mostrar al usuario un menú de opciones

Opción 1: Agregar una persona (apellido, nombre, dni, email y número de teléfono). Esta opción debe agregar al diccionario a la persona que el usuario ingrese

Opción 2: Modificar una persona: dado su dni debe buscar la persona y preguntar si desea cambiar los demás campos de la persona, cambiando los que quiera."""

def menu():
    """Mostrar el menú de opciones."""
    print("AGENDA TELEFÓNICA")
    print("1. Agregar una persona")
    print("2. Modificar una persona")
    print("3. Salir")

def agregar_persona(agenda):
    """Agregar una persona a la agenda."""
    apellido = input("Ingrese el apellido de la persona: ")
    nombre = input("Ingrese el nombre de la persona: ")
    dni = input("Ingrese el DNI de la persona: ")
    email = input("Ingrese el correo electrónico de la persona: ")
    telefono = input("Ingrese el número de teléfono de la persona: ")
    agenda[dni] = {'apellido': apellido, 'nombre': nombre, 'email': email, 'telefono': telefono}
    print("Persona agregada exitosamente.")

def modificar_persona(agenda):
    """Modificar los datos de una persona."""
    dni = input("Ingrese el DNI de la persona que desea modificar: ")
    if dni in agenda:
        print("Datos actuales de la persona:")
        print("Apellido:", agenda[dni]['apellido'])
        print("Nombre:", agenda[dni]['nombre'])
        print("Email:", agenda[dni]['email'])
        print("Teléfono:", agenda[dni]['telefono'])
        modificar = input("¿Desea modificar los datos? (s/n): ")
        if modificar.lower() == 's':
            agenda[dni]['apellido'] = input("Nuevo apellido: ")
            agenda[dni]['nombre'] = input("Nuevo nombre: ")
            agenda[dni]['email'] = input("Nuevo correo electrónico: ")
            agenda[dni]['telefono'] = input("Nuevo número de teléfono: ")
            print("Datos modificados exitosamente.")
        else:
            print("No se han realizado modificaciones.")
    else:
        print("Persona no encontrada en la agenda.")

def main():
    """Función principal para ejecutar el programa."""
    agenda = {}
    while True:
        menu()
        opcion = input("Ingrese el número de la opción que desea ejecutar: ")
        if opcion == '1':
            agregar_persona(agenda)
        elif opcion == '2':
            modificar_persona(agenda)
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()
