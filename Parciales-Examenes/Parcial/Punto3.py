#mensajes
preguntaBase='Ingrese la base del triangulo: '
preguntaAltura='Ingrese la altura del triangulo: '

def areaTriangulo (base = 0, altura = 0):
    area = (base * altura)/2
    return area


print(areaTriangulo(int(input(preguntaBase)),int(input(preguntaAltura))))