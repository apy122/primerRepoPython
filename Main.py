from Gestion.GestionEmpleado import GestionEmpleado
from Bean.Empleado import Empleado

menu =["Menu:",
        "1. Mostrar Empleados",
        "2. Agregar empleado",
        "3. modificar empleado",
        "4. eliminar empleado",
        "5. Salir"
        ]

class main():
   def __init__(self):
      self.menu=menu
      self.gestion= GestionEmpleado()
      self.nextId=0
      self.opcion= 0
      
      #Crear empleados ejemplo
      emp1 = Empleado(1,"Ana", "Ventas",22, "It")
      emp2 = Empleado (2,"Luis", "TI",21, "Desarrollador")
      emp3 = Empleado(3, "Marta", "RRHH", 25,  "Coordinadora")

      self.gestion.agregar_empleado2(emp1)
      self.gestion.agregar_empleado2(emp2)
      self.gestion.agregar_empleado2(emp3)
   
   def mostrar_menu(self):
      for opcion in self.menu:
         print(opcion)
      self.opcion=int(input("Seleccione una opcion: "))

      while self.opcion !=5:

        if self.opcion==1:
            self.gestion.listar_empleados()
            break
        
        elif self.opcion==2:
            self.gestion.agregar_empleado1()
            
        
        elif self.opcion==3:
            GestionEmpleado.modificar_empleado(self)
            print("Modificar empleado")
            
        
        elif self.opcion==4:
            GestionEmpleado.eliminar_empleado(self)
            print("Eliminar empleado")
            
        
        else:
            print("Opcion no valida")
            
      volverMenu = input("Desea volver al menu? (s/n): ")
      if volverMenu == "n" or volverMenu == "N" or volverMenu == "no" or volverMenu == "No":
          self.opcion = 5
      else:
          self.mostrar_menu()

#ejecutar app
app = main()
app.mostrar_menu()