from io import open

#Escribir en un fichero
texto = "Una linea con texto \nOtra Linea con texto"

fichero = open('fichero.txt','w') #Modo de escritura 
#fichero = open('fichero.txt','r') #Modo Lectura 
#Borra y elimina contenido
fichero.write(texto)
#fichero.read(texto)
#lineas = fichero.readlines(texto) #Leer lineas
#read

fichero.close()


