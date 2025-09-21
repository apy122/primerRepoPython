from Bean.Persona import Persona

class Empleado(Persona):
    def __init__(self, idEmpleado, nombre, apellidos, edad, puesto):
        super().__init__(nombre, apellidos, edad)
        self.idEmpleado = idEmpleado
        self.puesto = puesto

    def __str__(self):
        return f"ID: {self.idEmpleado}, Nombre: {self.nombre} {self.apellidos}, Edad: {self.edad}, Puesto: {self.puesto}"

    def saludar(self):
        print(f"Hola, soy {self.nombre} y trabajo como {self.puesto}")