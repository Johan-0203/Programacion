temperatura_coporal=[36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]
mensaje_max='La temperatura mas alta es'
mensaje_min='La temperatura mas baja es'
mensaje_tomado='La temperatura se tomaba cada'
print(mensaje_max,max(temperatura_coporal))
print(mensaje_min,min(temperatura_coporal))
print(mensaje_tomado, len(temperatura_coporal)/24*60, 'minutos')