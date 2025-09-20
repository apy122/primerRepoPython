#Importo abstract
from abc import ABC,abstractmethod

#clase
class  Persona(ABC):
    def __init__(self, nombre, apellidos, edad):
        self.nombre= nombre
        self.apellidos= apellidos
        self.edad= str(edad)
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Apellidos: {self.apellidos}, Edad: {self.edad}"
    
    @abstractmethod
    def saludar(self):
        pass