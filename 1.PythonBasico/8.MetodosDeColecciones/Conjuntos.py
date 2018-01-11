#Conjuntos
#Colecciones estan referenciadas en memoria

c = set() #Conjunto Vacio

c.add(1) #Añadir Elemento
c.add(2)
c.add(3)

c.discard(1) #Quitamos elemento

c2 = c.copy() #Copiamos un conjunto a otro

c2.clear() #limpiamos conjunto

#Comparar conjuntos
#Conjuntos Disyuntos -> Sin nada en comun
c1 = {1,2,3}
c2 = {3,4,5}
c3 = {1,-99}
c4 = {1,2,3,4,5}

c1.isdisjoint(c3) #Son disjuntos el C1 y C2
c1.issubset(c4) #C1 es subconjunto de C4
c4.issuperset(c1) #C4 es un super contenedor de C1

#Uniones, diferencias y conjuntos

c1.union(c2) == c4 #Union de conjunto C1 y C2 es igual al C4

c1.update(c2) #unirlos de verdad

c1 = {1,2,3}
c2 = {3,4,5}
c3 = {1,-99}
c4 = {1,2,3,4,5}

c1.difference(c2)
c1.difference_update(c2) 


#Devuelve un conjunto con elementos comunes
#Intercepcion

c1.intesection(c2)  #Solo nos muesta
c1.intesection_update(c2) #Lo guarda en el c1


#Elementos que no concuerdan entre 2 conjuntos
c1.symmmetric_difference(c2)













