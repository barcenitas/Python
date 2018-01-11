"""
Created by Edgar Daniel Barcenas Martinez
Proteco Gen 34. FI UNAM
Diciembre 28, 2017
"Funciones Recursivas "
"""

#Factorial de un numero
def factorial(x):
	#print("Valor Inicial ->",x)
	if x > 1:
		x = x * factorial(x-1)
	return x

factorial(5)


