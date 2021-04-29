import matplotlib.pyplot as plt
equipos = ['Real Madrid','Barcelona','Milan','Liverpool','Bayern','Ajax','Juventus','Atletico']
titulos =[19,14,14,13,9,8,8,7]
plt.bar(equipos, titulos, width = 0.6, color = 'b')
#--------------------------
plt.title('Equipos ganadores de champions')
plt.xlabel('Equipos de futbol')
plt.ylabel('Titulos ganados')
plt.savefig('graficoChampions.png')
#--------------------------
plt.show()