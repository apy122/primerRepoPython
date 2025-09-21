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
        print(f"Empleado {empleado.nombre} agregado exitosamente.")
        return
    
    def modificar_empleado (self):
        try:
            idEmpleado = int(input("Ingrese el ID del empleado a modificar: "))
        except ValueError:
            print("Entrada inválida. El ID debe ser un número.")

        for emp in self.empleados:
            if emp.idEmpleado == idEmpleado:
                nombre= input("Ingrese nuevo nombre del empleado: ")
                apellidos = input("Ingrese nuevo nombre del empleado: ")
                edad = int(input("Ingrese nueva edad del empleado: "))
                puesto = input("Ingrese nuevo puesto del empleado: ")
                emp.nombre = nombre
                emp.apellidos = apellidos
                emp.edad = edad
                emp.puesto = puesto
                print(f"Empleado con ID {idEmpleado} modificado exitosamente.")
                return
    
    def eliminar_empleado(self):
        try:
            idEmpleado = int(input("Ingrese el ID del empleado a eliminar: "))
        except ValueError:
            print("Entrada inválida. El ID debe ser un número.")

        for emp in self.empleados:
            if emp.idEmpleado == idEmpleado:
                self.empleados.remove(emp)
                print(f"Empleado con ID {idEmpleado} eliminado exitosamente.")
                return