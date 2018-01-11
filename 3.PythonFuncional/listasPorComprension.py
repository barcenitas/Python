#Comprension de listas

lista = [letra for letra in 'casa']
print(lista)

lista = [numero**2 for numero in range(0,11)]
print(lista)


lista = [numero for numero in range(0,11) if numero % 2 == 0]



pares = [numero for numero in [numero**2 for numero in range(0,11)] if numero %2 == 0]