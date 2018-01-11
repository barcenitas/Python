"""
Creado por Edgar Daniel Barcenas Martinez
Proteco Gen 34. FI UNAM
Diciembre 23, 2017
"Metodo del Slicing"
"""
palabra = 'Python'

# Indices:

# [P][y][t][h][o][n]
#  0  1  2  3  4  5
# -6 -5 -4 -3 -2 -1  

print ("Toda la palabra  = "+  palabra + "\n")
print ("Primer Caracter  = " + palabra[0])
print ("Segundo Caracter = " + palabra[1])
print ("Tercer Caracter  = " + palabra[2])
print ("Cuarto Caracter  = " + palabra[3])
print ("Quinto Caracter  = " + palabra[4])
print ("Ultimo Caracter  = " + palabra[5])

#El metodo de Slicing Consiste es partir alguna cadena utilizando sus indices

print(palabra[:])  #Nos muestra toda la cadena
print(palabra[1:]) #A partir de la posicion 1 imprime lo que siga hasta terminar
print(palabra[:3]) #Imprime hasta antes de la posicion 3
print(palabra[2:-1]) #imprime tho
print(palabra[-2:])  #imprime on

#Concatenar con el metodo de Slicing

print("Concatenado palabra[:2] + palabra[2:] = " + palabra[:2] + palabra[2:])

#Curisidades
print(palabra[99:])  #A partir de una posicion fuera de rango imprime espacios porque no hay nada.
print(palabra[:99] + "\n")  # Imprime la palabra completa 

#En python las cadenas son inmutables.

#Ejemplo de lo que no debe hacerse:
#palabra[0] = "N" o palabra[0] = 'N'

#Con el metodo de Slicing podemos hacer lo siguiente:

palabra = "N" + palabra[1:]

print (palabra)


#voltear una palabra con Slicing
palabraAlreves = "sodot a aloH" 

palabraBien = palabraAlreves[::-1]


print(palabraAlreves)
print(palabraBien)

