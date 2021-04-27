#Aqui explicaremos como hacer un grafico de barras
import matplotlib.pyplot as plt
lenguajes = ['py','java','dart','ta','elixir']
encuesta =[50,10,20,10,10]
plt.bar(lenguajes, encuesta, width = 0.6, color = 'b')
#--------------------------
plt.title('Lenguajes mas usados')
plt.xlabel('Lenguajes de programacion')
plt.ylabel('Porcentaje de uso')
plt.savefig('graficoLenguajes.png')
#--------------------------
plt.show()