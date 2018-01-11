"""
Created by Edgar Daniel Barcenas Martinez
Proteco Gen 34. FI UNAM
Diciembre 28, 2017
"Excepciones"
"""

while(True):
	try:
		n = float(input("introduice un numero:"))
		m = 4.0
		print("{}/{}={}".format(n,m,n/m))
	except:
		print("Ha ocurrido un error")
	else:
		print("Todo ha funcionado correctamente")
		break

	finally:
		print("Fin de una iteracion")