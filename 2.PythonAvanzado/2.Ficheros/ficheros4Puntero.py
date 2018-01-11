from io import open

fichero = open('fichero.txt','r')
fichero.seek(10)
fichero.read()
fichero.seek(0) #nos situa en el Caracter que le indiquemos
texto = fichero.read()

fichero.seek(len(texto)/2)

fichero.readline()
#r+ lectura mas escritura con el putero al inicio

#fichero.writelines(lineas) 