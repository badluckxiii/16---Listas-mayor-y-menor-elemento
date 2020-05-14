# Ingresar por teclado los nombres de 5 personas y almacenarlos en una lista. 
# Mostrar el nombre de persona menor en orden alfabético. 
llista=[]
for x in range(5):
    nom=input('Nom:')
    edad=int(input('Edad: '))
    llista.append([nom,edad])
min=llista[0][1]
nom=llista[0][0]
for y in range(len(llista)):
    print('Edad',llista[y][1])
    if llista[y][1]<min:
        nom=llista[y][0]
print('El menor d\'edad es ',nom)