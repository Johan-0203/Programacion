import funciones as fn

print(fn.sumar(2,4))

def sumar (a,b):
    return a+b+a

print(fn.calcular(sumar,2,4))
print(fn.calcular(fn.sumar,2,4))
