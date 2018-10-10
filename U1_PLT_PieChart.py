import matplotlib.pyplot as plt

slices = [7,2,2,13]



activities = ['sleeping', 'eating', 'working','playing']

cols = ['c','m','r','b']

plt.pie(slices, labels=activities, colors = cols, 
	startangle=90,shadow = True, explode = (0,0,0,0))

plt.title('Pie Chart Example') 
plt.legend()
plt.show()
