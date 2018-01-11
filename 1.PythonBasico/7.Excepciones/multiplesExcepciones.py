"""
Created by Edgar Daniel Barcenas Martinez
Proteco Gen 34. FI UNAM
Diciembre 28, 2017
"Multiples Excepciones"
"""

try:
	n = float(input("introduce un numero"))
	5/n

except TypeError:
	print("No se puede dividir el numero por una cadena")
except ValueError:
	print("Debes introducir un numero")		
except ZeroDivisionError:
	print("No se puede dividir entre Cero")	
except Exception as e:
	print(type(e).__name__)	