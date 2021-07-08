import matplotlib.pyplot as plt 
import numpy as np 
from trilat import * 
from matplotlib.patches import Circle 


plt.ion()
fig, ax=plt.subplots()
plt.xlim(-5, 15)
plt.ylim(-5, 15)
D1=[10, 9, 8, 7, 6, 5]
D2=[10, 9, 8, 7, 6 ,5]
D3=[5, 6 ,7, 8, 9, 10]

D1=np.array(D1)
D2=np.array(D2)
D3=np.array(D3)

print(D1, D2, D3)

for i in range(len(D1)): 
    plt.clf()
    plt.xlim(-5, 15)
    plt.ylim(-5, 15)
    #d1=D1[i]
    #print(d1)
    range1 = Circle((10, 10), D1[i], fill = False)
    plt.gca().add_patch(range1)
    plt.Circle((10, 10), D1[i], fill = False)
    #ax.add_artist(range1)
    #d2=D2[i]
    #print(d2)
    range2 = Circle((0, 10), D2[i], fill = False)
    plt.Circle((0, 10), D2[i], fill = False)
    plt.gca().add_patch(range2)

    d3=D3[i]
    print(d3)
     #plt.pause(1)
    range3 = Circle((0, 0), D3[i], fill = False)
    plt.Circle((10, 10), D3[i], fill = False)
    plt.gca().add_patch(range3)
    plt.show()
    
    #
    #
    #


           
#plt.scatter(x, y)
#plt.pause(0.2)
plt.ioff()
plt.show()


             

#ax = plt.scatter()








