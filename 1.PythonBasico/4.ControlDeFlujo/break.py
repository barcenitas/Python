"""
Created by Edgar Daniel Barcenas Martinez
Proteco Gen 34. FI UNAM
Diciembre 28, 2017
"Break"
"""

#Sentencia break
#Se utiliza en ciclos for y while con el fin de terminar el bucle actual
#Se ejecuta el codigo siguiente al bucle

for i in range(1, 50):
	if(i == 20):
		break
	print(i)

print("Sali del bucle")
print()
#Sentencia continue
#Termina la iteracion actual y continua con la siguiente
for i in "Python":
	if(i == "h"):
		continue
	print(i)
print()
x = 2
while(x < 20):
	if(x == 10):
		break
	print(x)
	x += 1 # x = x + 1



