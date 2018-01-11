import random

#Generar numero flotante Aleatorio

random.random() # >= 0 y <1.0

random.uniform(1,10) # >=1 y <10

#Generar numero Entero Aleatorio

random.randrange(10) # >=0  y < 10
random.randrange(0,101) # >=0  y < 101
random.randrange(0,101,2) #Numero Par. >=0  y < 101
random.randrange(0,101,5) #Multiplo de 5. >=0  y < 101

c = "Hola Mundo"  #Aleaorio de la cadena
random.choice(c)  #Sirve para las listas
#Barajear
l=[1,2,3,4,5,6]
random.shuffle(l)
print(l)

#Muestra Aleatoria de la lista
random.sample(l,3)

