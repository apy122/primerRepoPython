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
    
    def modificar_empleado (self):
        idEmpleado= int(input("Ingrese el ID del empleado a modificar: "))
        for emp in self.empleados:
            try:
                if self.empleados != None and emp.idEmpleado == idEmpleado:
                    emp.nombre = input("Ingrese nuevo nombre del empleado (dejar en blanco para no cambiar): ")
                    emp.apellido = input("Ingrese nuevo apellido (dejar en blanco para no cambiar): ")
                    emp.edad = input("Ingrese nueva edad del empleado (dejar en blanco para no cambiar): ")
                    emp.puesto = input("Ingrese nuevo puesto del empleado (dejar en blanco para no cambiar): ")
            except ValueError:
                print("Entrada invalida. Por favor, intente de nuevo.")
                return
            
            raise ValueError(f"Empleado con ID {idEmpleado} no encontrado.")
        