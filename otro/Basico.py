#input de dato
edad= int(input("Inserte edad:"))

#Condicionales
if edad<18:
    print("Menor de edad")
elif  edad>18 and edad<65:
    print("Eres adulto")
else:
    print("Eres una persona mayor")

#Recorrer numeros
for i in range(10):
    print(i)

#Recorrer numeros  otra forma
numero=1
while numero <=5:
    print(numero)
    numero +=1

#Funcion
def saludar():
    print("hello world")

saludar()