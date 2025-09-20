from Bean.Empleado import Empleado

class GestionEmpleado:
    def __init__(self):
        self.empleados = []
        self.contador_id = 0

    def listar_empleados(self):
        for emp in self.empleados:
            print(emp)
    def agregar_empleado1(self):
        idEmpleado = self.contador_id
        nombre = input("Ingrese nombre del empleado: ")
        puesto = input("Ingrese puesto del empleado: ")
        salario = float(input("Ingrese salario del empleado: "))
        nuevo_empleado = Empleado(idEmpleado, nombre, puesto, salario)
        self.empleados.append(nuevo_empleado)
        print(f"Empleado {nombre} agregado exitosamente.")
        self.contador_id += 1
    
    def agregar_empleado2(self, empleado : Empleado):
        self.empleados.append(empleado)
        self.contador_id += 1
    
    def modificar_empleado(self, idEmpleado: int, nombre: str = None, puesto: str = None, salario: float = None):
        for emp in self.empleados:
            if emp.idEmpleado == idEmpleado:
                if nombre:
                    emp.nombre = nombre
                if puesto:
                    emp.puesto = puesto
                if salario:
                    emp.salario = salario
                return emp
        raise ValueError(f"Empleado con ID {idEmpleado} no encontrado.")