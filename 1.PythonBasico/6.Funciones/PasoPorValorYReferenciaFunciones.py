"""
Created by Edgar Daniel Barcenas Martinez
Proteco Gen 34. FI UNAM
Diciembre 28, 2017
"Funciones Paso por Valor y paso por referencia"
"""

#Paso por referencia  -> Solo las listas
def doblarValores(numeros):
	for i,n in enumerate(numeros):
		numeros[i] *= 2

ns=[2,4,8]
doblarValores(ns)
print(ns)

#Paso por valor  ->Todos los tipos de Datos excepto listas
def numero(a):
	a=5
	print(a)

a=15
print(a)
numero(a)
print(a)

#Tratar a listas por paso por valor
def doblarValores2(numeros):
	for i,n in enumerate(numeros):
		numeros[i] *= 2

ns=[2,4,8]
doblarValores2(ns[:]) #Con Slicing se manda una copia de la lista.
print(ns)

