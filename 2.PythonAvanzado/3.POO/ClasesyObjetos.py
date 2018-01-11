"""
Created by Edgar Daniel Barcenas Martinez
Proteco Gen 34. FI UNAM
Diciembre 28, 2017
"Excepciones"
"""


try:
	n = input("introduce un numero")
	5/n

except Exception as e:
	print( type(e).__name__ )

	