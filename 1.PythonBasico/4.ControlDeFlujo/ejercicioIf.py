"""
Created by Edgar Daniel Barcenas Martinez
Proteco Gen 34. FI UNAM
Diciembre 28, 2017
"IF ejercicio"
"""

"""
Programa que nos dice si un numero ingresado por el usuario es entero o real
"""
numero = int(input('Proporciona un número: '))
if numero % 2 == 0 :
	print('es par')
else: 
	print('es impar')
	if numero % 3 == 0 :
		print('es multiplo de 3')
	if numero % 5 == 0 :
		print('es multiplo de 5')
	if numero % 7 == 0 :
		print('es multiplo de 7')
	if  numero % 3 != 0 or numero % 5 != 0 or numero % 7 != 0:
		print('tu nombre')