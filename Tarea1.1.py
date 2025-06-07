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
    
    
    

