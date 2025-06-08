print("Rafael Ernesto Morales Diaz") 
print("20202001873") 
print("Tarea  1.1 de Inteligencia Artificial")
print() 


print("Ejercicio1")

def lista_numeros(lista):
    
    mayor = lista[0]
    for numero in lista:
        if numero > mayor:
            mayor = numero
    return mayor


numeros = [3, 9, 4, 1, 14]

resultado = lista_numeros(numeros)

print("El numero mas de alto de la lista es :", resultado)
print()

print("---------------------------------------------------")


print("Ejercicio 2") 

numero = int(input("Ingrese un numero para la tabla de multiplicar : "))

for i in range(1,11):
    
    multiplicacion = numero * i
    print(f"{numero} x {i} = {multiplicacion}")
  
print() 
print("---------------------------------------------------")
print("Ejercicio 3")

lista = [4, 2, 7, 4, 2, 1, 9, 7]

lista_unica = sorted(set(lista))    

print("La lista original es :", lista)
print("La lista sin numeros repetidos es :", lista_unica)

print()

print("---------------------------------------------------")
print("Ejercicio 4")
estudiantes = {}

while True:
    nombre = input("Escriba el nombre del estudiante o escriba salir para terminar: ")
    if nombre.lower() == 'salir':
        break
    try:
        nota = float(input(f"Ingrese la nota de {nombre}: "))
        estudiantes[nombre] = nota
    except ValueError:
        print("Por favor, ingrese un valor valido para la nota.")


print("\nDatos de los estudiantes:")
for nombre, nota in estudiantes.items():
    print(f"{nombre}: {nota}")
    
    
print()

print("---------------------------------------------------")
print("Ejercicio 5")    

ventas = {
    'Producto': ['A', 'B', 'A', 'C', 'B', 'A'],
    'Cantidad': [10, 5, 7, 3, 2, 8]
}

resultado = {}

for i in range(len(ventas['Producto'])):
    
    producto = ventas['Producto'][i]
    
    cantidad = ventas['Cantidad'][i]

    if producto in resultado:
        
        resultado[producto] = resultado[producto]+cantidad
    else:
        resultado[producto] = cantidad

print("Ventas por cada uno de los producto")
print(resultado)    