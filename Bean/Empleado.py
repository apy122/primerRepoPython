from Bean.Persona import Persona

class Empleado(Persona):
    def __init__(self, idEmpleado, nombre, apellidos, edad, puesto):
        super().__init__(idEmpleado, nombre, apellidos)
        self.idEmpleado = idEmpleado
        self.puesto = puesto

    def saludar(self):
        print(f"Hola, soy {self.nombre} y trabajo como {self.puesto}")