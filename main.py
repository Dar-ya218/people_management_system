from persona import Persona  # Importamos la clase Persona

def agregar_persona():
    nombre = input("¿Cómo te llamas? ")
    edad = int(input("¿Cuántos años tienes? "))
    nueva_persona = Persona(nombre, edad)
    return nueva_persona

def saludar_todas(personas):
    for persona in personas:
        print(persona.saludar())

def mostrar_todas(personas):
    for persona in personas:
        print(persona.mostrar_info())

def menu():
    personas = []  # Lista de personas
    while True:
        print("\n----- MENÚ -----")
        print("1. Agregar una persona")
        print("2. Saludar a todas las personas")
        print("3. Mostrar información de todas las personas")
        print("4. Salir")

        opcion = input("Elige una opción (1-4): ")

        if opcion == '1':
            persona = agregar_persona()
            personas.append(persona)
        elif opcion == '2':
            saludar_todas(personas)
        elif opcion == '3':
            mostrar_todas(personas)
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elige una opción del 1 al 4.")

if __name__ == "__main__":
    menu()
