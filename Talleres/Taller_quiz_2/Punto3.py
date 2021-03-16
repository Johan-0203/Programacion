listaPesos=[20000,30000,4000,2500,1000,7600]
mensajeMayor='El Mayor numero ingresado es'
mensajeMenor='El Menor numero ingresado es'
mensajeProm='El promedio es'

print(mensajeMayor, max(listaPesos))
print(mensajeMenor, min(listaPesos))
print(mensajeProm, sum(listaPesos)/len(listaPesos))