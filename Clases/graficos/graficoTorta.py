import matplotlib.pyplot as plt

pielabels =['Python','Java','dart','js']
sizes =[30,25,25,20]
explode = [0,0,0.1,0]
plt.pie(sizes,labels=pielabels,explode=explode, shadow = 0.5, counterclock = 1, startangle = 45)
#----------------------------
plt.title('Uso de lenguajes de programacion en el 2021')
plt.savefig('tortaLenguajes.png')
#----------------------------
plt.show()