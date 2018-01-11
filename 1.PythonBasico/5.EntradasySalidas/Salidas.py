"""
Created by Edgar Daniel Barcenas Martinez
Proteco Gen 34. FI UNAM
Diciembre 28, 2017
"Salidas"
"""

v = "otro texto"

n = 10

print("Esto es",v,"y un numero",n)

c = "Esto es '{}' y un numero '{}'".format(v,n)

print(c)
print("Esto es '{1}' y un numero '{0}'".format(v,n))
print("Esto es '{texto}' y un numero '{num}'".format(texto=v,num=n))


print("Esto es '{v}' y un numero '{n}'".format(v=v,n=n))

print("Esto es '{v}','{v}','{v}' y un numero '{n}'".format(v=v,n=n))

print("{:>30}".format("Palabra"))  #30 caracteres a la derecha
print("{:30}".format("Palabra"))  #30 caracteres a la izquierda jaja

print("{:^30}".format("Palabra"))  #30 caracteres al centro

print("{:.2}".format("Palabra"))  #Truncamiento a dos caracteres

#Formateo de numeros enteros rellenados con espacios
print("{:4d}".format(10))
print("{:4d}".format(100))
print("{:4d}".format(1000))
#Formateo de numeros enteros rellenados con ceros
print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))

#Formateo de numeros flotantes, rellenados con espacios
print("{:7.3f}".format(3.1415161814)) #7 Espacios y 3 decimales
print("{:07.3f}".format(3.1415161814)) #7 Espacios con ceros y 3 decimales



