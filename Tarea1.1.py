#Rafael Ernesto Morales Diaz 
#20202001873 
#Tarea  1.1 de Inteligencia Artificial 


#Ejercicio1

def lista_numeros(lista):
    
    mayor = lista[0]
    for numero in lista:
        if numero > mayor:
            mayor = numero
    return mayor


numeros = [3, 9, 4, 1, 14]

resultado = lista_numeros(numeros)

print("El numero mas de alto de la lista es :", resultado)
