#  Cargar una lista con 5 elementos enteros. Imprimir el mayor y un mensaje si 
# se repite dentro de la lista (es decir si dicho valor se encuentra en 2 o más
#  posiciones en la lista) 
listaEnteros=[]
for x in range(5):
    valor=int(input('Valor: '))
    listaEnteros.append(valor)
mayor=listaEnteros[0]
repite=0
for y in range(len(listaEnteros)):
    if y>mayor:
        mayor=listaEnteros[y]
    if(mayor==listaEnteros[y]):
        repite+=1
print(mayor, repite)