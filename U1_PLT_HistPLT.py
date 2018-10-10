import matplotlib.pyplot as plt


ages=[4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9, 11,23,22,12,15,20,25]

bins=[0,5,10,15,20]

plt.hist(ages, bins, histtype='bar',rwidth=0.25)

plt.title('Histogram Example') 
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.show()