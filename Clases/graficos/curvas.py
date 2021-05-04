import matplotlib.pyplot as plt

tiempo = [0,1,2,3,4,5]
sensor = [4,5,6,8,9,10]
plt.plot(tiempo,sensor,'--.g')
############
plt.title('Grafico Sensor Vs Tiempo')
plt.xlabel('Tiempo(s)')
plt.ylabel('Voltaje(mV)')
plt.savefig('Sensor.png')
############
plt.show()