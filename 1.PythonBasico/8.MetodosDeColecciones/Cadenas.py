#Cadenas

saludo = "Hola Mundo"

saludo.upper() #Mayusculas

saludo.lower()  #Minusculas

saludo.capitalize()  #Primer caracter en Mayuscula

saludo.title()  # Primer de cada palabra en Mayuscula

saludo.count('mundo') #cuentas veces aparece mundo

saludo.find('mundo') #busca la primer aparicion de mundo y regresa su posicion

saludo = "Hola mundo mundo"

saludo.rfind('mundo') #regresa la posicion de la ultima aparacion de la cadena

#comprobar
c = '100'

c.isdigit()  #comprueba si la cadena es un numero

#Comprueba si es alfanumerico
c2="ABC10034p" 

c2.isalnum()

#comprobar si solo tiene caracteres del abecedario
c2.isalpha()

C3 = "Hola Mundo"

#comprueba si es mayuscula
c3.isupper()
#comprueba si es minuscula
c3.islower()
#comprueba si es un titulo
c3.istitle()
#Comprobar si es un espacio
c4 = " "
c4.ispace()

#comprobar si empieza con algun caracter
c3.startwith("Hola")

#comprobar si termina con algun caracter
c3.endswith("mundo")

#Separar palabra

c3.split()  #devueleve lista con las palabras
c3.split()[0]  #devueleve lista con la ultima posicion

c3 = "Hola,Hola,Hola"

c3.split(',') #Separar por comas

c3=','

c3.join("Hola") #Separar Hola con comas

c3="---- Hola ---"

c3.strip('-') #Elimina el caracter 

c3= "Hola Mundo Mundo Mundo Mundo"

c3.replace('o',0)  #Remplaza un caracter por otro

c3.replace('mundo','',4) #Remplazar con espacios donde diga mundo solo 4 veces 






