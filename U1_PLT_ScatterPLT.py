import matplotlib.pyplot as plt





x=[1,2,3,4,5,6,7,8]
y=[5,4,3,2,5,8,9,0]

plt.scatter(x,y,label='black points',color='r')

plt.title('scatter plot Example') 
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.show()
