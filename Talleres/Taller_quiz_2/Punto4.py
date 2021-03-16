listaPesos=[20000,30000,4000,2500,1000,7600]
preguntaBorrarPos='Ingrese la posicion que desa borrar'
print(listaPesos)
posicion=int(input(preguntaBorrarPos)) - 1
listaPesos.pop(posicion)
print(listaPesos)
