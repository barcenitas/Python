#Diccionarios

colores = {"amarillo":"yellow","azul":"blue","verde":"green"}

colores["amarillo"]

colores.get('negro','No se encuentra')

'amarillo' in colores

#iterar sobre diccionario
colores.keys()
colores.values()
colores.items()

for c in colores.keys():
	print(c)

for c,v in colores.items():
	print(c,v)

colores.pop("amarillo","no encuentra")

colores.clear()


