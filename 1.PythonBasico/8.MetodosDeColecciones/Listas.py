#Listas

lista = [1,2,3,4,5]
lista.append(6)  #Añadir al Final

lista.clear() #Limpia la lista

l1 = [1,2,3]
l2 = [4,5,6]

l1.extend(l2)  #Unir lista 2 con la 1

l1.count(4) #Cuenta las apariciones del 4 en la lista

l1.index(4) #Muestra la posicion de la primer coincidencia

l1.insert(-1,20)  #Añadir elemento -> Posicion, elemento
#-1 es el penultimo elemento

#Para añadir en la ultima posicion es necesario poner la posicion pero positiva
# Tambien podemos poner en posicion un numero grande y al no encontrarlo se agrega en la ultima posicion

l1.insert(20,10) #Posicion, Valor


#Sacar valor de la lista

l1.pop(0) # Sacamos posicion Cero

#Eliminar con Remove

l1.Remove(10) #Eliminamos el elemento-> Valor 


l1.reverse()  #Da la vuelta a la lista. Revirtiendo la lista


l1.sort() #ordenar la lista
l1.sort(reverse=True) #Ordenar con un orden inverso

#Revertir una Cadena utilizando una lista con el metodo join()

cadena = "Hola Mundo"

l1=list(cadena)

cadena = "".join(l1)

print(cadena)
