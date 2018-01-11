"""
Created by Edgar Daniel Barcenas Martinez
Proteco Gen 34. FI UNAM
Diciembre 28, 2017
"Funciones "
"""

#Definicion de funciones
def saludo():
	c="Hola desde funcion"
	print(c)

saludo()

#Funciones que retornan valor
def saludo():
	c="Hola desde funcion"
	return c

saludo()


#Funciones que reciben y retornan valores
def suma(a,b):
	return a+b

print(suma(5,10))
