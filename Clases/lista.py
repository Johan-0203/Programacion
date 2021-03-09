nombre = []
print(type(nombre))
print(nombre)
nombre =['Santi', 'Samuel','Daniel','Aleja']
print(nombre)
print(nombre[2])
nombre.append('Mauricio')
print(nombre)
print(nombre[2])
edad=[18,19,20,17,24,27,36,21,18,22]
estatura=[1.60,1.84,1.72,1.79]

#al ultimo
print(edad[-2])
print(edad[0:2])
print(edad[:3])
print(edad[2:])
edad.sort()
print(edad)
edad.sort(reverse=True)
print(edad)
mayor=max(edad)
print(mayor)
menor=min(edad)
print(edad)
#contar elementos
largolistaedad=len(edad)
prom=(sum(edad))/largolistaedad
print(prom)
#eliminar elemento
edad.pop(2)
print(edad)

#ciclo for y listas
largolistaedad=len(edad)
for indice in range(largolistaedad):
    print('estoy en la posicion',
    indice,'y valgo',
    edad[indice])
largolistanom=len(nombre)
for indice in range(largolistanom):
    print(nombre[indice])

posicionesconvalorespares=[]
for indice in range(largolistaedad):
    if(edad[indice]%2==0):
        posicionesconvalorespares.append(indice)

print(edad)
print(posicionesconvalorespares)

#solo cuando les interese mostrar la lista
for edades in edad:
    print(edades)
for nom in nombre:
    print(nom)