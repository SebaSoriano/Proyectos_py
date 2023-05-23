numeros1 = [1, 2, 3, 4]
numeros2 = [5, 6, 7, 8]
conca = numeros1 + numeros2 #se defina la variable conca como la concatenacion de ambas listas
print(conca) #se imprime el valor de conca

print(len(conca)) #se imprime el valor de la cantidad de elementos en conca

print(numeros1[0]) #se imprime el valor dentro de numeros1 que esta en la posicion 0
print(numeros2[3]) #se imprime el valor dentro de numeros2 que esta en la posicion 3
print(numeros1[-1]) #se imprime el valor dentro de numeros1 que esta en la posicion -1, o bien, en la 3

print(conca[0:4]) #se imprimen los valores entre las posiciones 0 y 3, la 4 no la toma
print(conca[0:8]) #se imprimen los valores entre las posiciones 0 y 8, considerar que solo existe hasta la posicion 7

comprobar1 = 9 in conca #variable que almacena el valor de verdad de la afirmacion
comprobar2 = 2 in conca
print(comprobar1) #se imprime el valor de verdad
print(comprobar2)

tupleado = (9, 10, 11, 12) #esto es un tuple, como una lista pero sus valores no se pueden modificar
#tupleado[0] = 5 #no se puede hacer pq da un error

stringeado = "Wena los k" #esto es una string, como una lista pero con caracteres y simbolos
#stringeado[0] = "G" #los string tampoco se pueden modificar