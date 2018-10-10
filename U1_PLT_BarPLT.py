import matplotlib.pyplot as plt

plt.bar( [1,2,3,4], [5,6,7,8], label = 'Example 1')
plt.bar( [6,7,8,5], [5,9,8,1], label = 'Example 2')

plt.title('Bar Graph Example') 
#plt.legend()
plt.xlabel('Student Rank')
plt.ylabel('No. of Student')
plt.show()
