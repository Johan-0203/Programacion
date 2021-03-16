temperatura_coporal=[36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]
mensaje_hipotermia='Hipotermia'
mensaje_fiebre='Fiebre'
mensaje_Normal='Normal'
for posicion in temperatura_coporal:
    if (posicion<36):
        print(posicion, '->',mensaje_hipotermia)
    elif(posicion>=36 and posicion<=37.5):
        print(posicion, '->',mensaje_Normal)
    else:
        print(posicion, '->',mensaje_fiebre)