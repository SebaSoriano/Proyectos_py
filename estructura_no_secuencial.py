set1 = set([1,1,2,2,2,3,3,3,3,4,4,4,4,5,6,7,8,9,10]) #un set es un conjunto matematico de elementos
lista = [1,1,2,2,3,4,5,6,7,8,9,10] #una lista es un conjunto de elementos simple

set2 = set([2,2,4,4,4,6,8,10,12,14,16,18,20])

print(set1)
print(len(set1)) #la cantidad de elementos que estan en set1 es 10
print(lista)

resta1 = set1 - set2 #los elementos que estan en set1 pero no en set2
resta2 = set2 - set1 #los elementos que estan en set2 pero no en set1
interseccion = set1 & set2 #la interseccion se denota por & ampersand
union = set1 | set2 #la union se denota por | pipe

print(resta1)
print(resta2)
print(interseccion)
print(union)

persona = {"nombre": "Juan", "apellido": "Perez", "edad": 40} #esto es un diccionario
#se define una palabra clave y se le asigna una cosa
print(persona["nombre"]) #se imprime el valor asignado a la palabra clave nombre
print(len(persona)) #se imprime la cantidad de palabras claves que tenemos definidas
print("edad" in persona) #se imprime el valor de verdad