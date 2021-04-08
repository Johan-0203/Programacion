def calcularIMC (peso=0, estatura=0):
    IMC = peso/(estatura**2)
    return IMC

print(round(calcularIMC(60,1.80),2))