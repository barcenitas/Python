from collections0 import Counter

l= [1,1,2,2,2,3,4,5,5,5,5]

Counter(l)


p = "Palabra"

Counter(p)

#Contar palabras

animales = ["perro","perro","perro","gato"]

animales.split()

Counter(animales.split())

c = Counter(animales.split())

c.most_common(1) #Elementos mas comunes
#el numero mas comun o los n numeros mas comunes

l=[10,20,20,20,20,10]


c.most_common() #Sin parametro regresa una  lista ordenada de la mayor elemento comun al menos comun

l=[10,20,30,10,20,20,10]

c.keys() #Devuelve claves con los valores que se repiten

c.values()

sum(c.values())

 
