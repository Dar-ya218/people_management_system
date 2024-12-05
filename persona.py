class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo nombre
        self.edad = edad      # Atributo edad

    def saludar(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."
    
    def mostrar_info(self):
        return f"{self.nombre} tiene {self.edad} años."
